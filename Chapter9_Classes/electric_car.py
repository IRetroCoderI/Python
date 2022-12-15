from car import Car

class Battery:
    def __init__(self, batterySize = 75):
        self.batterySize = batterySize

    def describeBattery(self):
        print(f"This car has a {self.batterySize}-kWh battery.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()
    
    def getBatterySize(self):
        self.battery.describeBattery()


my_Tesla = ElectricCar("Tesla", "Model X", "2022")

print(my_Tesla.bio())
my_Tesla.setOdometer(100)
print(my_Tesla.getMileage())
my_Tesla.getBatterySize()
