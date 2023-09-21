# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:45:26 2020

@author: SNIPER
"""

strat = 1
end = 20
s=0
for i in range(strat,end+1):
    if i>1:
        for n in range(2,i):
            if(i%n==0):
                break
        else:

            print(i)

