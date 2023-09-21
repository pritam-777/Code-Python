# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:27:54 2020

@author: SNIPER
"""

# Python code to demonstrate 
# sort list by frequency 
# of elements 

from collections import Counter 

ini_list = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 
			5, 5, 5, 4, 4, 4, 4, 4, 4] 

# printing initial ini_list 
print ("initial list", str(ini_list)) 

# sorting on bais of frequency of elements 
result = sorted(ini_list, key = ini_list.count)
								

# printing final result 
print("final list", str(result)) 
