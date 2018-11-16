import numpy as np
import sys
import aes_sub
import Mix

def bunkatsu(i_key):
    b = int(len(i_key)/4)
    
    try:
        i_key_list = [i_key[i: i+b] for i in range(0, len(i_key), b)]
        return(i_key_list)
    except ValueError as e:
        return(e)


def key_arr(i_key):
    input_result = []
    for i in range(4):
        input_result += bunkatsu(i_key[i])
    #print(input_result)
    for i in range(len(input_result)):
        input_result[i] = int(input_result[i],16)
    arr = np.array(input_result).reshape((4,4))
    return(arr)

#def aes_r(i_key,i_sub_key):

def sub_arr(i_key):
    k = format(int(i_key,2),'032x')
    k = bunkatsu(k)
    arr_s = key_arr(k)
    return(arr_s)

def ShiftRows(result_array):
    for i in range(4):
        result_array[i] = np.roll(result_array[i],-i)
    return(result_array)
    

if __name__ == '__main__':
    input_m = input('平文: ')
    input_s = input('秘密鍵: ')
    sub_key = aes_sub.sub_key_gen(input_s)

    #print(sub_key)

    input_m = bunkatsu(input_m)
    
    arr_m = key_arr(input_m)
    arr_m = arr_m.T
    
    print("\n\n 平文")
    print(arr_m)

    arr_s = sub_arr(sub_key[0])   
    print("\n\n サブ鍵")
    print(arr_s)
    add_r = arr_m^arr_s

    print("\n サブ鍵^平文")
    print(add_r)
    result_array = add_r

    #-----以下よりround処理
    for i in range(9):
        result_array = np.vectorize(aes_sub.subword)(result_array)
        result_array = ShiftRows(result_array)
        result_array = Mix.MixColumns(result_array)
        arr_s = sub_arr(sub_key[i+1])
        result_array = result_array^arr_s
    
    result_array = np.vectorize(aes_sub.subword)(result_array)
    result_array = ShiftRows(result_array)
    arr_s = sub_arr(sub_key[10])
    result_array = result_array^arr_s
    print(result_array)
    c = ""
    for i in range(4):
        for j in range(4):
            c += format(result_array[i][j],'08b')

    print(c)
