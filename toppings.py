

toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requests in requested_toppings:
    if requests in toppings:
        print(f"Adding {requests}")
    else:
        print(f"Sorry, we don't have {requests}")

print(f"\nFinished making your pizza!!")