import numpy as np
import numpy.linalg as la

import base_functions as bf

# represents how many values we'll around in values.
around_value = 4

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

""" # Here we'll get rectangle matrix.
def stright_run(a_array, b_array, n, debug=False):    
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
                bf.debugOutput(a_array, b_array) """

def swap_strings_in_matrix(a_matrix, b_matrix, current_str, string_to_change):
    # Swap in a_matrix.
    temp1 = np.copy(a_matrix[current_str])            
    a_matrix[current_str] = np.copy(a_matrix[string_to_change])
    a_matrix[string_to_change] = np.copy(temp1)
    # Swap in b_matrix.
    temp2 = np.copy(b_matrix[current_str])
    b_matrix[current_str] = np.copy(b_matrix[string_to_change])
    b_matrix[string_to_change] = np.copy(temp2)

def swap_rows_in_matrix(a_matrix, current_row, row_to_swap):
    n = len(a_matrix)
    temp1 = list() # stores current row.
    for i in range(0, n):
        temp1.append(np.copy(a_matrix[i][current_row]))    
        a_matrix[i][current_row] = np.copy(a_matrix[i][row_to_swap])
        a_matrix[i][row_to_swap] = np.copy(temp1[i])

# returns x_array as answer of ALU.
def gauss1(a1_array, b1_array, debug=False):

    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array) 

    n = len(b_array)
    x_array = np.arange(n)
    x_array = np.zeros_like(x_array, dtype=np.float64)

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

# ----------------------------------------------------------------------------------------------------------------------
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
                for i in range(k+1, n):
                    if abs(arr[i][row]) > max_el[0]:
                        max_el[0] = arr[i][row]
                        max_el[1] = i

                return max_el[1]
            else:
                return False                

        max_str = get_string_with_max_el_in_row(a_array, k)
        if k!=max_str:
            swap_strings_in_matrix(a_array, b_array, k, max_str)

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

# ----------------------------------------------------------------------------------------------------------------------
def gauss3(a1_array, b1_array, debug=False):

    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)

    n = len(b_array)
    x_array = np.arange(n)
    x_array = np.zeros_like(x_array, dtype=np.float64)    

    right_position_x = list() # for editing an answer for right sequence.    
    right_position_rows = list() # list thst stores right positions of rows.
    for i in range(0, n):
        right_position_rows.append(i)

    # Here we'll get rectangle matrix.
    # Прямой ход. Состоит из n-1 шага.
    for k in range(0, n-1):                                 # k - номер итерации.          

        # returns an array with 3 elements, or True or False.
        # k - here the number of string from wich we'll start searchin.
        def get_string_and_row_with_max_el(a_matrix, k, n):             
            if a_matrix[k][k] is not None:

                max_element = [a_matrix[k][k], k, k] # [0] - element, [1] - its string, [2] - its row.
                for i in range(k, n):
                    for j in range(k, n):
                        if a_matrix[i][j] > max_element[0]:
                            max_element[0] = a_matrix[i][j]
                            max_element[1] = i
                            max_element[2] = j                
                else:
                    return max_element
            else:
                return None        

        max_element = get_string_and_row_with_max_el(a_array, k, n)
        if k != max_element[1]:
            swap_strings_in_matrix(a_array, b_array, k, max_element[1])
        if max_element[2] != k:
            swap_rows_in_matrix(a_array, k, max_element[2])

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