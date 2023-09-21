# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:25:59 2021

@author: SNIPER
"""

#d1={"M1":"W1"
#,"M2":"W2"
#,"M3":"W3"
#,"M4":"W1"
#,"M5":{"W1","W4"}
 #  }
#for i in d1:
    

    
d2={"W1":"M1",
"W2":"M2",
"W3":"M3",
"W1":"M4",
"W1":"M5"}
print(d2)
for i in d2:
    if(i=="W1"):
        print(d2[i])