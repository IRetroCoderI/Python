def myFunc(a, b):
    print("Function works!")
    print(a + b)

user = int(input("Please press 1 for calculator\n"))
if user == 1:
    print("test success")
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    myFunc(a, b)

else:
    print("Error")


