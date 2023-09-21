# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:02:35 2020

@author: SNIPER
"""

#def end_zeros(num: int) -> int:
    # your code here
   # num_str=str(num)
   # num_str=num_str[::-1]
    #count=0
    #make number into a string and reverse it.
    #for each character count the number of zeros
    #stop counting when you find a digit that is not a zero
    #for i in num_str:
        #if i=='0':
            #count+=1
        #else:
            #break
    #return count
    
a =1101000
b=str(a)
b = b[::-1]
print(b)
count = 0
for i in b:

    
    if(i=='0'):
        
        count+=1
    else:
        break
    
print(count)
       