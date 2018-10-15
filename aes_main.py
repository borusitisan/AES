import numpy as np
import sys


def bunkatsu(i_key):
    b = int(len(i_key)/4)
    
    try:
        i_key_list = [i_key[i: i+b] for i in range(0, len(i_key), b)]
        return(i_key_list)
    except ValueError as e:
        return(e)


#arr = np.arange(9).reshape((3,3))
#arr = arr.T
#print(arr)


def aes_main():
    input_m = input('平文: ')
    input_m = bunkatsu(input_m)
    input_result = []
    for i in range(4):
        input_result += bunkatsu(input_m[i])
    print(input_result)
    arr = np.array(input_result, dtype='int32')#.reshape((4,4))
    #arr = arr.T
    print(arr)

aes_main()