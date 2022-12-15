list = ["gordon ramsey", "aaron sanchez", "barack obama", "albert einstein"]

i = 0
for guests in list:
    print(f"\tGuest number {i+1} is {guests.title()}")
    i+=1
i = 0

cancelled = list.pop(2)
print(f"Uh oh, {cancelled.title()} cancelled!")
print(list)
print("\n")

newGuest = "jim carey"
list.insert(2, newGuest)
print(list)

print(sorted(list))

listLen = len(list)
print(listLen)
