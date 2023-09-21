# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:02:29 2020

@author: SNIPER
"""
def Three_Word(st):
    count =0
    for i in st.split():
        
        if i.isalpha():
            
            count+=1
        else:
            count=0
        if count ==3:
            return True
    return False
        
    
    
    
    
    
    
    
    
st="bla bla bla bla"
print(Three_Word(st))