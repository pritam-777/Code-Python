# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:00:02 2020

@author: SNIPER
"""

def count_digit(st):
    digit = [i for i in st if i.isdigit()]
    return len(digit)
   
    
    
    
st = '5 plus 6 is'
print(count_digit(st))