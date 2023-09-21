# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:57:04 2020

@author: SNIPER
"""

def Armstrong(n):
    p = n
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+r**3
        n//=10
    if(p==sum):
        print("Armstrong Number")
    else:
        print("Not Armstrong")




        
if __name__=='__main__':
    val =153
    Armstrong(val)
    
     
   
     
    
    