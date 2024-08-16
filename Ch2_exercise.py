# Exercise 1
print(f'\nExercise 1: a, b, c\n')

# Exercise 2
print(f'Exercise 2')
usern = input(f'Give me an integer: ')

if int(usern) % 2 == 0:
    print(f'{usern} is an even number\n')
else:
    print(f'{usern} is an odd number\n')

# Exercise 5
print(f'Exercise 5')

def f(x,y):
    if x != 0 and y == 0:
        return(f'The result is infinite...')
    elif x == 0 and y == 0:
        return(f'Indeterminate form')
    else:
        return(x/y)
    
a = int(input(f'Dividend: '))
b = int(input(f'Divisor: '))

print(f'{f(a,b)}\n')

# Exercise 7
print(f'Exercise 7')

def nand(x,y):
    if x and y:
        return False
    else:
        return True
    
print(nand(True,True))
print(nand(True,False))
print(nand(False,True))
print(nand(False,False))
    
def nor(x,y):
    if not x and not y:
        return True
    else:
        return False

print(nor(True,True))
print(nor(True,False))
print(nor(False,True))
print(nor(False,False))

def xnor(x, y):
    if x and y:
        return True
    elif not x and not y:
        return True
    else:
        return False
    
print(xnor(True,True))
print(xnor(True,False))
print(xnor(False,True))
print(xnor(False,False))
