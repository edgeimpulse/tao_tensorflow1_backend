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

"""Collection of callbacks."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from keras.callbacks import Callback

from nvidia_tao_tf1.cv.retinanet.utils.model_io import save_model


class KerasModelSaver(Callback):
    """Save the encrypted model after every epoch.

    Attributes:
        filepath: formated string for saving models
        ENC_KEY: API key to encrypt the model.
    """

    def __init__(self, filepath, key, save_model, verbose=1):
        """Initialization with encryption key."""
        self.filepath = filepath
        self._ENC_KEY = key
        self.verbose = verbose
        self.save_model = save_model

    def on_epoch_end(self, epoch, logs=None):
        """Called at the end of an epoch."""
        self.save_model.set_weights(self.model.get_weights())
        fname = self.filepath.format(epoch=epoch + 1)
        fname = save_model(self.save_model, fname, str.encode(self._ENC_KEY), '.hdf5')
        if self.verbose > 0:
            print('\nEpoch %05d: saving model to %s' % (epoch + 1, fname))
