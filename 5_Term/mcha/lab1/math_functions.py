import numpy as np
import numpy.linalg as la

import base_functions as bf

# represents how many values we'll around in values.
around_value = 5

# Checks if there's a possible solve.
def checkSolve(a1_array, b1_array):
    
    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)

    n = len(a_array)
    # Now we crate Расширенную матрицу.
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
def gauss1(a1_array, b1_array, debug=False):

    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array) 

    n = len(b_array)
    x_array = np.arange(n)
    x_array = np.zeros_like(x_array, dtype=np.float64)
    
    # Here we'll get rectangle matrix.
    # Прямой ход. Состоит из n-1 шага.
    for k in range(0, n-1):                                 # k - номер итерации.      
        if a_array[k][k] == 0:
            print(f'1-st method could not be used, cuz A[{k}][{k}] == 0 on step ')
            return False
        else:
            # Считаем главные элементы k-го шага.             
            for i in range(k+1, n):                 # i - номера уравненений.
                q = a_array[i][k] / a_array[k][k]   

                # from i-equation subtract (k-equation * q).
                for c in range(n): # run on string.           
                    a_array[i][c] -= a_array[k][c] * q                             
                b_array[i] -= b_array[k] * q
            a_array = np.around(a_array, decimals=around_value)
            b_array = np.around(b_array, decimals=around_value)

            if debug:
                print(f"iteration no. {k}")     
                bf.debugOutput(a_array, b_array)           

    # Обратный ход.    
    # Иду от последней строки треугольной матрицы к первой. [n-1,0]. 
    # ik - number of current string.
    for ik in range(n-1, -1, -1):        
        # x_array[k] = (b_array[k] - rightpart)/a_array[k][k].        
        if ik == n-1:
            x_array[ik] = (b_array[n-1]) / a_array[ik][ik]
        else:
            rightpart = 0
            for k in range(ik+1, n):
                rightpart += a_array[ik][k] * x_array[k]
            x_array[ik] = (b_array[ik] - rightpart) / a_array[ik][ik]

        x_array = np.around(x_array, decimals=around_value)

        if debug:
            print(f"x_array[{ik}] = {x_array[ik]}")

    return x_array

def gauss2(a1_array, b1_array, debug=False):

    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)

    n = len(b_array)
    x_array = np.arange(n)
    x_array = np.zeros_like(x_array, dtype=np.float64)

    # Here we'll get rectangle matrix.
    # Прямой ход. Состоит из n-1 шага.
    for k in range(0, n-1):                                 # k - номер итерации.      

        # searching for max element for x[k].
        def get_string_with_max_el_in_row(arr, row):
            if arr[k][row] is not None:    
                max_el = list()
                max_el = [arr[k][row], k]   # [0] - stores the value.
                                            # [1] - stores number of string of this element.
                for i in range(k, n):
                    if arr[i][row] > max_el[0]:
                        max_el[0] = arr[i][row]
                        max_el[1] = i

                return max_el[1]
            else:
                return False
        
        def swap_strings_in_matrix(matrix ,current_str, string_to_change):
            temp = np.copy(matrix[current_str])            
            matrix[current_str] = np.copy(matrix[string_to_change])
            matrix[string_to_change] = np.copy(temp)

        max_str = get_string_with_max_el_in_row(a_array, k)
        if k!=max_str:
            swap_strings_in_matrix(a_array, k, max_str)

        if debug:
            print("------------------")
            print(f"Iteration : {k}")
            print("Matrix after swap : ")
            print(a_array)
            print("------------------")

        if a_array[k][k] == 0:
            print(f'2-nd method could not be used, cuz A[{k}][{k}] == 0 on step ')
            return False
        else:
            # Считаем главные элементы k-го шага.             
            for i in range(k+1, n):                 # i - номера уравненений.
                q = a_array[i][k] / a_array[k][k]   

                # from i-equation subtract (k-equation * q).
                for c in range(n): # run on string.           
                    a_array[i][c] -= a_array[k][c] * q                             
                b_array[i] -= b_array[k] * q
            a_array = np.around(a_array, decimals=around_value)
            b_array = np.around(b_array, decimals=around_value)

            if debug:
                print(f"iteration no. {k}")     
                bf.debugOutput(a_array, b_array)           

    # Обратный ход.    
    # Иду от последней строки треугольной матрицы к первой. [n-1,0]. 
    # ik - number of current string.
    for ik in range(n-1, -1, -1):        
        # x_array[k] = (b_array[k] - rightpart)/a_array[k][k].        
        if ik == n-1:
            x_array[ik] = (b_array[n-1]) / a_array[ik][ik]
        else:
            rightpart = 0
            for k in range(ik+1, n):
                rightpart += a_array[ik][k] * x_array[k]
            x_array[ik] = (b_array[ik] - rightpart) / a_array[ik][ik]

        x_array = np.around(x_array, decimals=around_value)

        if debug:
            print(f"x_array[{ik}] = {x_array[ik]}")

    return x_array    

def gauss3(a1_array, b1_array, debug=False):

    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)

    n = len(b_array)
    x_array = np.arange(n)
    x_array = np.zeros_like(x_array, dtype=np.float64)

    # Here's a main logic.

    return x_array