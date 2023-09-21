# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:32:15 2020

@author: SNIPER
"""

def split_pairs(a):
    new_lst = []

    if len(a) % 2 != 0:
        a += "_"
       

    for i in range(0, len(a), 2):
        new_lst.append(a[i : i + 2])
    return new_lst


print(split_pairs("abc"))