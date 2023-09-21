# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:07:06 2020

@author: SNIPER
"""

def ReverseWord_SwapCase(sentence):
    words = sentence.split()
    reverse_sentence = ' '.join(reversed(words))
    x = reverse_sentence.swapcase()
    print(x)
    
    
    
    
sentence = "aWESOME is cODING"
ReverseWord_SwapCase(sentence)
    
    