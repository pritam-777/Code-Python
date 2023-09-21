# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:46:45 2020

@author: SNIPER
"""

students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
print(students)

for i in students:
    print(i)
    
    for j in students[i]:
        print(j,students[i][j])