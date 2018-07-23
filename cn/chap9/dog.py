#ecoding=UTF-8
'''
Created on 2018年7月17日

@author: Administrator
'''
#在Python中，首字母大写的名称指的是类。这个类定义中的括号是空的，因为我们要从空白创建这个类
class Dog():
    """一次模拟小狗的简单尝试"""
    #处的方法__init__()是一个特殊的方法，每当你根据Dog类创建新实例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
    #在这个方法的定义中，形参self必不可少，还必须位于其他形参的前面
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

#根据类创建实例     
#，命名约定很有用：我们通常可以认为首字母大写的名称（如Dog）指的是类，而小写的名称（如my_dog）指的是根据类创建的实例  
my_dog = Dog('willie',6) 
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
    