# Exercise 1
print(f'\nExercise 1\n')

import random

# generate 10 random integers between 1 and 100, and 10 random floats between 1 and 100

random_integers = [random.randrange(1, 100) for i in range(10)]
random_floats = [random.uniform(1,100) for i in range(10)]
print(f'{random_integers=}\n{random_floats=}')


# Exercise 2
print(f'\nExercise 2\n')

# Rewrite the following bad code and make it better

"""

# checks if a number is (1) perfect (2) prime

x = int(input("Provide a number to analyze: \n"))
sum = 0
for i in range(1, x):
    if (x % i == 0):
        sum = sum + i
if x >= 2:
    prime = True
    for y in range(2,x):
        if not (x % y):
            prime = False
else:
    prime = False
if sum == x:
    print("The number is perfect")
else:
    print("The number is not perfect")
if prime:
    print("The number is prime")
else:
    print("The number is not prime")

"""


# Divide up the code into functions. Which parts of the code can naturally be made into functions? 
    # 1. Function to see if number is perfect 
    # 2. Function to see if number is prime
    # 3. Function that interacts with the user and returns output (main)
# What should the functions take as parameters and return so that they can be useful outside this module? 
# You might want to have a main function main(x) that takes the number x as a parameter.


def is_perfect(x):
    sum = 0
    for i in range(1, x):
        if (x % i == 0):
            sum = sum + i
    if sum == x:
        return True
    else:
        return False

def is_prime(x):
    if x >= 2: 
        for y in range (2, x):
            if not (x % y):
                return False
    else:
        return False
    return True

def main(x):
    print(f'The number {x} is perfect: {is_perfect(x)}')
    print(f'The number {x} is prime: {is_prime(x)}')

x = int(input("Provide a number to analyze: \n"))

main(x)

# Exercise 3
print(f'\nExercise 3\n')

# Change the function from exercise 2 so that the user can decide whether to choose a number themselves or let the program choose one at random

def is_perfect(x):
    sum = 0
    for i in range(1, x):
        if (x % i == 0):
            sum = sum + i
    if sum == x:
        return True
    else:
        return False

def is_prime(x):
    if x >= 2: 
        for y in range (2, x):
            if not (x % y):
                return False
    else:
        return False
    return True

def choice():
    while True:
        x = input("Provide a number to analyze or press enter to analyze a random number: \n")
        if x == '':
            return random.randint(1, 10**6)  
        try:
            return int(x)
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def main():
    x = choice()
    print(f'The number {x} is perfect: {is_perfect(x)}')
    print(f'The number {x} is prime: {is_prime(x)}')

main()

