"""
Author: Cole Clements, cclements2016@my.fit.edu
Course: CSE 2050, Fall 2018
Project: Playing Tic-Tac-Toe
"""
from sys import (stdin, stdout)

posWin = []
single, team = 0, 0

# store wins by row
for i in range(3):
    posWin.append(list(stdin.readline().rstrip()))

# store wins by column
for col in range(3):
    temp = []
    for row in range(3):
        temp.append(posWin[row][col])
    posWin.append(temp)

# store diagonal wins
dia = [posWin[0][0], posWin[1][1], posWin[2][2]]
dia2 = [posWin[2][0], posWin[1][1], posWin[0][2]]
posWin.append(dia)
posWin.append(dia2)

# find wins
for i in range(8):
    if len(set(posWin[i])) is 1:
        single += 1

    if len(set(posWin[i])) is 2:
        team += 1

stdout.write(f"{single}\n{team}\n")