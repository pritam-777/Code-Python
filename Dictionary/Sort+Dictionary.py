# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:33:56 2020

@author: SNIPER
"""

color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
          
print(color_dict)

for i in sorted(color_dict):
    print("%s: %s" % (i, color_dict[i]))