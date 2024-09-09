"""array indexing"""
import numpy as np
def main():
    """Driven function"""
    array_1d = np.arange(10)
    print (array_1d[1])

    print (array_1d[-1])

    #access 2d array
    array_2d = np.array([[12,2,34,5],
                         [3,4,5,3],
                         [4,5,6,2]])
    print(f'the 0,0 element {array_2d[0,0]}')
    print(f'the 2,-2 element {array_2d[2,-2]}')
    print(f'the full element {array_2d[0]}')

    #slicing
    print(f'a element {array_1d}')
    print(f'slicing element 1:4 {array_1d[1:4]}')
if __name__=='__main__':

    main()

