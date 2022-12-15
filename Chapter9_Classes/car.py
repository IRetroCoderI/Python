class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0
    
    def bio(self):
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def setOdometer(self, mileage):
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back the odometer!")

    def updateOdometer(self, mileage):
        self.odometerReading += mileage
        return self.getMileage()

    def getMileage(self):
        return f"Mileage: {self.odometerReading}"


myCar = Car("nissan","altima",2002)
print(myCar.bio())
print(myCar.getMileage())

print(myCar.updateOdometer(30))