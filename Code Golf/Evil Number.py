# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 19:25:35 2020

@author: SNIPER
"""

def Evil_number(n):
    i = 0
    binary = 0
    while(n!=0):
        r = n%2
        binary = binary + r*(10**i)
        n =  n /10
        
    count_no = count_one(binary)
    if (count_no %2 ==0):
        return True
    
    return False
    
    
    
def count_one(num):
    count = 0
    while(num!=0):
        
        r = num % 10
        if r == 1:
            count+=1
        num = num/10
    return count
    
    
    

if __name__=='__main__':
    
    check=Evil_number(3)
    if(check):
        print ("Evil Nummber")
    else: 
        print ("Odious Number")
        
    