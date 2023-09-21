# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:39:44 2020

@author: SNIPER
"""
def safe_pawns(pawns):
    
    pawns_indexes = set()
    for p in pawns:
        
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))
        count=0
    for row,col in pawns_indexes:
        is_safe = ...
        if is_safe:
            count+=1
    
    
    
    
safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6