# -*- coding: utf-8 -*-

import math
def StrictDivisor(n):
    result = 0
    i=2
    while(i<=math.sqrt(n)):
        if(n%i==0):
            if(i==(n/i)):
                result=result+i
            else:
                result=result+(i+n/i)
        
             
        i=i+1
    return (result+1)
        
    

        
if __name__=='__main__':
    n=10
    print(StrictDivisor(n))
    