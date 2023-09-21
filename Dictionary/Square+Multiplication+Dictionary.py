# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:19:13 2020

@author: SNIPER
"""

def Square_Dictionary(n):
    d=dict()
    for i in range(1,n+1):
        d[i] = i*i
        
    print(d)
    
    
    
if __name__=="__main__":
    
    Square_Dictionary(10)
        
        