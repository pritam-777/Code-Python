# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:22:14 2020

@author: SNIPER
"""

#|****
#|*
#|***
#|**
#|****

def pattern(n):
    for i in n:
        print("|",end=" ")
        print("*"*int(i))
 

if __name__=='__main__':
    n="41325"
    pattern(n)
    
    