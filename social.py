# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Social Hierarchy

from sys import (stdin, stdout)

n, m, k = stdin.readline().split()
n = int(n)
order = ['_']*n # order of manatees
pickedPos = []

status = list(stdin.readline().split())  # manatee status order

for i in range(int(k)): # insert manatees that want certain position
    manatee, pos = stdin.readline().split()
    order[int(pos) - 1] = manatee
    pickedPos.append(manatee)


index = 0 # insert based on status rules
for item in status:
    if item in order:
        index = order.index(item)
        continue

    for pos in range(index, n):
        if order[pos] is '_':
            order[pos] = item
            index = pos
            break

posOfOne = ''
if '1' in order:    # check if one was already inserted
    posOfOne = order.index('1') + 1
else:
    i = n - 1
    statusIn = int(m) - 1
    while (i >= 0): # see if we can mix status position to move oone up in list

        if order[i] is '_':

            for k in range(i, -1, -1):  # go backwards in list from pos i
                temp = order[k]
                if temp in pickedPos and temp in status:
                    i = order.index(temp) # update pos since cant be moved back
                    break
                elif temp in status:
                    order[i] = temp
                    order[k] = '_'
                    break

        i -= 1

    posOfOne = order.index('_') + 1

stdout.write(f"{posOfOne}\n")