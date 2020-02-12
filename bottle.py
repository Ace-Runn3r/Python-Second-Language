# -*- coding: utf-8 -*-
"""
Author: Cole Clements, cclements2016@my.fit.edu
Course: CSE 2050, Fall 2018
Project: Bottle Recycling
"""
from sys import (stdin, stdout)

for line in stdin:
    start, day, cost = line.split()
    
    totalBottles = int(start) + int(day)
    cost = int(cost)
    
    finalCount = 0
    bottlesBought = 0
    
    while (totalBottles >= cost):
        bottlesBought = int(totalBottles/cost)
        totalBottles += bottlesBought
        totalBottles -= (bottlesBought * cost)
        finalCount += bottlesBought 
        
    stdout.write(str(finalCount) + '\n')
