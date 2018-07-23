#coding=UTF-8
'''
Created on 2018年7月17日

@author: Administrator
'''
from _collections import OrderedDict
from cn.chap9.car2 import ElectricCar, Car


my_tesla = ElectricCar('tesla','model s',8089)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_car = Car('tesla','model s',8999)

#Python标准库
'''
字典让你能够将信息关联起来，但它们不记录你添加键—值对的顺序。要创建字典并记录其
中的键—值对的添加顺序，可使用模块collections中的OrderedDict类。OrderedDict实例的行为
几乎与字典相同，区别只在于记录了键—值对的添加顺序
'''
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
    print(name.title() + " 's favorite language is " + language.title())
    
#类编码风格
'''
类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名
和模块名都采用小写格式，并在单词之间加上下划线
'''
