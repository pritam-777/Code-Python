# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:22:54 2020

@author: SNIPER
"""

my_dict={"Math":98,"Physics":82,"Chemistry":85,"Bengali":77,"English":78,"Computrt Science":91}

key_max = max(my_dict.keys(),key=(lambda i : my_dict[i]))
key_min = min(my_dict.keys(),key=(lambda i : my_dict[i]))

print(my_dict[key_max])
print(my_dict[key_min])