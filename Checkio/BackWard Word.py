# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:05:44 2020

@author: SNIPER
"""

def BackwardEachWord(st):
    x = st.split(' ')
    newWords = [i[::-1]for i in x]
    print(newWords)
    newSentence = " ".join(newWords)
    return newSentence
    
        
    
    
    
    
    
st= "Hello World"
print(BackwardEachWord(st))