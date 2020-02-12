# -*- coding: utf-8 -*-
"""
Author: Cole Clements, cclements2016@my.fit.edu
Course: CSE 2050, Fall 2018
Project: Hamiltonian Hypercube
"""
from sys import (stdin, stdout)

n, start, end = stdin.readline().split()

grayCode = ['0','1'] # start of gray code sequence 
	
for count in range(int(n) - 1):
    mirror = grayCode[::-1]
    grayCode = (grayCode + mirror)
    for data in range(len(grayCode)):
        if int(data) < (len(grayCode)/2):
            grayCode[data] = '0' + grayCode[data]
        else:
            grayCode[data] = '1' + grayCode[data]

diff = grayCode.index(end) - grayCode.index(start) - 1

stdout.write(str(diff) + '\n')