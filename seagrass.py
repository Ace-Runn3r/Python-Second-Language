# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Easting Seagrass

from sys import (stdin, stdout)

_ = int(stdin.readline())

manatees = list(map(int, stdin.readline().split()))
manatees.sort(reverse = True)

count = 0

for manatee in manatees:
    if manatee >= count:
        count += 1

stdout.write(f"{count}\n")