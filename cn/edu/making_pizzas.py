#coding=UTF-8
'''
Created on 2018年7月17日

@author: Administrator
'''
#1导入整个模块
#from cn.edu import pizza
#2导入特定的函数
#from cn.edu.pizza import make_pizza
#3.使用asg 给函数指定别名
#from cn.edu.pizza import make_pizza as mp
#4.使用as给模块指定别名
#from cn.edu import pizza as p
#5.导入模块中的所有函数
from cn.edu.pizza import *

#1调用pizz中的函数
#pizza.make_pizza(16,'pepperoni')
#pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

#2导入整个代码块  
#make_pizza(16,'pepperoni')
#make_pizza(12,'mushrooms','green peppers','extra cheese')

#3.使用asg给函数指定别名
#p(16,'pepperoni')
#mp(12,'mushrooms','green peppers','extra cheese')

#4.使用as给模块指定别名
#p.make_pizza(12,'mushrooms','green peppers','extra cheese')
#p.make_pizza(16,'pepperoni')

#5.导入模块中的所有函数
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')