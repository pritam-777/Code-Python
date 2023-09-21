# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:20:40 2020

@author: SNIPER
"""

def sun_angle(time):
    h, m = list(map(int, time.split(':')))
    print("Hour ",h)
    print("Minutes",m)
    angle = 15 * h + m / 4 - 90
    print(angle)
    return angle if 0 <= angle <= 180 else "I don't see the sun!"



if __name__ == '__main__':
   print(sun_angle("10:15"))