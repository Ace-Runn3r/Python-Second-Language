# -*- coding: utf-8 -*-
"""
Author: Cole Clements, cclements2016@my.fit.edu
Course: CSE 2050, Fall 2018
Project: To Advertise, Or Not
"""
from sys import (stdin, stdout)

n = int(stdin.readline())

for i in range(n):
    inputLine = stdin.readline()
    dontAdvertise, doAdvertise, advertiseCost = inputLine.split()
    
    dontAdvertise = int(dontAdvertise)
    netIncome = int(doAdvertise) - int(advertiseCost)
    
    if (dontAdvertise > netIncome):
        stdout.write("do not advertise" + '\n')
    elif (dontAdvertise == netIncome):
        stdout.write("does not matter" + '\n')
    else:
        stdout.write("advertise" + '\n')
