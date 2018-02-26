class Restaurant():
    """docstring for Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)
        print("The cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening!")

    def set_number_served(self, served_number):
        self.number_served = served_number

    def increment_number_served(self, increment_number_served):
        self.number_served += increment_number_served

class IceCreamStand(Restaurant):
    """docstring for IceCreamStand"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_icescream_info(self):
        for flavor in self.flavors:
            print(flavor)

IceCream = IceCreamStand('ico', 'ice', ["fdfsa", "fdsf"])
IceCream.show_icescream_info()