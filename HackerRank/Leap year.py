# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 20:09:16 2020

@author: SNIPER
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%400==0):
        return True
    elif(year % 4 == 0 and year % 100 != 0):
        return True
    
    
    return leap

year = int(input())
print(is_leap(year))