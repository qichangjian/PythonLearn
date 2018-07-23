#coding=UTF-8
'''
Created on 2018年7月17日

@author: Administrator
'''
from builtins import str
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        #给属性指定默认值
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    
    def read_odometer(self):
        """打印一条指出汽车历程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it")
    
    def update_odometer(self,mileage):
        """将历程表读数设置为指定的值 禁止将历程往回调""" 
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """"汽车油箱"""
        print("This car need a gas tank!")
        

#将实例用作属性：如果电瓶的描述太多了，可以把他相关的抽离出来作为一个属性给El...
class Battery():
    """模拟电动汽车  电瓶 的简单尝试"""
    
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery!")
  
    def get_range(self):
        """打印一条消息 指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = 300
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
        
class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self,make,model,year):
        """初始化父类的属性 再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
        #self.battery = Battery(80)
'''       
my_tesla = ElectricCar('tesla','model',2022)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
#修改电瓶的值
my_tesla.battery.battery_size = 88
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()
'''


