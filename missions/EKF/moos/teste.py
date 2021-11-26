import numpy as np
def calc_C():
        C = np.zeros((11,6))
        C[0:3,0]=1
        C[3,1] = 1
        C[4,2] = 1
        C[5:7,3]=1
        C[7:9,4]=1
        C[9: ,5]=1
        return C
C = calc_C()
print(C)