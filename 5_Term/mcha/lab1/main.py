import math_functions as mf
import our_data as odata
import base_functions as bf
import numpy as np

def main():

    # user input.
    debug = bf.get_debug_info()

    # load data.
    a_array = odata.a_array[0]
    b_array = odata.b_array[0]

    # print source data.
    print("our a_array : ")
    bf.print2DArray(a_array)
    print("our b_array : ")
    bf.printArray(b_array)
    print()

    # Setup printoptions.
    np.set_printoptions(precision=mf.around_value, suppress=True, floatmode="fixed")    

    # main logic.
    if not  mf.checkSolve(a_array, b_array):
        print("")
    else:    
        # 1-st gauss.
        gaussAnswer = mf.gauss1(a_array, b_array, debug[0])
        print(f"Our Answer 1: -------------------\n{gaussAnswer}")

        # 2-nd gauss.        
        gaussAnswer2 = mf.gauss2(a_array, b_array, debug[1])
        print(f"Our Answer 2: -------------------\n{gaussAnswer2}")

        # 3-d gauss
        #gaussAnswer3 = mf.gauss3(a_array, b_array, debug[2])
        #print(f"Our Answer 3: -------------------\n{gaussAnswer3}")

main()
