#coding UTF-8
'''
Created on 2018年7月17日

@author: Administrator
'''
#import语句让Python打开模块car，并导入其中的Car类
from cn.chap9.car import Car

my_new_car = Car('audd', 'a4', 3333)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

