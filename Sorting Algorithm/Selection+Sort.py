# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:42:49 2020

@author: SNIPER
"""

def selection_sort(arr):
    for i in range(len(arr)):
        iMin = i
        for j in range(i+1,len(arr)):
            if(arr[iMin]>arr[j]):
                iMin = j
        arr[i],arr[iMin]=arr[iMin],arr[i]
                
    
    
if __name__ == '__main__':
    
    arr=[20,15,45,12,35,30]
    selection_sort(arr)
    for i in range(len(arr)):   
        print(arr[i])
            