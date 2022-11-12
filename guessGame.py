import random
import time

num = random.randrange(1, 100)

user = 0
while (user != num) and (user != -1):
    user = int(input("guess what number I'm thinking of from 1 to 100! "))
    time.sleep(1)

    if(user < num):
        print("Too low, guess again! ")
        time.sleep(1)
    elif(user > num):
        print("Too high, guess again! ")
        time.sleep(1)


if user == num:
    print("That's it! Thank you for playing!\n")
else:
    print("Okay, see you next time!")











