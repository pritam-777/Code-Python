# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:21:14 2021

@author: SNIPER
"""

class Robot():
    
    def __init__(self, name):
        print(name + " has been created!")
        
    def __del__(self):
        print ("Robot has been destroyed")
        
        
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y