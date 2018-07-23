#ecoding=UTF-8
'''
Created on 2018年7月17日

@author: Administrator
'''
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
            
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#修改属性的值
my_new_car.odometer_reading = 20
my_new_car.read_odometer()

#通过方法修改属性的值
my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.read_odometer()

#通过方法将属性的值递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

#继承：子类
class ElectricCar(Car):
    """电动汽车的独到之处"""
    
    def __init__(self,make,model,year):
        """电动车的独到之处初始化父类的属性 再初始化电动汽车特有的属性"""
        """初始化父类的属性"""
        super().__init__(make, model, year)
        #电动汽车特有属性
        self.battery_size = 70
        
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery!")

    #重写父类中的方法
    def fill_gas_tank(self):
        """"电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s',2017)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()











