# Exercise 1
print(f'\nExercise 1 and 2\n')

def divide_by_elems(filename,x):
    quotients = []
    with open(filename, 'r') as h:
        for n in h:
            frac = x / int(n)
            quotients.append(frac)
    return quotients

# What would happen if argument to x was a string? 

divide_by_elems("numbers.txt", 2) # Test to see if function works
divide_by_elems("numbers.txt", "2") # Give an error because argument is a string, therefore it cannot perform the calculation

# Change the function so that:
# 1. If the string can be converted to an integer, the function should continue without crashing
# 2. Otherwise it should return None.
# 3. If file is incorrect give error.
# 4. Function can read the file but file could have incorrect values. Take that into consideration (value could be zero or a non-digit character) 
# Achieve this behavior with the help of try and except.

def divide_by_elems_better(filename,x):
    quotients = []
    try:                                # Evaluate argument x
        x = int(x)
    except ValueError:
        print("divide_by_elems_better: Error inputing an argument tha cannot be tranformed to integer.\nComputing to None")
        return None
    
    try:                                # Evaluate if file can be oppened
        h = open(filename, 'r')
    except IOError:
        print("divide_by_elems_better: A file-related problem occurred.")

    for n in h:
        try:                            # Evaluate if the numbers in the file are ok
            frac = x / int(n)
            quotients.append(frac)
        
        except ZeroDivisionError:
            print(f'divide_by_elems_better: Division by zero in line.')
        except ValueError:
            print(f'divide_by_elems_better: Character could not be converted to int.')

    return quotients
    
divide_by_elems_better("numbers.txt", 2) # works
divide_by_elems_better("numbers.txt", "2") # works
nada = divide_by_elems_better("numbers.txt", "s") ; print(nada) # works giving none
divide_by_elems_better("number_error.txt", "2") # works

# Note: I probably should have been doing this with if statements instead of try-except block




