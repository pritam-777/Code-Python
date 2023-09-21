# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:42:46 2021

@author: SNIPER
"""

def FizzBuzz(n):
    for i in range(1,50):
        if(i%3==0 and i%5==0):
            print(i,"FizzBuzz")
        else:
            if(i%3==0):
                print(i,"Fizz")
            elif(i%5==0):
                print(i,"Buzz")
            
            
    
    
    
    
    
    
    
    
    
    
n=50
FizzBuzz(n)