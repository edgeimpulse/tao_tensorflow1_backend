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

"""Modules related to TensorFlow training operation."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from nvidia_tao_tf1.core.training.features import (
    enable_deterministic_training,
    enable_mixed_precision,
)
from nvidia_tao_tf1.core.training.train_op_generator import TrainOpGenerator

__all__ = (
    "enable_deterministic_training",
    "enable_mixed_precision",
    "TrainOpGenerator",
)