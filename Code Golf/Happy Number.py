# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:49:54 2020

@author: SNIPER
"""

def isHappyNumber(n):
    s = 0
    while(n!=0):
        r = n%10
        s = s+(r*r)
        n= n //10
    return s


n = 82
res  = n
while(res!=1 and res!=4):
    res = isHappyNumber(n)
if(res == 1):
    print("Happy Number")
elif(res==4):
    print("Not Happy")
        
    

        
    
    
    
    
    
    
