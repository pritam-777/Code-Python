# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:57:53 2021

@author: SNIPER
"""

def Fibonnaci(n):
    a=0
    b=1
    if n<0:
        print("Incorrect Input")
    elif n==0:
        print(a)
    elif n==1:
        print(b)
    else:
        print(a)
        
        for i in range(1,n):
            c=a+b
            print(c)
            b=a
            a=c
            
        
    
    
    
Fibonnaci(25)