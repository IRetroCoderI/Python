
results = {}

polling_active = True

while polling_active:
    name = input("what is your name? ")
    response = input("what mountain would you like to climb? ")
    results[name] = response

    anotherOne = input("Another guest? ")
    if anotherOne == "no":
        polling_active = False


for name, response in results.items():
    print(f"{name.title()} would like to climb {response.title()}. ")
