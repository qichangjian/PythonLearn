#conding=UTF-8
'''
Created on 2018年7月18日

@author: Administrator
'''
'''
各种断言方法
assertEqual(a, b)                  核实a == b
assertNotEqual(a, b)               核实a != b
assertTrue(x)                      核实x为True
assertFalse(x)                     核实x为False
assertIn(item, list)               核实item在list中
assertNotIn(item, list)            核实item不在list中
'''

#一个要测试的类：调查问卷
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    
    def __init__(self,question):
        """存储一个问题 并为存储答案作准备"""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """"显示调查问卷的问题"""
        print(self.question)
        
    def store_response(self,new_response):
        """存储单份调查问卷 也就是一个答案"""
        self.responses.append(new_response)
        
    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
            
