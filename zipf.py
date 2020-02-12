# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Failure to Communicate

from sys import (stdin, stdout, argv)
from scipy.optimize import leastsq
from scipy.stats import entropy
from urllib.request import urlopen
from numpy import vectorize
from gzip import open as gopen

def objective(x):
    return x + (x * x)


text = urlopen(argv[1])
text = gopen(text, 'rb')
text = text.read().decode()

charCounts = {}

for item in text:
    if item in charCounts:
        charCounts[item] = charCounts[item] + 1
    else:
        charCounts[item] = 1

probArray = []
for item in charCounts:
    probArray.append(charCounts[item] / len(text))

vec = vectorize(probArray)
alpha = leastsq(objective, 1)

print(alpha)
probArray.sort(reverse=True)
print(charCounts)