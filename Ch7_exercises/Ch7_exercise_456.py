# (done) 1. Modify the program below to work from the command line by using argparse. 
    # The program should take the number x as a required argument.
# (done) 2. Upgrade the program so that:
    # it takes a list of arbritrary many numbers (using argparse, more specifically -> nargs='+')) 
    # performs the functions on each of the numbers
# 3. Add Unit tests with assert

import argparse

def is_perfect(x):
    """Checks if an integer x is perfect. That is
    if the sum of divisors to x is equal to x.
    Example of a perfect number is 6, because
    1, 2, and 3 divides 6 and 1+2+3=6.
    Parameters:
    x (int): input number
    Returns:
    bool: True if x is perfect
    """
    sum = 0
    for i in range(1, x):
        if(x % i == 0):
            sum = sum + i
    if sum == x:
        return True
    else:
        return False
        
def is_prime(x):
    """Checks if an integer x is a prime number. That is
    if x is only divisible with 1 and itself.
    Parameters:
    x (int): input number
    Returns:
    bool: True if x is a prime number
    """
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True


def main(args):
    for n in args.x:
        n_int = int(n)
        print(f'\nNumber {n} is prime:', is_prime(n_int))
        print(f'Number {n} is perfect:', is_perfect(n_int))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if number is perfect and prime",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('x', type=int, nargs='+',                              # nargs(+) allows me to add one or more arguments
                        help='Numbers to determine if prime and perfect (must be separated by space)')
    args = parser.parse_args()
    main(args) # Call the main function if run from terminal
