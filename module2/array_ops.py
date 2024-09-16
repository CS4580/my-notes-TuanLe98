"""My template"""

import numpy as np
import pandas as pd

def main():
    """Driven function"""
    number_list =[2,4,6,8,10]
    print(f'Before list{number_list}')
    for item in range(len(number_list)):
        number_list[item]=number_list[item]+3
        
    print(f'After list{number_list}')

    number_arr = np.array(number_list)
    print(f'before array {number_arr}')
    number_arr+=3
    print(f'After array {number_arr}')

if __name__=='__main__':
    main()
