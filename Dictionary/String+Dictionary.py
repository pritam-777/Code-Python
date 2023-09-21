# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:29:26 2020

@author: SNIPER
"""

str="pritamBhakta"
my_dict ={}
for i in str:
    my_dict[i]=my_dict.get(i,0)+1
    
print(my_dict)