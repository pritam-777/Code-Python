# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:48:07 2020

@author: SNIPER
"""

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
#dic4={}
#dic4.update(dic1)
#dic4.update(dic2)
#dic4.update(dic3)
dic5 = {}
for i in [dic1,dic2,dic3]:
    dic5.update(i)
    
print(dic5)