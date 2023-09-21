# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:50:06 2020

@author: SNIPER
"""

def popular_word(text,words):
    text=text.lower()
    x =text.split()
    answer = {}
    for i in words:
        answer[i]=x.count(i)
        
    return answer
        
    
    
print(popular_word('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))