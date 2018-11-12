import numpy as np



def gl8(a,b):
    r = 0
    p = '11b'  # x^8 + x^4 + x^3 + x + 1
    px = int(p,16)
    
    #排他的論理和を取る
    for i in range(8):
        if ((b & 1) != 0):
            r ^= a
        a <<= 1
        b >>= 1
        
    #溢れてる部分
    s = r >> 8 #溢れてるbit取り出す
    sz = len(format(s,'0b'))
    for i in range(sz):
        if ((s & 1) == 1):
            r ^= px
        px <<= 1
        s >>= 1
    return r

def MixColumns(b):
    a = [0x02,0x03,0x01,0x01,0x01,0x02,0x03,0x01,0x01,0x01,0x02,0x03,0x03,0x01,0x01,0x02]

    A = [a[4*y:4*(y+1)] for y in range(len(a)//4)]
    
    C = [0 for i in range(4)]
    c = [[],[],[],[]]
    #行列計算
    for k in range(4):
        B = b[k]
        for i in range(4):
            for j in range(4):
                C[i] ^= gl8(A[i][j],B[j])
        #１６進数のベクトルに変換
            c[i].append(C[i])
    c = np.array(c)
    return(c)