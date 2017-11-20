'''
pizzas = ['Fish', 'Lemon', 'Pork']
for pizza in pizzas:
    print(pizza)
    print("I like " + pizza + " pizza")
print("I really love pizza.")


animals = ['cat', 'dog', 'bird']
for animal in animals:
    print("A " + animal + " would make a great pet")
print("Any of these animals would make a great pet")
'''

'''
# 4.3
for value in range (1,21):
    print(value)
'''

'''
# 4.4
input = []
for value in range(1, 1000000):
    input.append(value)
print(input)
'''

'''
# 4.5
input = []
for value in range(1, 1000000):
    input.append(value)
print(min(input))
print(max(input))
print(sum(input))
'''

'''
# 4.6
for value in range(1,21,2):
    print(value)
'''

'''
# 4.7
for value in range(3, 31, 3):
    print(value)
'''

'''
# 4.8
number = [value ** 3 for value in range(1, 11)]
print(number)
'''

'''
# 4.10
fruit = ['apple', 'pear', 'peach', 'grape', 'banana']
print('The first three items in the list are:')
print(fruit[0:3])
print('Three items from the middle of the list are:')
print(fruit[1:4])
print('The last three items in the list are:')
print(fruit[-3:])
'''

'''
# 4.11
pizzas = ['Fish', 'Lemon', 'Pork']
friend_pizzas = pizzas[:]

pizzas.append('Beef')
friend_pizzas.append('Chicken')
print('My favorite pizzas are:')
print(pizzas)
print("My friend's favourite pizzas are:")
print(friend_pizzas)
'''

'''
# 4.13
foods = ('fish', 'meat', 'pork', 'pizza', 'shrimp')
for food in foods:
    print(food)

foods = ('fish', 'mushroom', 'pork', 'pizza', 'shrimp')
for food in foods:
    print(food)
'''