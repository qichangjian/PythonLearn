#coding=UTF-8
'''
Created on 2018年7月18日

@author: Administrator
'''
import json

#读取remember_me.py中存储的数据
filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back," + username)