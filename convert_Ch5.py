
def fahrenheit_to_celsius(t):
    t_celsius = (t - 32) / 1.8
    return t_celsius

condition = True

while condition:
    answer = input('Enter a temperature in Fahrenheit: ')
    try:
        t_fahrenheit = float(answer)
        condition = False
    except ValueError:
        print('Invalid parameter, please input a number.')

t = fahrenheit_to_celsius(t_fahrenheit)
print("Celsius: ", t)
