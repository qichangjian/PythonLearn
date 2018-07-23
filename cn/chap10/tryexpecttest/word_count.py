#coding=UTF-8
'''
Created on 2018年7月18日

@author: Administrator
'''
from builtins import str
'''
def cout_word(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry ,the file " + filename + " does not exist."
        print(msg)
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
        
filename = 'alice.txt'
cout_word(filename) 

#列表存储名
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
    cout_word(filename)
'''

#失败的时候一声不吭 pass
def cout_word(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #记录消息在文件中missing_files.txt
        with open('missing_files.txt','w') as f_miss:
            msg = "Sorry ,the file " + filename + " does not exist."
            f_miss.write(msg)
        #这里不提示任何消息
        pass
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

#列表存储名
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt','meiyou.txt', 'little_women.txt']
for filename in filenames:
    cout_word(filename)


#打印一个单词在一个列表中出现的次数
'''
line = "Row , row , row you boat"
num_row = line.count('row')
num_rows = line.lower().count('row')    
print(str(num_row) + ":" + str(num_rows) )
'''













  

