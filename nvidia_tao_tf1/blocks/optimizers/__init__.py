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
"""Modulus application building block: Opimizers."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from nvidia_tao_tf1.blocks.optimizers.adadelta_optimizer import AdadeltaOptimizer
from nvidia_tao_tf1.blocks.optimizers.adam_optimizer import AdamOptimizer
from nvidia_tao_tf1.blocks.optimizers.gradient_descent_optimizer import (
    GradientDescentOptimizer,
)
from nvidia_tao_tf1.blocks.optimizers.masking_optimizer import MaskingOptimizer
from nvidia_tao_tf1.blocks.optimizers.momentum_optimizer import MomentumOptimizer
from nvidia_tao_tf1.blocks.optimizers.optimizer import Optimizer
from nvidia_tao_tf1.blocks.optimizers.rms_prop_optimizer import RMSPropOptimizer

__all__ = (
    "AdadeltaOptimizer",
    "AdamOptimizer",
    "GradientDescentOptimizer",
    "MaskingOptimizer",
    "MomentumOptimizer",
    "Optimizer",
    "RMSPropOptimizer",
)
