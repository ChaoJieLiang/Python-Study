'''
# 5.3
alien_color = 'yellow'
if alien_color == 'green':
    print('You got 5 points')
'''

'''
# 5.4
alien_color = 'red'
if alien_color == 'green':
    print('You got 5 points')
else:
    print('You got 10 points')
'''

'''
# 5.5
alien_color = 'red'
if alien_color == 'green':
    print('You got 5 points')
elif alien_color == 'yellow':
    print('You got 10 points')
else:
    print('You got 15 points')
'''

'''
# 5.6
age = 32
if age <= 2:
    print('You are a baby')
elif (age > 2) and (age < 4):
    print('You start to walk')
elif (age >= 4) and (age < 13):
    print('You are a child')
elif (age >= 13) and (age < 20):
    print('You are a young man')
elif (age >= 20) and (age < 65):
    print('You are an adult')
elif age >= 65:
    print('You are an old man')
'''

'''
# 5.7
favorite_fruits = ['apple', 'orange', 'banana', 'grape', 'pear']
search_fruit = 'orange'
if search_fruit in favorite_fruits:
    print('You really like ' + search_fruit)
'''

'''
# 5.8
user_list = ['Peter', 'John', 'admin', 'Mike', 'Leo']
user = 'admin'

if user in user_list:
    print('Hello ' + user + ', thank you for logging in again')
elif user == 'admin':
    print('Hello admin, would you like to see a status report?')
'''

'''
# 5.9
user_list = []
user = 'admin'

if user_list:
    if user in user_list:
        print('Hello ' + user + ', thank you for logging in again')
    elif user == 'admin':
        print('Hello admin, would you like to see a status report?')
else:
    print('We need to find some users')
'''

'''
# 5.10
current_users = ['peter', 'john', 'mary', 'mike', 'leo']
new_users = ['John', 'Sherry', 'Mike', 'James', 'Franklin']

for new_user in new_users:
    new_user = new_user.lower();
    if new_user in current_users:
        print("This name is used, please select new one.")
    else:
        print('This name is unused, you could use it.')
'''

'''
# 5.11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    else:
        print(str(number) + 'th')
'''