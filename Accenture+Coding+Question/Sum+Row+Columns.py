# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 19:37:33 2021

@author: SNIPER
"""

def Max_row_column(n,m,ls):
    
    
    for i in range(m):
        new_ls=[]
        for j in range(m,n):
            new_ls.append(ls[j])
            
    print(new_ls)
    
    
    
n=3
m=3
ls=[1,2,3,4,5,6,7,8,9]
Max_row_column(n,m,ls)
            