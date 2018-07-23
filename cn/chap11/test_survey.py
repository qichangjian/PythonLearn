#coding=UTF-8
'''
Created on 2018年7月18日

@author: Administrator
'''
import unittest
from cn.chap11.survey import AnonymousSurvey


#测试类
'''
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    def test_store_single_response(self):
        """测试答案是否被妥善"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        
        self.assertIn('English', my_survey.responses)
        
    def test_store_three_responses(self):
        """测试三个答案会被妥善保存"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        #断言测试新存储的三个答案是否通过
        for response in responses:
            self.assertIn(response,my_survey.responses)
    
unittest.main()
'''

#方法setup()
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    def setUp(self):
        """创建一个调查对象和一组 答案 供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
        
    def test_store_single_responses(self):
        """测试1个答案会被妥善保存"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """测试三个答案会被妥善保存"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
            
unittest.main()