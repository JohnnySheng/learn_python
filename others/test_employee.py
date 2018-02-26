import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('Johnny', 'Sheng', 10000)

            

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 15000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(250)
        self.assertEqual(self.my_employee.salary, 10250)

unittest.main()