# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 19:57:01 2020

@author: SNIPER
"""

class Car :
    def __init__(self):
        print("init method Call")




ford = Car()
Audi = Car()



ford.speed =200
Audi.speed = 250

ford.color = 'Red'
Audi.color = 'Blue'

print(ford.color)
print(Audi.speed)

Audi.color = 'Yellow'

print(Audi.color)

