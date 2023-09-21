# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:12:03 2020

@author: SNIPER
"""

import datetime
def Days_Count(date1,date2):
    
   #d1 = datetime.date(date1[0], date1[1], date1[2])
   d1 = datetime.date(*date1)
   #d2 = datetime.date(date2[0], date2[1], date2[2])
   d2 = datetime.date(*date2)
   return abs(d1-d2).days
    
DOB = 1997 ,5,19
CURRENTDATE = 2020,9,4
print(Days_Count(DOB,CURRENTDATE))