#!/bin/python3

import math
import os
import random
import re
import sys


class Car:

    def __init__(self,MaxSpeed,SpeedUnit):
        self.MaxSpeed = MaxSpeed
        self.SpeedUnit = SpeedUnit
    def __str__(self):
        str1 = "Car with the maximum speed of {} {}"
        return str1.format(self.MaxSpeed,self.SpeedUnit)
    

        

class Boat:
    def __init__(self,MaxSpeed):
        self.MaxSpeed =MaxSpeed
    def __str__(self):
        str2 = "Boat with the maximum speed of {} knots"
        return str2.format(self.MaxSpeed)
        

if __name__ == '__main__':