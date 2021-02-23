import math_functions as mf
import our_data as odata
import base_functions as bf

def main():

    # load data.
    a_array = odata.a_array[1]
    b_array = odata.b_array[1]

    # print source data.
    print("our a_array : ")
    bf.print2DArray(a_array)
    print("our b_array : ")
    bf.printArray(b_array)
    print()

    # main logic.
    if not  mf.checkSolve(a_array, b_array):
        print("")
    else:    
        # 1-st gauss.
        gaussAnswer = mf.gauss1(a_array, b_array)
        print(f"Our Answer 1: -------------------\n{gaussAnswer}")

        # 2-nd gauss.        
        gaussAnswer2 = mf.gauss2(a_array, b_array)
        print(f"Our Answer 2: -------------------\n{gaussAnswer}")

        # 3-d gauss

main()
