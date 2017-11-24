'''
# 8.1
def display_message():
    print("I learn function from this chapter.")


display_message()
'''

'''
# 8.2
def favorite_book(title):
    print("One of my favorite books is " + title)


favorite_book("Alice in Wonderland")
'''

'''
# 8.3
def make_shirt(size, letter):
   print("You select size " + size + " with letter " + letter)


make_shirt("6", "A")
make_shirt(size="8", letter="B")
'''

'''
# 8.4
def make_shirt(size, letter = "I love Python"):
   print("You select size " + size + " with letter " + letter)


make_shirt("4")
'''

'''
# 8.5
def describe_city(city_name, country = "China"):
   print(city_name + " is in " + country)


describe_city("Shanghai")
describe_city("Los Anglos", "USA")
'''

'''
# 8.6
def city_country(city, country):
   rt_Country = city + " " + country
   return rt_Country.title()


print(city_country("Shanghai", "China"))
'''

'''
# 8.7
def make_album(name, cd, song_number=''):
   if song_number:
      info = {'singer_name': name, 'CD_name': cd, 'Song_Number':song_number}
   else:
      info = {'singer_name': name, 'CD_name': cd}
   return info
'''

'''
print(make_album("周杰伦", "爱在西元前"))
print(make_album("周杰伦", "龙卷风", "4"))
'''

'''
# 8.8
while True:
   print("\nPlease type singer's name.")
   print("Enter 'q' to quit.")

   singer_name = input("Singer name: ")
   if singer_name == 'q':
      break

   album_name = input("Album name: ")
   if album_name == 'q':
      break

   print(make_album(singer_name, album_name))
'''

'''
# 8.9
magicians = ['Peter', "Sherry", 'Rong']


def show_magicians(magicians):
   for magician in magicians:
      print(magician)


show_magicians(magicians)
'''

'''
# 8.10
magicians = ['Peter', "Sherry", 'Rong']
new_magicians = []

def show_magicians(magicians):
   for magician in magicians:
      print(magician)


def make_great(current_magicians, complete_magicians):
   while current_magicians:
      complete_magician = "the Great " + current_magicians.pop()
      complete_magicians.append(complete_magician)


show_magicians(magicians)
make_great(magicians, new_magicians)
show_magicians(new_magicians)
'''

'''
# 8.11
magicians = ['Peter', "Sherry", 'Rong']
new_magicians = []


def show_magicians(magicians):
   for magician in magicians:
      print(magician)


def make_great(current_magicians, complete_magicians):
   while current_magicians:
      complete_magician = "the Great " + current_magicians.pop()
      complete_magicians.append(complete_magician)


show_magicians(magicians)
make_great(magicians[:], new_magicians)
show_magicians(magicians)
show_magicians(new_magicians)
'''

'''
# 8.12
def sandwichs (*materials):
   for material in materials:
      print(material)


sandwichs("meat")
sandwichs("pork", "fish")
'''

'''
# 8.13
profile = {}


def build_profile(first, last, **user_info):

   profile['first_name'] = first
   profile['last_name'] = last
   for key, value in user_info.items():
      profile[key] = value
   return profile

   
user_profile = build_profile('albert', 'einstein', location='princenton', field='physics')
print(user_profile)
'''

'''
# 8.14
profile = {}
def build_car_profile(name, mfg, **car_profile):
   profile['name'] = name
   profile['mfg'] = mfg

   for key, value in car_profile.items():
      profile[key] = value
   return profile


car = build_car_profile('subaru', 'outback', color='blue', two_package=True)
print(car)
'''