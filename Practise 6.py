'''
# 6.1
friend_name = {'first_name': 'Peter', 'last_name': 'Liang',
                'age': 25, 'city': 'Shanghai'}
print(friend_name['first_name'])
print(friend_name['last_name'])
print(friend_name['age'])
print(friend_name['city'])
'''

'''
# 6.2
favourite_number = {'Peter': 5, 'Mary': 4, 'John': 100,
                    'Sherry': 13, 'James': 50}
print("Peter's favourite number is " + str(favourite_number['Peter']))
print("Mary's favourite number is " + str(favourite_number['Mary']))
print("John's favourite number is " + str(favourite_number['John']))
print("Sherry's favourite number is " + str(favourite_number['Sherry']))
print("James's favourite number is " + str(favourite_number['James']))
'''

'''
# 6.5
river = {'nile': 'Egypt', 'yz river': 'China', 'heng river': 'India'}

for k, v in river.items():
    print("\nThe " + k.title() + " runs through " + v.title())

for k in river.keys():
    print(k)
    
for v in river.values():
    print(v)
'''

'''
# 6.6
favorite_languages = {'jen': 'python', 'sarah': 'c',
                        'edward': 'ruby', 'phil': 'python'}
user = ['jen', 'peter']

for name in user:
    if name in favorite_languages.keys():
        print("Thank you ")
    else:
        print("Please join us.")
'''

'''
# 6.7
friend_name0 = {'first_name': 'Peter', 'last_name': 'Liang',
                'age': 35, 'city': 'Shanghai'}
friend_name1 = {'first_name': 'Sherry', 'last_name': 'Shao',
                'age': 34, 'city': 'Shanghai'}
friend_name2 = {'first_name': 'Rong', 'last_name': 'Cao',
                'age': 33, 'city': 'Shanghai'}
peoples = [friend_name0, friend_name1, friend_name2]

for people in peoples:
    print(people)
'''

'''
# 6.9
favorite_places = {'Peter': ['Shanghai'], 'Sherry': ['Shanghai', 'USA']
                   , 'Rong': ['Australia', 'UK']}
for k,v in favorite_places.items():
    print(k, v)
'''

# 6.11
cities = {
            'Shanghai': {
                'Country': 'China',
                'Population': 1000,
                'Fact': 'Modern'
                        },
            'Los Anglos': {
                'Country': 'USA',
                'Population': 2000,
                'Fact': 'Beautiful'
                        },
         }
for city in cities.items():
    print(city)
