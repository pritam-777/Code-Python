# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:07:09 2020

@author: SNIPER
"""

def  nearest_value(set_value,n):
    set_value = sorted(set_value)
    difference = [abs(i-n)for i in set_value]
    print(difference)
    index = difference.index(min(difference))
    return set_value[index]
    
       
       
    
    
    

    
    
a = {4,3,6,7,8,9,11,12}
n = 10
print(nearest_value(a,n))
