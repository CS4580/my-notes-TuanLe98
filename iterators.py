"""My template"""

import numpy as np
def main():
    """Driven function"""
    interable = ['Freshman', 'Sophomore','Junior','Senior']

    iterator = iter(interable)
    print(next(iterator))
    #TODO: add a function with a try: catch: to test the iterator

if __name__=='__main__':
    main()
