

status = True
while status:
    age = int(input("How old are you! "))

    if age == -1:
        status = False
    elif age < 3:
        price = "free"
    elif age < 12:
        price = "10 dollars"
    else:
        price = "15 dollars"

    if age != -1:
        print(f"Because you are {age}, your ticket will be {price}")

    