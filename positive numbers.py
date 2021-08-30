# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 01:48:20 2021

@author: aninditha
"""

list1 = (12, -7, 5, 64, -14)
list2 = (12, 14, -95, 3)
print("input:",list1)
print("input:",list2)
new_list1 = list(filter(lambda x: x >0, list1))
new_list2 = list(filter(lambda x: x >0, list2))
print("output:",new_list1)
print("output:",new_list2)