"""
Author: Cole Clements, cclements2016@my.fit.edu
Course: CSE 2050, Fall 2018
Project: Working on the Railroad
"""
from sys import (stdin, stdout)

for line in stdin:
    x, y = line.split()
    if int(y)%2 == 0:
        stdout.write("possible" + '\n')
    else:
        stdout.write("impossible" + '\n')