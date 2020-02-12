# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Progressive Pathways

from sys import (stdin, stdout)

def findPath(graph, node, prevNode, weight, pathWeights, visited):

    visited[node] = True
    weight += graph[prevNode][node]

    if node is 1:
        pathWeights.append(weight)
        return pathWeights

    for i in range(len(graph[node])):
        if i != prevNode and graph[node][i] > 0 and visited[i] is False:
            newVisit = visited.copy()
            findPath(graph, i, node, weight, pathWeights, newVisit)

    

intersec, connections = stdin.readline().split()
intersec = int(intersec)
connections = int(connections)
pathWeights = []

graph = [[0 for x in range(intersec)]for y in range(intersec)]

for line in range(connections):
    row, col, weight = map(int, stdin.readline().split())
    graph[row - 1][col - 1] = weight
    graph[col - 1][row - 1] = weight

visited = [False] * intersec
findPath(graph, 0, 0, 0, pathWeights, visited)

minPath = min(pathWeights)

paths = 0
for path in pathWeights:
    if path == minPath:
        paths += 1

stdout.write(f"{paths}\n")
