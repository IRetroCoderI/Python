



msg = ""


active = True

while active:
    city = input("What's your favorite city? ")

    if city == 'quit':
        break
    else:
        print(f"I'd love to visit {city.title()}")