# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:58:46 2020

@author: SNIPER
"""

class Car :
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color
    def set_speed(self,value):
        self.__speed= value
    def get_speed(self):
        return self.__speed
    def set_color(self,col):
        self.__color= col
    def get_color(self):
        return self.__color
        




ford = Car(200,'Red')
Audi = Car(300,'Green')
honda = Car(400,'Yellow')




ford.set_speed(600)
print(ford.get_speed())
print(honda.get_color())
