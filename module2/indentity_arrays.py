"""My template"""

import numpy as np
def main():
    """Driven function"""
    #create a 2d 3*3 identity matrix
    identity_3x3=np.eye(3,3)
    print(identity_3x3)

    diagonal_2d=np.diag([1,2,3,4,5,5])
    print(diagonal_2d)

    arr_5x3_zeros=np.zeros((4,5), dtype=np.uint)
    print(arr_5x3_zeros)

    arr_5x3_one=np.ones((5,3),dtype=np.uint)
    print(arr_5x3_one)

    arr_5x3_pi=np.full((5,3),np.pi)
    print(arr_5x3_pi)

    arr_5x3_radom=np.random.random((5,3))
    print(arr_5x3_radom)

if __name__=='__main__':
    main()
