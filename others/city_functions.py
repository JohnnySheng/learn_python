# city _functions.py 

def get_city_Name(city, country, population):
    city_name = city + ", " + country
    info = city_name.title() + " - population " + str(population)
    return info

