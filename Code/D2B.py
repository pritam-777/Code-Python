# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:41:46 2020

@author: SNIPER
"""
def D2B(num):
    if num>1:
        D2B(num//2)
        
    print(num%2,end = " ")
    


if __name__=='__main__':
    val =7
    D2B(val)