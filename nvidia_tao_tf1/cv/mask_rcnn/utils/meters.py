"""Meters."""
# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta
from abc import abstractmethod

import collections
from functools import lru_cache
import numpy as np
import six

__all__ = ["MetricMeter", "StandardMeter", "AverageMeter",
           "MovingAverageMeter", "MemoryLessMovingAverageMeter"]


# Supported Numpy DTypes: `np.sctypes`
ACCEPTED_INT_NUMBER_FORMATS = (
    int,
    np.uint8,
    np.uint16,
    np.uint32,
    np.uint64,
    np.int,
    np.int8,
    np.int16,
    np.int32,
    np.int64,
)

ACCEPTED_FLOAT_NUMBER_FORMATS = (
    float,
    np.float,
    np.float16,
    np.float32,
    np.float64,
    np.float128,
)

ACCEPTED_STR_NUMBER_FORMATS = (
    str,
    np.str,
)

ACCEPTED_NUMBER_FORMATS = \
    ACCEPTED_INT_NUMBER_FORMATS +  \
    ACCEPTED_FLOAT_NUMBER_FORMATS +  \
    ACCEPTED_STR_NUMBER_FORMATS


@six.add_metaclass(ABCMeta)
class AbstractMeterMixin(object):

    @abstractmethod
    def AUTHORIZED_DTYPES(self):
        pass


@six.add_metaclass(ABCMeta)
class MetricMeter(AbstractMeterMixin):
    """Metric Meter."""

    # Supported Numpy DTypes: `np.sctypes`
    AUTHORIZED_DTYPES = tuple(ACCEPTED_NUMBER_FORMATS)

    @lru_cache(maxsize=128)
    def __init__(self):
        """Init."""
        self._values = np.array([])

    def reset(self):
        """Reset."""
        self._values = np.array([])

    @lru_cache(maxsize=128)
    def __str__(self):
        """str."""
        return self.__class__.__name__

    def get_last(self):
        """Get last element."""
        try:
            return self._values[-1]
        except IndexError:
            raise ValueError("Impossible to get the last value. No value has been recorded yet")

    def record(self, val):
        """Record."""
        if not isinstance(val, MetricMeter.AUTHORIZED_DTYPES):
            raise TypeError("Unsupported datatype received: %s" % str(type(val)))

        if np.isnan(val) or np.isinf(val):
            raise ValueError("invalid value received: %s" % str(val))

        self._values = np.append(self._values, val)

    @abstractmethod
    def read(self):
        """Read."""
        raise NotImplementedError()


class StandardMeter(MetricMeter):
    """Standard Meter."""

    def read(self):
        """Read."""
        return self.get_last()


class AverageMeter(MetricMeter):
    """Average Meter."""

    def read(self):
        """Read."""
        if len(self._values):
            return np.mean(self._values)
        raise ValueError("NaN Result, Impossible to compute the average of an empty list")


class MovingAverageMeter(MetricMeter):
    """Moving Average Meter."""

    def __init__(self, window_size):
        """Init."""
        super(MovingAverageMeter, self).__init__()

        if not isinstance(window_size, int):
            raise ValueError("`window_size` must be an integer")

        if window_size < 1:
            raise ValueError("`window_size` must be superior or equal to 1")

        self._window_size = window_size

    @lru_cache(maxsize=128)
    def __str__(self):
        """Str."""
        return "%s(window_size=%d)" % \
            (super(MovingAverageMeter, self).__str__(), self._window_size)

    def read(self):
        """Read."""
        if len(self._values):
            return np.mean(self._values[-self._window_size:])
        raise ValueError("NaN Result, Impossible to compute \
            the moving average of an empty list")


class MemoryLessMovingAverageMeter(MetricMeter):
    """Memoryless Moving Average."""

    def __init__(self, window_size):
        """Init."""
        super(MemoryLessMovingAverageMeter, self).__init__()

        self._values = collections.deque(maxlen=window_size)

        if not isinstance(window_size, int):
            raise ValueError("`window_size` must be an integer")

        if window_size < 1:
            raise ValueError("`window_size` must be superior or equal to 1")

        self._window_size = window_size

    def reset(self):
        """Reset."""
        self._values = collections.deque(maxlen=self._window_size)

    @lru_cache(maxsize=128)
    def __str__(self):
        """Str."""
        return "%s(window_size=%d)" % \
            (super(MemoryLessMovingAverageMeter, self).__str__(), self._window_size)

    def read(self):
        """Read."""
        if len(self._values):
            return np.mean(self._values)
        raise ValueError("NaN Result, \
            Impossible to compute the moving average of an empty list")
