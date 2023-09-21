# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:37:26 2020

@author: SNIPER
"""

def Abundant_Numbers(n):
    for i in range(1,n):
        sum_number = 0
        for j in range(1,i):
            if(i%j==0):
                sum_number+=j
        if(sum_number>i):
            print(i)
        sum_number = 0
    
            
            
        
        
    
    
    
    
if __name__=='__main__':
    Abundant_Numbers(100)
    
