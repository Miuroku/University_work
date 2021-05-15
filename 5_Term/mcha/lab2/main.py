import base_functions as bf
import our_data as odata
import math_functions as mf

import numpy as np

def main():

    # Load data.
    a_array = odata.a_array[0]
    b_array = odata.b_array[0]
    accuracy = odata.accuracy
    debug = odata.debug

    # Setup print options.
    np.set_printoptions(precision=mf.around_value-1, suppress=True, floatmode="fixed")

    # Print source data.
    bf.print_arrays(a_array, b_array)

    # Main logic.
    if not mf.checkSolve(a_array, b_array):
        return
    else:
        # 1-st method (Метод простых итераций).
        x_answers1 = mf.get_solutions_simple_iterations(a_array, b_array, accuracy, debug)
        print("Our Answer 1 : ------------------------------")
        bf.printArray(x_answers1)

        # 2-nd method (Метод Зейделя).
        x_answers2 = mf.get_solutions_Seidel_method(a_array, b_array, accuracy, debug)
        print("Our Answer 2 : ------------------------------")
        bf.printArray(x_answers2)

main()