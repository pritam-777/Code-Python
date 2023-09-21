# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:41:18 2020

@author: SNIPER
"""
def Count(str):
    upper,lower,number,special=0,0,0,0
    for i in range(len(str)):
        if(str[i]>='A'  and str[i]<='Z'):
            upper+=1
        elif(str[i]>='a' and str[i]<='z'):
            lower+=1
        elif(str[i]>='0'and str[i]<='9'):
            number+=1
        else :
            special+=1
    print('Upper case letters:', upper) 
    print('Lower case letters:', lower) 
    print('Number:', number) 
    print('Special characters:', special) 
    
str="#pritAm@90Gmail.Com"
Count(str)