#coding=UTF-8
'''
Created on 2018年7月16日

@author: Administrator
'''
from builtins import str

#                                        第六章：字典
#一个简单的字典
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
#使用字典 ： 字典是一系列键-值对。与键相关联的值可以是数字，字符串，列表，字典
#实际上可以将任何对象用作字典的值
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print(alien_0)
#添加字典的键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#先创建一个空字典
alien_0 = {}
alien_0['color'] = 'red' 
alien_0['points'] = 5
alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)

#修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0)

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x: " + str(alien_0['x_position']))
#向右移动外星人：根据当前速度决定它能移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x: " + str(alien_0['x_position']))

#删除键值对
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['color']
print(alien_0)

#类似于对象组成的字典 : 最后个加上逗号是为了方便以后添加
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    'qi':'c',
    }

print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() +
    "!")

#遍历字典
#注意，即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }

for key,value in user_0.items():
    print("Key：" + key + "\tValue:" + value)

for name,language in user_0.items():
    print(name.title() + "'s favorite language is " + language.title())

#遍历字典中的所有键
#注意：遍历字典时候，会默认遍历所有的键
for name in user_0.keys():
    print("Name:" + name.title())
for name in user_0:
    print("Name:" + name.title())

#，我们使用了字典名，并将变量name的当前值作为键
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    'qi':'c',
    }
friends = ['phil','sarah','qi']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() +
              ",I see your favorite language is " +
              favorite_languages[name].title() +"!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our pool!")

#按照顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll!")

#遍历字典中的所有值
print("The follwing languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#用set（）方法去除结果中的重复值
print("set :")
for language in set(favorite_languages.values()):
    print(language.title())

#嵌套：有时候将一系列字典存储在列表中，或者将列表作为值存储在字典中这成为嵌套
#字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#创建一个用于存储外星人的空列表
aliens = []
#创建30个绿色外星人:自动
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    
#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
    
#显示创建了多少外星人
print("Total number of aliens: " + str(aliens.__len__()))
print("Total number of aliens: " + str(len(aliens)))
    
  
#创建一个用于存储外星人的空列表
aliens = []
#创建30个绿色外星人:自动
for alien_number in range(0,30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
#前三个变色
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'   
        alien['points'] = 10
#显示前五个
for alien in aliens[0:5]:
    print(alien)   
print("...")
    
    
#在字典中存储列表
#存储所点披萨的信息
pizza = {
    'crust':'thick',
    'toppings':['muchrooms','extra cheese'],
    }
#概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the follwing topping:")

for topping in pizza['toppings']:
    print("\t" + topping)
    
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language are:")
    for language in languages:
        print("\t" + language.title())
  
for name,languages in favorite_languages.items():
    
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is:")
        print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite language are:")
        for language in languages:
            print("\t" + language.title())
            
            
#在字典中存储字典
users = {
    'aeinstenin':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        }
    }
for username,user_info in users.items():
    print("UserName:" + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFullname :" + full_name)
    print("\tlocation :" + location)
    
    
    
   
#                                                           第七章：    用户输入和while循环
'''
#函数input（）的工作原理       在2.7版本中使用raw_input()
message = input("Tell me something, and I will repeat it to you:")
print(message)  

prompt = "If you tell us who you are ,we can personalize the message you see."  
prompt += "\nWhat is your first name? "
name = input(prompt)
print("Hello, " + name + "!")
    
#使用int（）来获取用户输入

age = input("how old are you? ")
age = int(age)
if age > 20:
    print("old > 20")
else:
    print("old <= 20")   
     
#求模运算符也就是取余 %
number = input("Enter a number, and I'll tell you if it's even or odd")
number = int(number)

if number % 2 == 0:
    print("\nTher number " + str(number) + "is even")
else:
    print("\nTher number " + str(number) + "is odd")
    

#while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
#让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program1. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program2. "
message = ""
while message != 'quit':
    message = input(prompt)    
    if message != 'quit':
        print(message)

#使用标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program3. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
   
#使用break退出循环
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program4. "
while True:
    city = input(prompt)
    if city == 'quit':
        break    
    else:
        print("I'd love to go to " + city.title())
 '''    
       
#在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
    
    
#使用while循环来处理列表和字典
#在列表之间移动元素

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice','brian','candace','qi']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
#显示所有已经验证的用户
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

'''
#使用用户输入来填充字典
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
# 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# 将答卷存储在字典中
    responses[name] = response
# 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n -------Roll Result ---------")
for name,response in responses.items():
    print(name + " Would like to climb " + response + ".")
'''


#                                                                                     第八章 函数
#使用关键字def来告诉Python你要定义一个函数。这是函数定义
#处的文本是被称为文档字符串（docstring）的注释，描述了函数是做什么的。文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。
#定义函数 def xx():
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()

#向函数传递信息
def greet_user1(username):
    """显示简单的问候语"""
    print("Hello, " + username.title())

greet_user1('jesse')

#传递参数
#位置参数
def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name)

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#关键字实参：  关键字实参是传递给函数的名称—值对,       参数顺序不重要
describe_pet(animal_type='cat', pet_name='hollcat')
describe_pet(pet_name='hollcat',animal_type='cat')

#默认值
def describe_pet1(pet_name,animal_type='dog'):
    """默认值显示宠物信息"""
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name)

