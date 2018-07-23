#coding=UTF-8
'''
Created on 2018年7月18日
@contact: 异常   json 文件读取
@author: Administrator
'''
from builtins import int

#异常
#处理ZeroDivisionError 异常
'''
输入：
print(5/0)

结果：
Traceback (most recent call last):
  File "D:\eclipse-workspace\PythonLearn\cn\chap10\tryexpecttest\division.py", line 10, in <module>
    print(5/0)
ZeroDivisionError: division by zero
'''
#使用try-except代码块
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("ZeroDivisionError : You can't divide by zero!")
    
print("other")
'''

#使用异常避免崩溃
#创建一个只执行除法晕眩的简单计算器 
'''
print("Give me two number , and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
'''

#优化计算器
'''
try except else
依赖于try代码块成功执行的代码都应放到else代码块中
'''
'''
print("Give me two number , and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Error： you can't divide by 0!")
    else:
        print(answer)
'''
       
#处理FileNotFoundError异常:read的文件不存在
'''
filename = 'alice.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
''' 

#修改后的程序
'''
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()     
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
'''    

#split（）拆分字符串
'''
title = "Alice in Wonderland"
words_title = title.split()
num_word = len(words_title)
print(str(num_word))
'''

#分析文本
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()     
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    #计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
    