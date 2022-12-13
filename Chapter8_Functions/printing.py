

def hello(*names):
    for name in names:
        print(f"Hello {name.title()}! it is very nice to meet you!")

def yellAt(*names):
    for name in names:
        print(f"WHAT IS WRONG WITH YOU {name.upper()}! THAT WAS NOT OKAY")