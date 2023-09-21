# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:09:09 2020

@author: SNIPER
"""

def Three_Word(st):
    count=0
    for word in st.split():
        if word.isalpha():
            count+=1
        else :
            count=0
        if count==3:
            return True
    return False
    
    
    st = "bla bla bla bla"
    print(Three_Word(st))
    
    