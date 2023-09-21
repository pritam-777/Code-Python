# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:19:43 2020

@author: SNIPER
"""

ls = [1,2,3,4,5]
new_ls=[]
for i in ls:
    if ls.count(i)>1:
        new_ls.append(i)
        
print(new_ls)
        