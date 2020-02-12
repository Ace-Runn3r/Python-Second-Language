# -*- coding: utf-8 -*-
"""
Author: Cole Clements, cclements2016@my.fit.edu
Course: CSE 2050, Fall 2018
Project: Alto Saxophone
"""
from sys import (stdin, stdout)

def fingerChange(oldChord, newChord):

    fingerPress = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        if oldChord[i] != newChord[i]:
            if (oldChord[i] - newChord[i]) == -1:
                fingerPress[i] = 1

    return fingerPress

chords = {
        'c': [0,1,1,1,0,0,1,1,1,1], 'd': [0,1,1,1,0,0,1,1,1,0],
        'e': [0,1,1,1,0,0,1,1,0,0], 'f': [0,1,1,1,0,0,1,0,0,0],
        'g': [0,1,1,1,0,0,0,0,0,0], 'a': [0,1,1,0,0,0,0,0,0,0],
        'b': [0,1,0,0,0,0,0,0,0,0], 'C': [0,0,1,0,0,0,0,0,0,0],
        'D': [1,1,1,1,0,0,1,1,1,0], 'E': [1,1,1,1,0,0,1,1,0,0],
        'F': [1,1,1,1,0,0,1,0,0,0], 'G': [1,1,1,1,0,0,0,0,0,0],
        'A': [1,1,1,0,0,0,0,0,0,0], 'B': [1,1,0,0,0,0,0,0,0,0]
         }

for line in stdin:
    song = line
    fingerCount = chords[song[0]]

    for i in range(1, len(song) - 1): #need to ignore new line character
        fingerPress = fingerChange(chords[song[i - 1]], chords[song[i]])
        fingerCount =  [sum(x) for x in zip(fingerCount, fingerPress)]

    stdout.write(str(fingerCount).strip('[]').replace(',','') + '\n')