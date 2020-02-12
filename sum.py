# -*- coding: utf-8 -*-
"""
Author: Cole Clements, cclements2016@my.fit.edu
Course: CSE 2050, Fall 2018
Project: Large Sum
"""
from sys import (stdin, stdout)

sumOfN = 0
for line in stdin:
    sumOfN += int(line)

lastTen = str(sumOfN)[-10:]

stdout.write((lastTen + '\n'))
