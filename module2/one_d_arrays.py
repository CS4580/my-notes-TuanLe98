"""1D array
"""
import numpy as np

"""My template"""
def main():
    """Driven function"""
    #create an array

    array = np.array([1,3,1,-2])
    print(array, type(array))
    numbers=[1,3,4,5,-1,4]
    print(numbers,type(numbers))

    #Convert list to array
    new_array = np.array(numbers)
    print(new_array,type(new_array))

    matrix=np.array([[1,3,4,5,2,4],[4,562,4,5,2,5]])
    print(matrix)

    print('3 array')
    matrix_3d=np.array([[[1,3,4,5,2,4],[4,562,4,5,2,5]]
                        ,[[1,3,4,2,5,4],[1,2,4,5,2,5]]
                        ])
    print(matrix_3d,type(matrix_3d))


    #Using the dtype optional argument to explicitly 
    #call the data type of the array
    
    new_arrays=np.array(numbers,dtype=np.short)
    print(new_arrays,new_arrays.dtype)

    pos_number=[1,3,4,5,1,4]
    new_arrays=np.array(pos_number,dtype=np.ushort)
    print(new_arrays,new_arrays.dtype)
    
    #float
    pos_number=[1,3,4,5,1,4]
    new_arrays=np.array(pos_number,dtype=np.float32)
    print(new_arrays,new_arrays.dtype)

    

if __name__=='__main__':
    main()
