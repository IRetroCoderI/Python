
file = 'guestlist.txt'

with open(file, 'a') as file_object:
    active = True
    while active:
        guestName = input("Please enter your name!: ")
        if guestName == "quit":
            active = False
            break
        file_object.write(f"{guestName.title()}\n")
    