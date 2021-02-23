import numpy as np
import numpy.linalg as la

def debugOutput(a1_array, b1_array):
    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)
    print(" a_array : ")
    print2DArray(a_array)
    print("\n b_array : ")
    printArray(b_array)
    print("\n")

def print2DArray(arr):
    for i in range(len(arr)):
        print("     ", end='')        
        for j in range(len(arr[i])):
            print(str(arr[i][j]) + " ",end='')
        print('')

def printArray(arr):
    print("     ", end='')        
    for i in range(len(arr)):
        print(str(arr[i]) + ' ', end='')

# Checks if there's a possible solve.
def checkSolve(a1_array, b1_array):
    
    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)

    n = len(a_array)
    # Now we're crate Расширенную матрицу.
    extended_matrix = np.column_stack((a_array, b_array))     
    
    if la.matrix_rank(extended_matrix) != la.matrix_rank(a_array):
        print("@@@ Attention : данное СЛАУ не имеет решений !")
        return False
    elif la.matrix_rank(a_array) != n:
        print("@@@ Attention : данное СЛАУ имеет бесконечность решений !")
        return False
    else:
        return True

# returns x_array as answer of ALU.
def gauss1(a1_array, b1_array):

    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array) 

    n = len(b_array)
    x_array = np.arange(n)
    x_array = np.zeros_like(x_array, dtype=np.float64)
    
    # Here we'll get rectangle matrix.
    # Прямой ход. Состоит из n-1 шага.
    for k in range(0, n-1):                                 # k - номер итерации.      
        if a_array[k][k] == 0:
            print(f'1-st method could not be used, cuz A[{k}][{k}] = 0 on step ')
            return False
        else:
            # Считаем главные элементы k-го шага.
            # q считается 

            for i in range(k+1, n):                           # i - номера уравненений.
                q = a_array[i][k] / a_array[k][k]     
                # from i-equation subtract (k-equation * q).
                for c in range(n): # run on string.           
                    a_array[i][c] -= a_array[k][c] * q                             
                b_array[i] -= b_array[k] * q
            a_array = np.around(a_array, decimals=4)
            b_array = np.around(b_array, decimals=4)
            print(f"iteration no. {k}")     
            debugOutput(a_array, b_array)           

    # Обратный ход. <--------------------------------------Error here somwhere .
    # Incorrect calculating of x[0] // Самый первый (на последнем шаге) икс не правильно считается.
    # Иду от последней строки треугольной матрицы к первой. [n-1,0]. 
    # ik - number of current string.
    for ik in range(n-1, -1, -1):        
        # x_array[k] = (b_array[k] - rightpart)/a_array[k][k].        
        if ik == n-1:
            x_array[ik] = (b_array[n-1]) / a_array[ik][ik]
        else:
            rightpart = 0
            for k in range(ik+1, n): # <---------------- Here the cycle sucks .
                rightpart += a_array[ik][k] * x_array[k] # <-----------rightpart wrong value. As a result there'll be a wrong x[0].                                                                           
            x_array[ik] = (b_array[ik] - rightpart) / a_array[ik][ik]

        x_array = np.around(x_array, decimals=4)
        print(f"x_array[{ik}] = {x_array[ik]}")

    return x_array

def gauss2(a1_array, b1_array):

    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)

    n = len(b_array)
    x_array = np.arange(n)
    x_array = np.zeros_like(x_array, dtype=np.float64)

    # Here's a main logic.

    return x_array

def gauss3(a1_array, b1_array):

    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)

    n = len(b_array)
    x_array = np.arange(n)
    x_array = np.zeros_like(x_array, dtype=np.float64)

    # Here's a main logic.

    return x_array

# Data input.
""" aSize = int(input("Enter an A dimension : "))
print("Enter A array:")
a_array = np.arange(aSize * aSize)
a_array = a_array.reshape(aSize, aSize)
a_array = np.zeros_like(a_array,dtype=np.float64)
for i in range(aSize):
    for j in range(aSize):
        a_array[i][j] = float(input(f"A[{i}][{j}] = "))

print("Enter B array : ")
b_array = np.arange(aSize)
b_array = np.zeros_like(b_array, dtype=np.float64)
for i in range(aSize):
    b_array[i] = float(input(f"B[{i}] = ")) """

# Our data here.
k = 14
a_array = np.array(
    [[ 5.13,	0.81,	3.47,	0.92,	-0.53],
    [  -0.53,	5.13,	0.81,	3.47,	0.92],
    [  3.72,	-0.53,	5.13,	0.81,	3.47],
    [  0.67,	3.72,	-0.53,	5.13,	0.81],
    [  0.81,	0.67,   3.72,   -0.53,	5.13]]
)

b_array = np.array(
    [  4.2, 4.2, 4.2, 4.2, 4.2]
)

# Some tests.
#    test1 (answer: [1, -4])
a_test1 = np.array([
    [1, -1],
    [2, 1]
]) 
b_test1 = np.array([
    -5, -7
])

# test2 (answer: [3, 5, 4])
a_test2 = np.array([
        [3., 2, -5],
        [2, -1, 3],
        [1, 2, -1]
])
b_test2 = np.array(
    [-1., 13, 9]
)

# test3 (answer: [])
a_test3 = np.array([
    []
])
b_test3 = ([
    
])

print("our a_array : ")
print2DArray(a_test)
print("our b_array : ")
printArray(b_test)
print()

if checkSolve(a_test, b_test) == False:
    print("")
else:    
    # 1-st gauss.
    gaussAnswer = gauss1(a_test, b_test)
    print(f"Our Answer 1: -------------------\n{gaussAnswer}")

    # 2-nd gauss.

    # 3-d gauss
