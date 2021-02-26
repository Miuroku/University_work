import base_functions as bf
import our_data as odata
import math_functions as mf

import numpy as np

def main():

    # Load data.
    a_array = odata.a_array[0]
    b_array = odata.b_array[0]
    accuracy = odata.accuracy

    # Setup print options.
    np.set_printoptions(precision=mf.around_value-1, suppress=True, floatmode="fixed")

    # Print source data.
    bf.print_arrays(a_array, b_array)

    # Main logic.
    if not mf.checkSolve(a_array, b_array):
        return
    else:
        # 1-st method (Метод простых итераций).
        x_answers = mf.get_solutions_simple_iterations(a_array, b_array, accuracy)
        print("Our Answer : ------------------------------")
        bf.printArray(x_answers)

        # 2-nd method (Метод Зейделя).
        

main()