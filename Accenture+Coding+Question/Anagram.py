# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:08:40 2021

@author: SNIPER
"""

#Anagram 

def areAnagram(str1,str2):
    n1=len(str1)
    n2=len(str2)
    if n1!=n2:
        return 0
    
    str1=sorted(str1)
    str2=sorted(str2)
    
    for i in range(0,n1):
        if str1[i]!=str2[i]:
            return 0
        
    return 1




str1 = "test"
str2 = "ttew"
if(areAnagram(str1,str2)):
    print("Yes")
else:
    print("No")