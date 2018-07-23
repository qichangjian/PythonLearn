#coding=UTF-8
'''
Created on 2018年7月18日

@author: Administrator
'''
from cn.chap11.survey import AnonymousSurvey

#实例化一个对象      定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to sppeak?"
my_survey = AnonymousSurvey(question)

#显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_response(response)

#显示调查结果
print("\n Thank you to everyon who participated in the survey!")
my_survey.show_results()