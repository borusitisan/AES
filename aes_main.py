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
    
def key_main(m,s):
    input_m = bunkatsu(m)
    
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
    for i in range(10):
        j = i+1
        print("----------------------------------------")
        print("\nラウンド%d回目" % j)
        result_array = np.vectorize(aes_sub.subword)(result_array)
        print("\nSubbyte処理")
        print(result_array)

        result_array = ShiftRows(result_array)
        print("\nShift処理")
        print(result_array)

        result_array = Mix.MixColumns(result_array)
        print("\nMixColumns処理")
        print(result_array)

        arr_s = sub_arr(sub_key[i])
        result_array = result_array^arr_s
        print("\nラウンド%d結果" % j)
        print(result_array)
    
    result_array = np.vectorize(aes_sub.subword)(result_array)
    result_array = ShiftRows(result_array)
    arr_s = sub_arr(sub_key[10])
    result_array = result_array^arr_s
    print("\n\n最終結果")
    print(result_array)
    
    c = ""
    for i in range(4):
        for j in range(4):
            c += format(result_array[i][j],'08b')
    
    return(c)

if __name__ == '__main__':
    input_m = input('平文: ')
    input_s = input('秘密鍵: ')
    input_m = ''.join(input_m.split())
    print(input_m)
    sub_key = aes_sub.sub_key_gen(input_s)

    result_key = []

    #if len(input_m) % 32 is 0:
    j = int(len(input_m)/32)

    for k in range(j):
        print(input_m[j * k:32 * (k+1)])
        result_key += key_main(input_m[j * k:32 * (k+1)],sub_key)
            

    print(result_key)
