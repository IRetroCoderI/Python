bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f"My favorite bike is {bicycles[-1].title()}")

bike_request = input("What bike would you like today? ")

if(bicycles.__contains__(bike_request.lower())):
    print("This bike is in stock")
else: 
    print("we do not have this bike in stock")


names = ["dio", "miguel", "isaiah", "angie"]
names.append("patrick")
names.insert(2, "Garry".lower())

for x in names:
    print(f"One of my friends is {x.title()}\n")
print("These are all of my friends!!")


print(names)