# Exercise 1
print(f'\nExercise 1\n')


def divide_by_elems(filename,x):
    quotients = []
    try:
        with open(filename, 'r') as h:
            for n in h.readlines():
                try:
                    frac = x / int(n)
                    quotients.append(frac)
    return quotients

    