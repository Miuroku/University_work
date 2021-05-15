import numpy as np
import numpy.linalg as la

import base_functions as bf

# Represents how many values we'll around in values.
around_value = 5

# Checks if there's a possible solve.
def checkSolve(a1_array, b1_array):
    
    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)
    n = len(a_array)

    # Now we crate Расширенную матрицу.
    extended_matrix = np.column_stack((a_array, b_array))     
    
    result = False
    if la.matrix_rank(extended_matrix) != la.matrix_rank(a_array):
        print("@@@ Attention : данное СЛАУ не имеет решений !")
        result = False
    elif la.matrix_rank(a_array) != n:
        print("@@@ Attention : данное СЛАУ имеет бесконечность решений !")
        result = False
    else:
        result = True        
    return result

# 1-st step.
# Привести СЛАУ к нормальному виду.
# Lead the system "A*x=b" to a system like "x = bi + (E-A)*x" 
def get_normal_SLAU_system(a1_array, b1_array,debug=False):

    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array) 
    n = len(b_array)
    whole_amount_of_elements = n * (n+1)
    amount_of_strings = n
    amount_of_rows = n + 1
    # Creatin 2-dimensional array.
    normal_system_array = np.arange(whole_amount_of_elements).reshape(amount_of_strings, amount_of_rows)
    normal_system_array = np.zeros_like(normal_system_array, dtype=float)

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                normal_system_array[i][j] = 0
            else:
                normal_system_array[i][j] = (-1 * a_array[i][j])/a_array[i][i]                
        normal_system_array[i][n] = b_array[i] / a_array[i][i]
    normal_system_array = np.around(normal_system_array, decimals=around_value)
    if debug:
        print("\nOur normal system array : -----------------------------")
        bf.print2DArray(normal_system_array)
    return normal_system_array

# 2-nd step.
# Убедиться что нормальная система удовлетворяет условиям сходимости итерационного процесса.
def check_convergence_conditions(normal_system_array1):
    normal_system_array = np.copy(normal_system_array1)
    n = len(normal_system_array)
    sum_array = np.arange(n)
    sum_array = np.zeros_like(sum_array, dtype=float)    
    for i in range(0, n):
        for j in range(0, n):
            sum_array[i] += abs(normal_system_array[i][j])
    max_value = np.max(sum_array)
    if max_value <= 1:
        return True
    else:
        return False

# Проверяет достигнута ли нужная точность в вычислениях.
# Смотрит разницу между итерациями (x_array_for_calc-последняя и x_array_for_get-предыдущая).    
def check_stop_condition(x_array_for_calc1, x_array_for_get1, accuracy):
    x_array_for_get = np.copy(x_array_for_get1)
    x_array_for_calc = np.copy(x_array_for_calc1)
    n = len(x_array_for_calc)
    difference = np.arange(n)
    difference = np.zeros_like(difference, dtype=float)
    result_count = 0
    result = False
    for i in range(0, n):
        difference[i] = abs(abs(x_array_for_calc[i]) - abs(x_array_for_get[i]))
        if difference[i] <= accuracy:
            result_count += 1
    if result_count == n:
        return True
    else:
        return False

# 3-d step.
# Вычисляем решение методом простых итераций.---------------------------------------------------------------------
def get_solutions_simple_iterations(a1_array, b1_array, accuracy, debug=False):

    # preparation.
    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)
    normal_system_array = get_normal_SLAU_system(a_array, b_array, debug)
    n = len(normal_system_array)
    x_array_for_get = np.arange(n)
    x_array_for_get = np.zeros_like(x_array_for_get, dtype=float)
    x_array_for_calc = np.arange(n)
    x_array_for_calc = np.zeros_like(x_array_for_calc, dtype=float)        
    
    # Подставляет x_array_for_get в normal_system_array.
    # Возвращает массив ответов для записи в x_array_for_calc.
    def get_x_answers(normal_system_array1, x_array_for_get1):
        normal_system_array = np.copy(normal_system_array1)
        x_array_for_get = np.copy(x_array_for_get1)
        n = len(x_array_for_get)
        x_array_for_calc = np.arange(n)
        x_array_for_calc = np.zeros_like(x_array_for_calc, dtype=float)

        for i in range(0, n):         
            for j in range(0, n):
                x_array_for_calc[i] += normal_system_array[i][j] * x_array_for_get[j]
            x_array_for_calc[i] += normal_system_array[i][n] # Adding last element.

            x_array_for_get[i] = x_array_for_calc[i]
        return x_array_for_get

    # main logic.    
    if check_convergence_conditions(normal_system_array):
        iteration_n = 0
        while(True):
            if debug:
                print(f"de : teration № [{iteration_n}]")

            x_array_for_calc = get_x_answers(normal_system_array, x_array_for_get)  
            if check_stop_condition(x_array_for_calc, x_array_for_get, accuracy):                                
                break         
            x_array_for_get = np.copy(x_array_for_calc)

            if iteration_n > 200:
                print("x_calc : ")
                bf.printArray(x_array_for_calc)
                print("x_get : ")
                bf.printArray(x_array_for_get)
                break
            iteration_n += 1
            # Continue iterations.
        #print(f"iterations : {iteration_n}")
        return np.around(x_array_for_calc, decimals=around_value)
    else:
        print("\n SLAU has not answers ! --------------------------")
        return None

# 2-nd method of solvin SLAU. --------------------------------------------------------------------------
# Метод Зейделя решения СЛАУ.
def get_solutions_Seidel_method(a1_array, b1_array, accuracy, debug=False):

    # preparation.
    a_array = np.copy(a1_array)
    b_array = np.copy(b1_array)
    normal_system_array = get_normal_SLAU_system(a_array, b_array, debug)
    n = len(normal_system_array)
    x_array_for_get = np.arange(n)
    x_array_for_get = np.zeros_like(x_array_for_get, dtype=float)
    x_array_for_calc = np.arange(n)
    x_array_for_calc = np.zeros_like(x_array_for_calc, dtype=float)        

    # Подставляет x_array_for_get в normal_system_array.
    # Возвращает массив ответов для записи в x_array_for_calc.
    def get_x_answers(normal_system_array1, x_array_for_get1):
        normal_system_array = np.copy(normal_system_array1)
        x_array_for_get = np.copy(x_array_for_get1)
        n = len(x_array_for_get)
        x_array_for_calc = np.arange(n)
        x_array_for_calc = np.zeros_like(x_array_for_calc, dtype=float)
        for i in range(0, n):
            for j in range(0, n):
                x_array_for_calc[i] += normal_system_array[i][j] * x_array_for_get[j]
            x_array_for_calc[i] += normal_system_array[i][n] # Adding last element.
        return x_array_for_calc            
    
    # main logic.    
    if check_convergence_conditions(normal_system_array):
        iteration_n = 0
        while(True):
            if debug:
                print(f"de : teration № [{iteration_n}]")

            x_array_for_calc = get_x_answers(normal_system_array, x_array_for_get)  
            if check_stop_condition(x_array_for_calc, x_array_for_get, accuracy):                                
                break         
            x_array_for_get = np.copy(x_array_for_calc)

            if iteration_n > 200:
                print("x_calc : ")
                bf.printArray(x_array_for_calc)
                print("x_get : ")
                bf.printArray(x_array_for_get)
                break
            iteration_n += 1
            # Continue iterations.
        #print(f"iterations : {iteration_n}")
        return np.around(x_array_for_calc, decimals=around_value)
    else:
        print("\n SLAU has not answers ! --------------------------")
        return None
