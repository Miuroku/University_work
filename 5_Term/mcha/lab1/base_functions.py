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
        return debug
    else:
        return None

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