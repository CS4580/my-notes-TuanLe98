"""create array from ranges"""

import numpy as np

def main():
    """Driven function"""
    #generate 1d array from 0-8

    array = np.arange(9)
    print(array)

    array = np.arange(-4,4)
    print(array)
    #add step
    array = np.arange(-8,8,2)
    print(array)

    #generate array with values from 0 - 5, in step of 0.5
    array = np.arange(0,5,0.1)
    print(array)

if __name__=='__main__':
    main()
