from math_functions import around_value
import numpy as np

# Our data here.
# "answer" means expected answer.

# [0] - index always stores main data.
a_array = list()
b_array = list()
accuracy = 0.0001
debug = False   

# main data --------------------------------------------------------------
# (answer: [0.769	-1.383	-3.298	-0.0603	-0.0325])
c_array = list()
d_array = list()
k = 14
c_array.append(
    np.array([
        [0.01,  0,      -0.02,  0,    0     ],
        [0.01,  0.01,   -0.02,  0,    0     ],
        [0,     0.01,   0.01,   0,     -0.02],
        [0,     0,      0.01,   0.01,  0    ],
        [0,     0,      0,      0.01,  0.01 ]
    ])
)
d_array.append(
    np.array([
        [1.33,  0.21,   0.17,   0.12,   -0.13 ],
        [-0.13, -1.33,  0.11,   0.17,   0.12  ],
        [0.12,  -0.13,  -1.33,  0.11,   0.17  ],
        [0.17,  0.12,   -0.13,  -1.33,  0.11  ],
        [0.11,  0.67,   0.12,   -0.13,  -1.33 ]
    ])
)
b_array.append(
    np.array(
        [1.2, 2.2, 4.0, 0.0, -1.2]
    )
)
# a_array = k * c_array + d_array.
a_array.append( k * c_array[0] + d_array[0] )
a_array[0] = np.around(a_array[0], decimals=around_value) 
# Just an expected value of a_array after calcualtions above.
""" np.array([
    [1.47,	0.21,	-0.11,	0.12,	-0.13], 
    [0.01,	-1.19,	-0.17,	0.17,	0.12],
    [0.12,	0.01,	-1.19,	0.11,	-0.11],
    [0.17,	0.12,	0.01,	-1.19,	0.11],
    [0.11,	0.67,	0.12,	0.01,	-1.19]
]) """

# Data for testin. ----------------------------------------------------------------------------
#   test1 (answer: [8.0000, 0.9999, 7.9999, 1.0000])
a_array.append(
    np.array([
        [3.0,     0,    0,   3],
        [0,     11,  1,   2],
        [1,     0,    5,   0],
        [-1,    2,    7,  11]
    ])
)
b_array.append(
    np.array(
        [21.0,    21,     48,     61]
    )
)

#   test2 (answer: [1.64,   -4.89,  1.64])
a_array.append(
    np.array([
        [10.0, 2, -1],
        [-2, -6, -1],
        [1, -3, 12]
    ])
)
b_array.append(
    np.array(
        [5.0, 24.42, 36.0]
    )
)

#   test3 (answer: [0.4, -0.0946, -0.54]) *** not really good test.
a_array.append(
    np.array([
        [3.6, 1.8, -4.7],
        [2.7, -3.6, 1.9],
        [1.5, 4.5, 3.3]
    ])
)
b_array.append(
    np.array(
        [3.8, 0.4, -1.6]
    )
)