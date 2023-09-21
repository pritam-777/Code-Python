# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:34:43 2020

@author: SNIPER
"""

def Second_index(text,symbol):
    
    count=text.count(symbol)
    if(count>=2):
        first = text.find(symbol)
        print("First :",first)
        second = text.find(symbol,first+1)
        print("Second :",second)
        return second
    else:
        return None
        
        
    
    
    
    

    
print(Second_index("find the river", "e"))
    