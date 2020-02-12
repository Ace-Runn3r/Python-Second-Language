# -*- coding: utf-8 -*-
"""
Author: Cole Clements, cclements2016@my.fit.edu
Course: CSE 2050, Fall 2018
Project: Reversing Numbers
"""
from sys import (stdin, stdout)

for line in stdin:
    binaryForm = "{0:b}".format(int(line))
    binaryForm = binaryForm[::-1]
    baseTen = int(binaryForm, 2)
    
stdout.write(str(baseTen)  + '\n')
