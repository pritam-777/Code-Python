# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:07:34 2020

@author: SNIPER
"""
import collections 
def Fequency_sort(item):
    result = sorted(item,key=item.count,reverse=True)
    str(result)
    return result
    
    
    
    
print(Fequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))


counts = collections.Counter(item)
new_list = sorted(lst, key=lambda x: -counts[x])