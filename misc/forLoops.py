cars = ["ferrari", "bmw", "altima", "civic", "porsche"]

for car in cars:
    if car == "altima":
        print(car.title())
    else:
        car.upper()


toppings = ["mushroom", "sausage", "pepperoni", "bell pepper", "anchovies", "salami"]

requested_topping = "mushroom"

if requested_topping in toppings:
    print(f"{requested_topping} is on our menu!")
else:
    print(f"{requested_topping} is not on our menu!")


banned_users = ["marie", "jason", "trump", "elon", "kanye", "tate"]

user = "jason"

if user not in banned_users:
    print(f"{user.title()} is not banned")
else:
    print(f"{user.title()} is banned for life LOL loser")




