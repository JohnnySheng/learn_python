class Car():
    """docstring for Car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title
        
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!!!")

class ElectricCar(Car):
    """docstring for ElectricCar"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self): 
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model_s', 2016)
print(my_tesla.describe_battery())   