# -*- coding: utf-8 -*-
"""
Author: Cole Clements, cclements2016@my.fit.edu
Course: CSE 2050, Fall 2018
Project: ASCII Clock
"""
from sys import (stdin, stdout)

numbers = {
    '1' : [['    +'],
           ['    |'],
           ['    |'],
           ['    +'],
           ['    |'],
           ['    |'],
           ['    +']],

    '2' : [['+---+'],
		   ['    |'],
		   ['    |'],
		   ['+---+'],
		   ['|    '],
		   ['|    '],
           ['+---+']],

    '3' : [['+---+'],
		   ['    |'],
		   ['    |'],
		   ['+---+'],
		   ['    |'],
		   ['    |'],
		   ['+---+']],

    '4' : [['+   +'],
           ['|   |'],
           ['|   |'],
           ['+---+'],
           ['    |'],
           ['    |'],
           ['    +']],

    '5' : [['+---+'],
           ['|    '],
           ['|    '],
           ['+---+'],
           ['    |'],
           ['    |'],
           ['+---+']],

    '6' : [['+---+'],
           ['|    '],
           ['|    '],
           ['+---+'],
           ['|   |'],
           ['|   |'],
           ['+---+']],

    '7' : [['+---+'],
           ['    |'],
           ['    |'],
           ['    +'],
           ['    |'],
           ['    |'],
           ['    +']],

    '8' : [['+---+'],
           ['|   |'],
           ['|   |'],
           ['+---+'],
           ['|   |'],
           ['|   |'],
           ['+---+']],

    '9' : [['+---+'],
           ['|   |'],
           ['|   |'],
           ['+---+'],
           ['    |'],
           ['    |'],
           ['+---+']],

    '0' : [['+---+'],
           ['|   |'],
           ['|   |'],
           ['+   +'],
           ['|   |'],
           ['|   |'],
           ['+---+']],

    ':' : [['   '],
           ['   '],
           [' o '],
           ['   '],
           [' o '],
           ['   '],
           ['   ']]
         }

data = True
while data:
    time = stdin.readline().strip('\n')
    if time == 'end':
        stdout.write('end')
        data = False
        continue

    for i in range(7):
        for num in time:
            stdout.write(str(numbers[num][i]).strip("[']"))
            if num is not time[-1]:
                stdout.write(' ')

        stdout.write('\n')
    stdout.write('\n' + '\n')