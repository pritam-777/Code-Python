# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:15:37 2020

@author: SNIPER
"""
def First_Word(st):
    x = st.replace(".", " ").replace(",", " ").split()[0]
    print(x)
st = "Hello world"
First_Word(st)