'''
# 7.1
car = input("需要什么车？")
print("Let me see if I can find you a " + car)
'''

'''
# 7.2
dinner = input("需要多少人用餐！")
if int(dinner) > 8:
    print("没有空桌")
else:
    print("有空桌")
'''

'''
# 7.3
number = input("请输入一个整数")
if (int(number)%10) != 0:
    print("不是10的整数倍")
else:
    print("是10的整数倍")
'''

'''
# 7.4
prompt = "\n请输入需要的配料！"
prompt += "\n输入'quit'退出。"

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("我们会在披萨中添加" + message)
'''

'''
# 7.5
prompt = "\n请输入年龄。"
prompt += "\n输入'quit'退出。"

message = ""
while message != 'quit':
    message = input(prompt)
    if int(message) < 3:
        print("免费")
    elif (int(message) >= 3) and (int(message) < 12):
        print("10元")
    elif int(message) > 12:
        print("15元")
'''

'''
# 7.8
sandwich_orders = ['pork', 'beef', 'chicken', 'vegetable']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich")
    finished_sandwiches.append(current_sandwich)
print(finished_sandwiches)
'''

'''
# 7.9
sandwich_orders = ['pork', 'pastrami', 'chicken', 'vegetable', 'pastrami',
                   'pastrami']

print("Pastrami sandwich is sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
'''

'''
# 7.10
prompt = "\n请输入最想去的地方"
prompt += "\n输入'quit'退出。"

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("我们会在披萨中添加" + message)
'''