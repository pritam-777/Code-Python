# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:11:35 2020

@author: SNIPER
"""

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)


print(buddy.age)
print(miles.name)
        
        
    