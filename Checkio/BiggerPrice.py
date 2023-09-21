# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:58:38 2020

@author: SNIPER
"""

def Bigger_price(limit,data):
    return sorted(data,key=lambda i:i['price'],reverse=True)[:limit]
    
    
    
    
    
print(Bigger_price(2,[
             {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}]) ) 