describe_pet1(pet_name='willie1')
describe_pet1('wi')

def describe_pet2(pet_name='qi',animal_type='dog'):
    """默认值显示宠物信息"""
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name)
#使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参
describe_pet2()

#返回值
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#让实参变为可选的
def get_formatted_name1(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name1('jimi', 'hendrix')
print(musician)
pmusician = get_formatted_name1('john', 'hooker', 'lee')
print(pmusician)

#返回字典
def build_person(first_name, last_name):
    """返回一个字典,其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person1(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person
musician = build_person1('jimi', 'hendrix', age=27)
print(musician)

#结合使用函数和while
'''
def get_formatted_name2(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
formatted_name = get_formatted_name2(f_name, l_name)
print("\nHello, " + formatted_name + "!")
'''

#传递参数
def greet_users(names):
    '''向列表中的每个用户都发出简单的问候'''
    for name in names:
        msg = "Hello, " + name.title() + "！"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

#在函数中修改列表
#原来的
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
#模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#现在修改后
def print_models(unprinted_designs,completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止打印每个设计后，都将其移到列表completed_models中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop() 
        #模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['iphone case','robot pendant','dodecahedron','qi']
completed_models = []  

#禁止函数修改列表:传递过去的参数是切边，所以元列表没有清空
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
#原列表清空
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

#传递任意数量的实参   *   ，注意，
#Python将实参封装到一个元组中，即便函数只收到一个值也如此
def make_pizza(*topping):
    """打印顾客点的所有配料"""
    print(topping)
make_pizza('pipperoni')
make_pizza('muchrooms','green pepper','extra cheese')
    
    
def make_pizza1(*toppings):
    """概述要制作的pizza"""
    print("\n Making a pizza with the following topping:")
    for topping in toppings:
        print(" - " + topping)
    
make_pizza1('pipperoni')
make_pizza1('muchrooms','green pepper','extra cheese')


#结合使用位置实参和任意数量实参
def make_pizza2(size,*toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print(" - " + topping)
        
make_pizza2(16,'pipperoni')
make_pizza2(14,'muchrooms','green pepper','extra cheese')

#使用任意数量的关键字实参   将函数编写成能够接受任意数量的键—值对
def build_profile(first,last,**user_info):
    """创建一个字典，其中半酣我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',location='princenton',field='physics')
print(user_profile)

#导入整个模块 pizza.py making_pizzas.py
#1导入整个模块
#from cn.edu import pizza

#导入特定的函数
#2导入特定的函数
#from cn.edu.pizza import make_pizza

#使用as给函数指定别名
#from cn.edu.pizza import make_pizza as mp

#使用as给模块指定别名
#from cn.edu import pizza as p

#导入模块中的所有函数
#from cn.edu.pizza import *

#函数编写指南
'''
1.应给函数指定描述性名称,且只在其中使用小写字母和下划线
2.每个函数都应包含简要地阐述其功能的注释
3.给形参指定默认值时,等号两边不要有空格 .对于函数调用中的关键字实参，也应遵循这种约定：
4.如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开
'''


#                                                         第九章：创建和使用类






















