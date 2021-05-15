import numpy as np

def get_debug_info():
    print("Use debug mode(y/n) ? : ", end='')
    debug = list()    
    if (input() == "y"):        
        for i in range(0,3):
            print(f"Debug gauss{i+1}(y/n) ? : ", end='')            
            usr_input2 = input()
            if usr_input2 == 'y':
                debug.append(True)
            else:
                debug.append(False)        
    else:
        for i in range(0, 3):
            debug.append(False)
    return debug

def print2DArray(arr):
    for i in range(len(arr)):
        print("     ", end='')        
        for j in range(len(arr[i])):
            print(str(arr[i][j]) + " ",end='')
        print('\n')

def printArray(arr):
    print("     ", end='')        
    for i in range(len(arr)):
        print(str(arr[i]) + ' ', end='')
    print('\n')

def print_arrays(a_array, b_array):    
    print("our a_array : ")
    print2DArray(a_array)
    print("\n our b_array : ")
    printArray(b_array)
    print('\n')
