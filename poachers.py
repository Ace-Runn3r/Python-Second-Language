# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Poachers!

from sys import (stdin, stdout)
from scipy.spatial import ConvexHull, Delaunay

w, p, m = map(int, stdin.readline().split())

wardens, poachers, manatees = [], [], []

def in_hull(points, convexHull):
    if not isinstance(convexHull,Delaunay):
        convexHull = Delaunay(convexHull)

    return convexHull.find_simplex(points)>=0

for i in range(w):
    wardens.append(stdin.readline().split())

for i in range(p):
    poachers.append(stdin.readline().split())

for i in range(m):
    manatees.append(stdin.readline().split())

wardenHull = ConvexHull(wardens).points
poacherHull = ConvexHull(poachers).points

for man in manatees:
    if in_hull(man, wardenHull):
        stdout.write(f"Manatee at ({man[0]}, {man[1]}) is safe.\n")
    elif in_hull(man, poacherHull):
        stdout.write(f"Manatee at ({man[0]}, {man[1]}) is endangered.\n")
    else:
        stdout.write(f"Manatee at ({man[0]}, {man[1]}) is vulnerable.\n")
