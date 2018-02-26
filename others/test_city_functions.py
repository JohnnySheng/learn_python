import unittest
from city_functions import get_city_Name

class CityTestCase(unittest.TestCase):
    """docstring for CityTestCase"""
    def test_city_functions(self):
        format_city = get_city_Name("shanghai", "china",2800000)
        self.assertEqual(format_city, "Shanghai, China - population 2800000")
        

unittest.main()