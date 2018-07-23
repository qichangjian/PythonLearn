#coding=UTF-8
'''
Created on 2018年7月18日

@author: Administrator
'''
import json
from cn.chap10.tryexpecttest.greet_user import username


#保存和读取用户生成的数据
'''
username = input("What is your name?")

filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll rember you when you come back, " + username + "!")
'''

#将这个程序和greet_user结合
#如果以前存储了用户名就加载它
#否则就提示用户输入用户名并保存它
'''
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name ?")
    with open(filename,'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username)
else:
    print("Welcome back ," + username)
    
print("不管如何都会输出")
'''
    
#重构：
'''
代码能够正确地运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。这样的过程被称为重构。
重构让代码更清晰、更易于理解、更容易扩展。
'''
'''
def greet_user():
    """问候用户 并指出名字"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name ?")
        with open(filename,'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username)
    else:
        print("Welcome back ," + username)
    print("不管如何都会输出")
    
greet_user()
'''

#再次重构greet_user()方法
'''
def get_stored_username():
    """如果存储了用户就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def greet_user():
    """问候用户并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username)
    else:
        username = input("What is your name?")
        filename = 'username.json'
        with open(filename,'w') as f_obj:
            json.dump(filename, f_obj)
            print("We'll remember you when you come back," + username)

greet_user()
'''

#再次重构
def get_stored_username():
    """如果存储了用户就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(filename, f_obj)
    return username

def greet_user():
    """问候用户并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username)
    else:
        username = get_new_username()
        print("We'll remember you when you come back," + username)

greet_user()