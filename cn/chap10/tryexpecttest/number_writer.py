#coding=UTF-8
'''
Created on 2018年7月18日

@author: Administrator
'''
import json


#使用json.dump() 和 json.load()
#存储数字列表json.dump
numbers = [2,3,5,7,11,13]

filename = 'numbers.json'

with open(filename,'w') as f_obj:
    #函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象
    json.dump(numbers,f_obj)

#读取列表到内存中json.load
with open(filename) as f_obj_r:
    numbers_r = json.load(f_obj_r)
    
print(numbers_r) 

