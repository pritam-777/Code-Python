# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:05:44 2020

@author: SNIPER
"""

from itertools import *
import itertools
dic ={'1':['a','b'],'2':['c','d']}
for i in itertools.product(*[dic[j]for j in sorted(dic.keys())]):
    print(''.join(i))