
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(f"Welcome to {self.name.title()}! we have the finest {self.cuisine.upper()} food in the world!")

    def openDoors(self):
        print(f"{self.name.title()} is open for business!!")


rest1 = Restaurant("DiGio's",'Italian')
rest1.describe_restaurant()

rest2 = Restaurant("pekking duck", "chinese")
rest2.describe_restaurant()