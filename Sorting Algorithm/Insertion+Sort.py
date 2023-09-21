# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:39:51 2020

@author: SNIPER
"""

def insertion_sort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        hole = i
        while(hole>0 and arr[hole]<arr[hole-1]):
            arr[hole] = arr[hole-1]
            hole-=1
        arr[hole]=value
        
    
    
    

    
arr=[10,5,14,12,25,18,22]
insertion_sort(arr)
for i in range(len(arr)):
    
    print ("% d" % arr[i]) 
