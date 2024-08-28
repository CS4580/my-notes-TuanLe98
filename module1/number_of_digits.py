"""number of  of digits"""

import math

def factorial_length(number):
    """count the number of digits in a factorial"""

    length = math.factorial(number)
    length = str(length)
    return len(length)

def main():
    print ('hello')
    number= 5
    digits = factorial_length(number)
    print(f'you have {digits} in factorial ({number})')

if __name__=="__main__":
    main()

   