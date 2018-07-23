#ecoding=UTF-8
'''
Created on 2018年7月18日

@author: Administrator
'''

#                                                                    第十章：文件和异常
#从文件中读取数据
#读取整个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    #为read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行
    #删除多出来的空行，可在print语句中使用rstrip()：
    print(contents.rstrip())


#文件路径
#相对路径
with open('txtfile\pi_digits1.txt') as file_object:
    contents = file_object.read()
    print(contents)
with open('txtfile\\pi_digits1.txt') as file_object:
    contents = file_object.read()
    print(contents)
with open('..\\alltxtfile\\pi_digits2.txt') as file_object:
    contents = file_object.read()
    print(contents)
  
#绝对路径 \\转义字符
with open('D:\\eclipse-workspace\\PythonLearn\\cn\\alltxtfile\\pi_digits2.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
file_path = 'D:\\eclipse-workspace\\PythonLearn\\cn\\alltxtfile\\pi_digits2.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

#逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
    print("over")
    for linenumber in range(1,2):
        print(linenumber)
        
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line2 in file_object:
        print(line2.rstrip())

#创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    
print(lines)
for line in lines:
    print(line)
for line in lines:
    print(line.rstrip())


#使用文件的内容
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
print(pi_string.__len__())
'''
读取文本文件时，Python将其中的所有文本都解读为字符串。如果你读取的是数字，并
要将其作为数值使用，就必须使用函数int()将其转换为整数，或使用函数float()将其转
换为浮点数。
'''

#包含一个一百万位的大型文件
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string[:52] + "...")
print(len(pi_string))   
    
#圆周率值中是否包含你的生日
'''
birthday = input("Enter your birthday , in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")
'''   
    
   
#写入文件
'''
1.打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'

2.写入（'w'）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件

3.Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式

4.函数write()不会在你写入的文本末尾添加换行符
'''
filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
        
#附加到文件
#如果你要给文件添加内容，而不是覆盖原有的内容，可以附加模式打开文
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets!\n")
    file_object.write("I love apps.")
    










