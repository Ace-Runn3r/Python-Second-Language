# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Grazing Patterns 

from sys import(stdin, stdout)
import copy

class Vertex:
    def __init__ (self, name, grass = True):
        self.name = name
        self.grass = grass

    def updateGrass(self, value):
        self.grass = value

    def hasGrass(self):
        return self.grass

    def __str__(self):
        return str(self.name) + str(self.grass)

class Graph:
    verticies = {}
    edges = {}
    def __init__ (self, verticies = {}):
        if not verticies:
            for i in range(1, 26):
                vert = Vertex(i)
                self.verticies[i] = vert
                self.edges[vert] = None
            self.createEdges()
        else:
            self.verticies = verticies
            for i in range(1, 26):
                self.edges[self.verticies.get(i)] = None
            self.createEdges()

    def createEdges(self):
        for i in range(1, 26):
            connect = []
            if (((i + 1) % 5) != 1):
                connect.append(self.getVertex(i + 1))
            if (i + 5 < 25):
                connect.append(self.getVertex(i + 5))
            if (((i - 1) % 5) != 0):
                connect.append(self.getVertex(i - 1))
            if (i - 5 > 0):
                connect.append(self.getVertex(i - 5))
            self.edges[self.getVertex(i)] = connect

    def getVertex (self, Vertex):
        return self.verticies.get(Vertex)

    def BFS (self, vert1, vert2):
        topQueue = []
        bottomQueue = []

        topQueue.extend(self.getEdges(vert1))
        bottomQueue.extend(self.getEdges(vert2))

        while(topQueue and bottomQueue)


    def getEdges (self, Vertex):
        vert = self.getVertex(Vertex)
        return self.edges.get(vert)

    def outPut(self):
        for key in self.verticies:
            print(f"{key} : {self.verticies[key]}")
    
    def printEdges(self):
        for i in range(1, 26):
            print(i)
            vert = self.getVertex(i)
            connections  = self.edges.get(vert)
            for k in connections:
                print(k)
            print("\n")
        
    def copyGraph(self):
        vertCopy = copy.deepcopy(self.verticies)
        return Graph(vertCopy)

field = Graph()
print(field.getEdges(5))
def pathCheck(field):
    noGrass = True
    for key in field.verticies:
        if field.verticies[key].grass is True:
            noGrass = False    
    return noGrass



n = int(stdin.readline())
maxMovesPer = int((23 - n)/2) + 1
numOfPaths = 0

for line in range(n):
    row, col = stdin.readline().split()
    vertIndex = ((int(row) * 5) - 5 + int(col))
    vertex = field.getVertex(vertIndex)
    vertex.updateGrass(False)

bLoc = 1
mLoc = 25

numOfPaths = 1



stdout.write(f"{numOfPaths}\n")