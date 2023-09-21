# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 23:38:54 2021

@author: SNIPER
"""

num = int(input())
sum = 0
temp = num
while(temp > 0):
	sum += temp % 10
	temp = int(temp / 10)
    
if(num / sum == 0):
	print(num/sum)
else:
	print("Not Harshad Number")