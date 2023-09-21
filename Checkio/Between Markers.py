# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:10:11 2020

@author: SNIPER
"""

def between_markers(text, begin, end):
     if begin in text:
        begin_index = text.find(begin) + len(begin)
     else:
        
        begin_index = 0
        
     if end in text:
        
        end_index = text.find(end)
     else:
        
        end_index = len(text)
     return text[begin_index:end_index]
        
    
    
    
print(between_markers('What is >apple<', '>', '<'))