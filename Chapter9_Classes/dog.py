class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"Sit, {self.name.title()}!")
        print(f"{self.name.title()} is now sitting.")

    def rollOver(self):
        print(f"Rollover, {self.name.title()}!")
        print(f"{self.name.title()} rolled over!")