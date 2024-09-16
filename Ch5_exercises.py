def divide_by_elems(filename,x):
    quotients = []
    try:
        with open(filename, 'r') as h:
            for n in h.readlines():
                try:
                    frac = x / int(n)
                    quotients.append(frac)
                except ZeroDivisionError:
                    print("divide_by_elems: Division by zero.")
                except ValueError:
                    print("divide_by_elems: Character could not be converted to int.")
    except IOError:
        print("divide_by_elems: A file-related problem occurred.")

    return quotients

    
data = divide_by_elems('numbers.txt', 2)
print(data)

def compute_ratios(xs,ys):
    ratios = []
    for i in range(min(len(xs),len(ys))):
        try:
            ratios.append(xs[i]/ys[i])
        except ZeroDivisionError:
            ratios.append(float('NaN')) # NaN = Not a Number
    return ratios

print(compute_ratios([2,3,4],[2,0,5]))
a = compute_ratios([2,3,4,0],[2,0,5])
