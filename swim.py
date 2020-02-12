# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Swimming Manatee 

from sys import (stdin,stdout)
from operator import itemgetter

def updateTop(atTop, currentMan):
    if ((atTop - currentMan[0]) < 0):
        return 0
    else:
        return atTop - currentMan[0]

n = int(stdin.readline())
upTimes, downTimes = [], []
leastTime = 0

for line in range(n):
    up, down = stdin.readline().split()
    upTimes.append(int(up))
    downTimes.append(int(down))

minUp = min(upTimes)
minDown = min(downTimes)

manatees = list(zip(upTimes, downTimes))
manatees = sorted(manatees, key = itemgetter(0, 1), reverse = True)
print(manatees)
firstMan = []
lastMan = []

length = len(manatees)
i = 0
while (i < length):
    if manatees[i][1] == minDown and not lastMan:
        lastMan = manatees.pop(i)
        length -= 1
        continue
    if manatees[i][0] == minUp and not firstMan:
        firstMan = manatees.pop(i)
        length -= 1
        continue
    i += 1
    
if not firstMan:
    firstMan = manatees.pop(-1)

leastTime = firstMan[0]
atTop = firstMan[1]
while (manatees):
    currentMan = manatees.pop(0)
    leastTime += currentMan[0]
    atTop = updateTop(atTop, currentMan)
    atTop += currentMan[1]

leastTime += lastMan[0]
atTop = updateTop(atTop, lastMan)
atTop += lastMan[1]
leastTime += atTop

stdout.write(f"{leastTime}\n{firstMan}\n{lastMan}\n")