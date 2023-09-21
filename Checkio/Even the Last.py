# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:09:10 2020

@author: SNIPER
"""

def Even_Last(ls):
    if len(ls)>=1:
        return (sum(ls[0::2]))*ls[-1]
    else:
        return 0
        
    
            
    
    
    
 
ls = [1, 3, 5]
print(Even_Last(ls))