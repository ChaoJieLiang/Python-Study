# import unittest
# from city import city_name
#
#
# class NamesTestCase(unittest.TestCase):
#     def test_city_country(self):
#         formatted_name = city_name('Shanghai', 'China')
#         self.assertEqual(formatted_name, 'Shanghai,China')
#
#     def test_city_country_population(self):
#         formatted_name = city_name('Shanghai', 'China', '50000')
#         self.assertEqual(formatted_name, 'Shanghai,China - population 50000')
#
#
# unittest.main()

import unittest
from city import Employee


class EmployeeTestCase(unittest.TestCase):
    def test_give_default_raise(self):
        formatted_default = Employee('zhou', 'kai', 2000)
        formatted_default.give_raise()
        self.assertEqual(formatted_default.salary, 7000)

    def test_give_custom_raise(self):
        formatted_custom = Employee('zhou', 'kai', 2000)
        formatted_custom.give_raise(8000)
        self.assertEqual(formatted_custom.salary, 10000)


unittest.main()