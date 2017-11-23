'''
# 9.1-2
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is opening")


restaurant = Restaurant('AAA', 'BBB')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('CCC', 'DDD')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('EEE', 'FFF')
restaurant.describe_restaurant()
restaurant.open_restaurant()
'''

'''
# 9.3
class User():
    def __init__(self, first_name, last_name, *other_info):
        self.first_name = first_name
        self.last_name = last_name
        self.other_info = other_info

    def describe_user(self):
        print(self.first_name, self.last_name, self.other_info)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)


user = User('Peter', 'Liang', 25, 'Male')
user.describe_user()
user.greet_user()
'''

'''
# 9.4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def description(self):
        print("There are " + str(self.number_served) + " customers have been in " + self.restaurant_name)

    def set_number_served(self, customer_number):
        self.number_served = customer_number

    def increment_number_served(self):
        self.number_served = self.number_served + 1

restaurant = Restaurant('Pizzahut', 'Pizza', 4)
restaurant.description()

restaurant.set_number_served(6)
restaurant.description()

restaurant.increment_number_served()
restaurant.increment_number_served()
restaurant.description()
'''

'''
# 9.5
class User():
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = login_attempts

    def increment_login_attempts(self):
        self.login_attemps = self.login_attemps + 1

    def reset_login_attempts(self):
        self.login_attemps = 0

    def describe(self):
        print(self.first_name + " " + self.last_name + ", you have logged " + str(self.login_attemps) + " times.")


user = User('Peter', 'Liang', 4)
user.increment_login_attempts()
user.increment_login_attempts()
user.describe()
user.reset_login_attempts()
user.describe()
'''

'''
# 9.6
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name + ".")
        print("Cuisine type is " + self.cuisine_type + ".")
        print("This restaurant has a total of " + str(self.number_served) +
              " people to eat.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is opening")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors)
        super().__init__(restaurant_name, cuisine_type)
        for i in flavors:
            print(i)


ice_cream = IceCreamStand('KFC', 'AAA', ['Chocklate', 'Strawberry'])
ice_cream.describe_restaurant()
'''

'''
# 9.7
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.first_name + " " + self.last_name + " has " + str(self.privileges))


admin = Admin('Peter', 'Liang')
admin.show_privileges()
'''

'''
# 9.8
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges():
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        privi = []
        for x in privileges:
            privi.append(x)

    def show_privileges(self):
        print("You have all authority in user")


admin = Admin('Peter', 'Liang')
admin.privileges.show_privileges()
'''

'''
# 9.14
from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(str(randint(1, self.sides)))


die = Die(6)
die.roll_die()
die = Die(10)
die.roll_die()
die = Die(20)
die.roll_die()
'''
