
# # 10.1
# with open('learning_python.txt') as file_objects:
#     contents = file_objects.read()
#     print(contents)
#
# with open('learning_python.txt') as file_objects:
#     for line in file_objects:
#         print(line)
#
# with open('learning_python.txt') as file_objects:
#     lines = file_objects.readlines()
#
# for line in lines:
#     print(line.rstrip())

# # 10.2
# with open('learning_python.txt') as file_objects:
#     lines = file_objects.readlines()
#
# for line in lines:
#     print_line = line.replace("Python", "C++")
#     print(print_line.rstrip())

# 10.3
# name = input("Please input your name.")
# with open('guest.txt', 'w') as file_object:
#     file_object.write(name)

# # 10.4
# status = True
# while status:
#     name = input("Please input your name. 'q' for quit.")
#     if name == 'q':
#         break
#     else:
#         print("Hello, " + name)
#         with open('guest_book.txt', 'a') as file_object:
#             file_object.write(name + "\n")

# 10.6-7
# status = True
# while status:
#     try:
#         nb1 = input('Please input a number."q" for quit.')
#         if nb1 == 'q':
#             break
#         nb2 = input('Please input another number."q" for quit')
#         if nb2 == 'q':
#             break
#         print(int(nb1) + int(nb2))
#
#     except ValueError:
#         print("不合法的数字，请重新输入")

# # 10.8
# try:
#     with open('cats.txt') as file_objects:
#         contents = file_objects.read()
# except FileNotFoundError:
#     print("Could not find cats.txt.")
# else:
#     print(contents)


# # 10.9
# try:
#     with open('cats.txt') as file_objects:
#         contents = file_objects.read()
# except FileNotFoundError:
#     pass
# else:
#     print(contents)

# # 10.11
# import json
#
# number = input("Please input your favorite number.")
# filename = 'favouritenumber.json'
# with open(filename, 'w') as file_object:
#     json.dump(number, file_object)
#
# with open(filename, 'r') as file_object:
#     number = json.load(file_object)
# print("I know your favorite number! It's " + number)

# # 10.12
# import json
#
# filename = 'number.json'
# try:
#     with open(filename) as f_obj:
#         numbers = json.load(f_obj)
# except FileNotFoundError:
#     numbers = input("Please input your favorite number")
#     with open(filename, 'w') as f_obj:
#         json.dump(numbers, f_obj)
#         print("I remember your favorite number")
# else:
#     print("I know your favorite number! It's " + str(numbers))

# 10.13
