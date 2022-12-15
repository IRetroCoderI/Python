try:
    a = int(input('num1: '))
    b = int(input('num2: '))
    print(a+b)
except ValueError:
    print("Numbers only, please!")