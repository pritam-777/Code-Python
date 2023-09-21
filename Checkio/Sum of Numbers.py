# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:45:52 2020

@author: SNIPER
"""
def addition_number(st):
    num = []
    for i in st.split():
        
        if i.isdigit():
            num.append(int(i))
    return sum(num)
    
  
st = '5 plus 6 is'
print(addition_number(st))

