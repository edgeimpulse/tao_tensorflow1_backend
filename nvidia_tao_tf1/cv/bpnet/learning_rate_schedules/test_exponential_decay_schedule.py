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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import pytest
import tensorflow as tf
from nvidia_tao_tf1.cv.bpnet.learning_rate_schedules.exponential_decay_schedule import (
    BpNetExponentialDecayLRSchedule,
)

STEPS_PER_EPOCH = 25


@pytest.mark.parametrize(
    "learning_rate, decay_epochs, decay_rate, staircase, min_learning_rate,"
    "expected_steps, expected_values",
    [
        (
            1.0,
            1,
            0.1,
            False,
            0.0,
            [26, 51, 71, 101],
            [0.1, 0.01, 0.0015848934, 0.0001],
        ),
        (
            1.0,
            1,
            0.1,
            False,
            0.0005,
            [26, 51, 71, 101],
            [0.1, 0.01, 0.0015848934, 0.0005],
        ),
        (1.0, 1, 0.1, True, 0.0, [26, 51, 71, 101], [0.1, 0.01, 0.01, 0.0001]),
        (1.0, 1, 0.1, True, 0.0005, [26, 51, 71, 101], [0.1, 0.01, 0.01, 0.0005]),
    ],
)
def test_exponential_decay_schedule(
    learning_rate,
    decay_epochs,
    decay_rate,
    staircase,
    min_learning_rate,
    expected_steps,
    expected_values,
):
    """
    Test ExponentialDecayLearningRateSchedule class.

    Args:
        learning_rate (float): initial learning rate to be used.
        decay_epochs (int): number of epochs before next decay.
        decay_rate (float): the decay rate.
        staircase (bool): whether to apply decay in a discrete staircase as opposed to
            continuous fashion.
        min_learning_rate (float): the minimum learning rate to be used.
        expected_steps (list): the steps over which the lr decay is evaluated.
        expected_values (list): the expected learning rates at the expected_steps.
    """
    global_step_tensor = tf.compat.v1.train.get_or_create_global_step()
    increment_global_step_op = tf.compat.v1.assign(
        global_step_tensor, global_step_tensor + 1
    )
    initializer = tf.compat.v1.global_variables_initializer()
    schedule = BpNetExponentialDecayLRSchedule(
        decay_epochs,
        learning_rate=learning_rate,
        decay_rate=decay_rate,
        staircase=staircase,
        min_learning_rate=min_learning_rate
    )

    # update the decay_steps
    schedule.update_decay_steps(STEPS_PER_EPOCH)

    lr_tensor = schedule.get_tensor()
    result_values = []
    sess = tf.compat.v1.Session()
    with sess.as_default():
        sess.run(initializer)
        for _ in range(110):
            global_step, lr = sess.run([increment_global_step_op, lr_tensor])
            if global_step in expected_steps:
                result_values.append(lr)
        assert np.allclose(result_values, expected_values)
