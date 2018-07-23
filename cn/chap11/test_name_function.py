#coding=UTF-8
'''
Created on 2018年7月18日

@author: Administrator
'''
'''
运行测试用例时，每完成一个单元测试，Python都打印一个字符：
                                                                                测试通过时打印一个句点；
                                                                                测试引发错误时打印一个E；
                                                                                测试导致断言失败时打印一个F。
'''
#先导入模块unittest以及要测试的函数
import unittest
from cn.chap11.name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_funcion.py"""
    
    def test_first_last_name(self):
        """能够正确的处理像Janis Joplin 这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """能够正确的处理像Wolfgan Amadeus Mozart 这样的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart','amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()