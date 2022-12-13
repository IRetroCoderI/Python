

def makeSandwiches(size, *items):
    sandwich = {'toppings' : items}
    for item in items:
        print(f'Adding {item.upper()} to your sandwich')
    print(f"Sandwich finished! Your sandwich is {size} and has {items}")

makeSandwiches('large', 'salami','pickles','olives','tuna','deez')
