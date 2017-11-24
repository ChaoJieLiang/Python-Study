# def city_name(city, country, population=''):
#     if population:
#         name = city + "," + country + " - population " + population
#     else:
#         name = city + "," + country
#     return name


class Employee():

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, add_salary=5000):
        self.salary += add_salary