"""My template"""
import numpy as np

def main():
    """Driven function"""
    print('Main function')

    # Generate a 1d array with values from 0-2
    arr_1d=np.array([0,1,2])
    print(arr_1d,type(arr_1d))

if __name__=='__main__':
    main()
