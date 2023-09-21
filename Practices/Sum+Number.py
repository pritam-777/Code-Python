# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:58:38 2020

@author: SNIPER
"""
def sum_addition(st):
    num=[]
    for i in st.split():
        
        if i.isdigit():
            num.append(int(i))
    return sum(num)
    
    
    
    
    
st='my numbers is 2'
print(sum_addition(st))