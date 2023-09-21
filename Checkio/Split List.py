# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 20:35:33 2020

@author: SNIPER
"""

def split_list(items):
    l = (len(items)+1)//2
    #print(l)
    # your code here
    return items[:l],items[l:]


if __name__ == '__main__':
    #print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

   
