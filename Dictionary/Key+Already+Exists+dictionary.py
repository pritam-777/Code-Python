# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:02:07 2020

@author: SNIPER
"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def CheckDictinoary(n):
    if n in d:
         print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')
        
        
if __name__ == "__main__":
    CheckDictinoary(10)
    
        