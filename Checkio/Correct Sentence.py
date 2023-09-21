# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:33:04 2020

@author: SNIPER
"""

def check_sentence(text):
    length = len(text)
    text = text.capitalize()
    if text[length-1]!='.':
        text+="."
    return text
    
    
    
    
st = "good, morning"
print(check_sentence(st))