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

"""Processors for transforming and augmenting data."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from nvidia_tao_tf1.blocks.multi_source_loader.data_format import (
    CHANNELS_FIRST,
    CHANNELS_LAST,
    DataFormat,
    TensorAxis4D,
    TensorAxis5D,
)
from nvidia_tao_tf1.blocks.multi_source_loader.data_loader import DataLoader
from nvidia_tao_tf1.blocks.multi_source_loader.frame_shape import FrameShape
from nvidia_tao_tf1.blocks.multi_source_loader.types import (
    empty_polygon_label,
    Example,
    FEATURE_CAMERA,
    LABEL_MAP,
    PolygonLabel,
)

__all__ = (
    "CHANNELS_FIRST",
    "CHANNELS_LAST",
    "DataFormat",
    "DataLoader",
    "empty_polygon_label",
    "Example",
    "FEATURE_CAMERA",
    "FrameShape",
    "LABEL_MAP",
    "PolygonLabel",
    "TensorAxis4D",
    "TensorAxis5D",
)
