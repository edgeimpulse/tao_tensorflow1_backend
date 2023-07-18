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
"""test helper layer."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from keras.layers import Input
from keras.models import Model
import numpy as np

from nvidia_tao_tf1.cv.yolo_v3.layers.export_layers import BoxLayer, ClsLayer


def test_box_layer():
    x = Input(shape=(10, 18))
    y = BoxLayer()(x)
    model = Model(inputs=x, outputs=y)

    encoded_val = '''np.array([[[ 0.31853288,  0.43654425, -0.04237543, -0.52155923,
                                  0.19736763,  0.08178696,  0.15963268,  0.21230579,
                                  0.20757881, -0.52988177,  0.61076724,  0.12471242,
                                 -0.11150562, -0.06977893, -0.43470218,  0.30996265,
                                  0.37252738,  0.51286116],
                                [ 0.14094187, -0.27182029,  0.18511877, -0.07511589,
                                 -0.07891718,  0.31212412,  0.16098262,  0.19797382,
                                 -0.43625911, -0.62739477,  0.40618992, -0.58509829,
                                  0.46435664,  0.30513983, -0.1154359 , -0.12232048,
                                 -0.35335439, -0.15514401],
                                [-0.4435788 ,  0.17339223,  0.49024131, -0.41337404,
                                 -0.03950875,  0.09569453,  0.11478826,  0.30234933,
                                 -0.07100774,  0.18649774, -0.03488029,  0.0932529 ,
                                 -0.1600546 , -0.08485666, -0.17145977, -0.36596332,
                                  0.21935859, -0.4561344 ],
                                [ 0.26568643,  0.05245326,  0.43467644, -0.04510512,
                                 -0.4880742 ,  0.13686102, -0.04520775,  0.27334498,
                                 -0.10976604,  0.30152139,  0.42257043,  0.65097083,
                                  0.65856431,  0.30920291, -0.10761981, -0.17804009,
                                  0.02396226, -0.42966381],
                                [ 0.0754364 , -0.43377111,  0.34619459,  0.20489158,
                                  0.44529587,  0.26571338, -0.47253105, -0.43720297,
                                 -0.13591284, -0.52512667,  0.14932724,  0.36775451,
                                 -0.16522197,  0.45886091, -0.12075849, -0.53379658,
                                 -0.41089267,  0.10501947],
                                [ 0.07269398, -0.25815662, -0.15854433, -0.1325061 ,
                                  0.2008364 , -0.12098036, -0.07968031, -0.16857242,
                                  0.00185386,  0.15585919,  0.0737384 , -0.00930042,
                                  0.11230997,  0.42464644,  0.12645006, -0.80636047,
                                  0.26897187, -0.06773979],
                                [-0.74415635,  0.08761501,  0.58244596, -0.43155333,
                                  0.53962684, -0.07503792, -0.18369426, -0.13517962,
                                 -0.13551022, -0.36913204,  0.03110164,  0.61730996,
                                 -0.12686711, -0.30124402, -0.30547717, -0.22220013,
                                  0.29756512, -0.184686  ],
                                [-0.33638997, -0.07932845, -0.55568364,  0.05962443,
                                  0.64843452,  0.79589313, -0.01803575, -0.20797992,
                                 -0.351547  , -0.50232191, -0.40235586, -0.02057243,
                                 -0.89491065, -0.1765394 , -0.17597896,  0.09962589,
                                 -0.37461121, -0.42049561],
                                [ 0.29857787, -0.14727424,  0.01760341,  0.30076768,
                                  0.13391777, -0.2511477 , -0.5511517 , -0.32004931,
                                 -0.1215235 ,  0.20353435, -0.07441485,  0.10444563,
                                 -0.0649847 ,  0.02956609,  0.39488643,  0.13267954,
                                  0.38612237,  0.02984453],
                                [ 0.56022737, -0.10532191, -0.125717  ,  0.09212133,
                                  0.00289174,  0.27512265,  0.19977999,  0.32625175,
                                  0.11545165,  0.2473364 ,  0.48727129,  0.22696133,
                                 -0.29905336,  0.01784677,  0.44397951,  0.12411839,
                                  0.24461395,  0.15557853]]])'''

    encoded_val = eval(encoded_val)
    expected = '''np.array([[[[  0.6352768 ,  0.4511522 ,  0.3282481 ,  0.399001  ]],
                              [[-0.08030513,  0.03847902, -0.1204156 ,  0.15814908]],
                              [[ 0.47748056, -0.6927845 , -0.02064419, -0.23614697]],
                              [[ 0.16066766, -0.16758   ,  0.09968942,  0.22190909]],
                              [[-0.3900978 ,  0.09533787, -0.26890844,  0.39753762]],
                              [[-0.23613298,  0.24853289, -0.39098775,  0.08969437]],
                              [[ 0.20180187, -0.7533715 , -0.09654567, -0.24473873]],
                              [[ 0.2593441 ,  0.18039277,  0.29542428, -0.2105855 ]],
                              [[-0.43725252,  0.33974332, -0.06859337,  0.35533237]],
                              [[-0.00450347,  0.6323684 ,  0.11346802,  0.49126607]]]])'''

    expected = eval(expected)
    pred = model.predict(encoded_val)
    assert np.max(np.abs(pred - expected)) < 1e-3


def test_cls_layer():
    x = Input(shape=(10, 18))
    y = ClsLayer()(x)
    model = Model(inputs=x, outputs=y)

    encoded_val = '''np.array([[[ 0.31853288,  0.43654425, -0.04237543, -0.52155923,
                                  0.19736763,  0.08178696,  0.15963268,  0.21230579,
                                  0.20757881, -0.52988177,  0.61076724,  0.12471242,
                                 -0.11150562, -0.06977893, -0.43470218,  0.30996265,
                                  0.37252738,  0.51286116],
                                [ 0.14094187, -0.27182029,  0.18511877, -0.07511589,
                                 -0.07891718,  0.31212412,  0.16098262,  0.19797382,
                                 -0.43625911, -0.62739477,  0.40618992, -0.58509829,
                                  0.46435664,  0.30513983, -0.1154359 , -0.12232048,
                                 -0.35335439, -0.15514401],
                                [-0.4435788 ,  0.17339223,  0.49024131, -0.41337404,
                                 -0.03950875,  0.09569453,  0.11478826,  0.30234933,
                                 -0.07100774,  0.18649774, -0.03488029,  0.0932529 ,
                                 -0.1600546 , -0.08485666, -0.17145977, -0.36596332,
                                  0.21935859, -0.4561344 ],
                                [ 0.26568643,  0.05245326,  0.43467644, -0.04510512,
                                 -0.4880742 ,  0.13686102, -0.04520775,  0.27334498,
                                 -0.10976604,  0.30152139,  0.42257043,  0.65097083,
                                  0.65856431,  0.30920291, -0.10761981, -0.17804009,
                                  0.02396226, -0.42966381],
                                [ 0.0754364 , -0.43377111,  0.34619459,  0.20489158,
                                  0.44529587,  0.26571338, -0.47253105, -0.43720297,
                                 -0.13591284, -0.52512667,  0.14932724,  0.36775451,
                                 -0.16522197,  0.45886091, -0.12075849, -0.53379658,
                                 -0.41089267,  0.10501947],
                                [ 0.07269398, -0.25815662, -0.15854433, -0.1325061 ,
                                  0.2008364 , -0.12098036, -0.07968031, -0.16857242,
                                  0.00185386,  0.15585919,  0.0737384 , -0.00930042,
                                  0.11230997,  0.42464644,  0.12645006, -0.80636047,
                                  0.26897187, -0.06773979],
                                [-0.74415635,  0.08761501,  0.58244596, -0.43155333,
                                  0.53962684, -0.07503792, -0.18369426, -0.13517962,
                                 -0.13551022, -0.36913204,  0.03110164,  0.61730996,
                                 -0.12686711, -0.30124402, -0.30547717, -0.22220013,
                                  0.29756512, -0.184686  ],
                                [-0.33638997, -0.07932845, -0.55568364,  0.05962443,
                                  0.64843452,  0.79589313, -0.01803575, -0.20797992,
                                 -0.351547  , -0.50232191, -0.40235586, -0.02057243,
                                 -0.89491065, -0.1765394 , -0.17597896,  0.09962589,
                                 -0.37461121, -0.42049561],
                                [ 0.29857787, -0.14727424,  0.01760341,  0.30076768,
                                  0.13391777, -0.2511477 , -0.5511517 , -0.32004931,
                                 -0.1215235 ,  0.20353435, -0.07441485,  0.10444563,
                                 -0.0649847 ,  0.02956609,  0.39488643,  0.13267954,
                                  0.38612237,  0.02984453],
                                [ 0.56022737, -0.10532191, -0.125717  ,  0.09212133,
                                  0.00289174,  0.27512265,  0.19977999,  0.32625175,
                                  0.11545165,  0.2473364 ,  0.48727129,  0.22696133,
                                 -0.29905336,  0.01784677,  0.44397951,  0.12411839,
                                  0.24461395,  0.15557853]]])'''
    encoded_val = eval(encoded_val)
    expected = '''np.array([[[ 0.3442388 , 0.30600947, 0.31275627, 0.25471213, 0.37388256,
                               0.3837296 , 0.4053815 ],
                              [0.21471846, 0.3685351 , 0.34551924, 0.2827858 , 0.28175643,
                               0.2476133 , 0.2768552 ],
                              [0.25708547, 0.22602433, 0.23522456, 0.22463313, 0.20118774,
                               0.27247456, 0.19056945],
                              [0.39703092, 0.3980631 , 0.34837776, 0.2858115 , 0.27523145,
                               0.3056678 , 0.23813948],
                              [0.3174772 , 0.24648973, 0.32920435, 0.2524312 , 0.19858934,
                               0.21420556, 0.28272408],
                              [0.25800774, 0.27375397, 0.3134377 , 0.27558005, 0.16002087,
                               0.29386497, 0.25043696],
                              [0.32985377, 0.23780398, 0.21593297, 0.21540776, 0.22579597,
                               0.2913851 , 0.23050907],
                              [0.19831222, 0.11625554, 0.18273215, 0.18278787, 0.21034616,
                               0.16327505, 0.15885517],
                              [0.25326118, 0.2328842 , 0.24426049, 0.28761938, 0.2566472 ,
                               0.28660387, 0.244294  ],
                              [0.34473014, 0.26376066, 0.31249547, 0.37738135, 0.32892877,
                               0.34742627, 0.33377704]]])'''

    expected = eval(expected).reshape(1, 10, 7, 1)
    pred = model.predict(encoded_val)
    assert np.max(np.abs(pred - expected)) < 1e-5
