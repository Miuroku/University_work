import numpy as np

# Our data here.
# "answer" means expceted answer.

# main data ---------------------------------------------------------
# (answer: [0.9396  0.8819 -0.2509 -0.0844  0.7284])
k = 14
a_array = np.array([
    [ 5.13,	    0.81,	3.47,	0.92,	-0.53],
    [  -0.53,	5.13,	0.81,	3.47,	0.92],
    [  3.72,	-0.53,	5.13,	0.81,	3.47],
    [  0.67,	3.72,	-0.53,	5.13,	0.81],
    [  0.81,	0.67,   3.72,   -0.53,	5.13]
])

b_array = np.array(
    [4.2, 4.2, 4.2, 4.2, 4.2]
)

# Some tests. --------------------------------------------------------
a_test = list()
b_test = list()

#   test1 (answer: [1, -4])
a_test.append(
    np.array([
        [1, -1],
        [2, 1]
    ])
)
b_test.append(
    np.array(
        [-5, -7]
    )
)

#   test2 (answer: [3, 5, 4])
a_test.append(
     np.array([
        [3., 2, -5],
        [2, -1, 3],
        [1, 2, -1]
    ])
)
b_test.append(
    np.array(
        [-1., 13, 9]
    )
)

# test3 (answer: False
# [-1, 3, 1])
a_test.append(
    np.array([
        [4, 2, -1],
        [5, 3, -2],
        [3, 2, -3]
    ])
)
b_test.append(
    np.array(
    [1, 2, 0]
    )
)

# test4 (answer: [5, -1, -5])
a_test.append(
    np.array([
        [8, 7 ,3],
        [-7, -4, -4],
        [-6, 5, -4]
    ])
)
b_test.append(
    np.array(
    [18, -11, -15]
    )
)