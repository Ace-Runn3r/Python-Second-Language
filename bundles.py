# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Seagrass Bundles

from sys import (stdin, stdout)

N, K = stdin.readline().split()

docks = {}

for line in range(int(K)):
    lower, upper = stdin.readline().split()

    for i in range(int(lower), int(upper) + 1):
        if i in docks:
            docks[i] = docks[i] + 1
        else:
            docks[i] = 1

rangeList = docks.values()
if len(docks) < int(N):
    smallest = 0
else:
    smallest = min(rangeList)

largest = max(rangeList)

difference = largest - smallest

stdout.write(f"{difference}\n")
