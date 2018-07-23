#coding=UTF-8
'''
Created on 2018年7月18日

@author: Administrator
'''
def get_formatted_name(first, last,middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()