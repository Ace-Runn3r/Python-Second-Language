# -*- coding: utf-8 -*-
"""
Author: Cole Clements, cclements2016@my.fit.edu
Course: CSE 2050, Fall 2018
Project: Never Mind
"""
from sys import (stdin, stdout)

n, maker, guess = stdin.readline().split()

maker = list(maker)
guess = list(guess)
r, s = 0, 0

for i in range(int(n)):
    if (maker[i] == guess[i]):
        r +=1
        maker[i] = '_'
        guess[i] = '_'


for i in range(int(n)):
    if (guess[i] in maker) and (guess [i] is not '_'):
        s +=1
        maker[maker.index(guess[i])] = '_'



stdout.write(str(r) + " " + str(s) + '\n')