# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:43:07 2020

@author: SNIPER
"""

my_dict = {'data1':100,'data2':-54,'data3':247}
print(my_dict.keys())
print(my_dict.values())
print("sum is :" ,sum(my_dict.values()))
result = 1 
for s in my_dict:
    result = result*my_dict[s]
    
print("Multiplication ",result)