

def fahrenheit_to_celsius(t_fahrenheit) -> float:
    """Function calculates the conversion from fahrenheit to celsius"""
    t_celsius = (t_fahrenheit - 32) / 1.8
    return t_celsius

def temp_input() -> float:
    """Function serves only to get data from user and test if it's the correct type of data"""
    condition = True
    while condition:
        answer = input('Enter a temperature in Fahrenheit: ')
        try:
            t_fahrenheit = float(answer)
            condition = False
        except ValueError:
            print('Invalid parameter, please input a number.')
    return  t_fahrenheit 

def main():
    t_fahrenheit = temp_input()
    t = fahrenheit_to_celsius(t_fahrenheit)
    print("Celsius: ", t)

if __name__ == "__main__":
    main()
