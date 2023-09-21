# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:14:41 2021

@author: SNIPER
"""

class A():
    
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
        
        
        
x=A()
x.pub