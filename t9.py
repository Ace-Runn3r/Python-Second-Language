# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Trie, Trie, Again

from sys import (stdin, stdout)

t9Map = {   
            'a':2, 'b':2, 'c':2,
            'd':3, 'e':3, 'f':3,
            'g':4, 'h':4, 'i':4,
            'j':5, 'k':5, 'l':5,
            'm':6, 'n':6, 'o':6,
            'p':7, 'q':7, 'r':7, 's':7,
            't':8, 'u':8, 'v':8,
            'w':9, 'x':9, 'y':9, 'z':9
}

class Node:
    def __init__(self, value = None):
        self.children = {}
        self.probability = {value:0}

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert (self, word, probability):
        curNode = self.root
        charList = list(word)
        nodeList = {}
        prevChar = charList[0]
        if t9Map[prevChar] not in curNode.children:
            curNode.children[t9Map[prevChar]] = Node(prevChar)

            curNode = curNode.children[t9Map[prevChar]]
            curNode.probability[prevChar] += probability
            curNode.children[prevChar] = {}
        else:
            curNode = curNode.children[t9Map[prevChar]]
            if prevChar in curNode.probability:
                curNode.probability[prevChar] += probability
            else:
                curNode.probability[prevChar] = probability    
        nodeList = curNode.children[prevChar]
            
        for char in charList[1:]:
            if t9Map[char] not in nodeList:
                nodeList[t9Map[char]] = Node(char)
            
                curNode = nodeList[t9Map[char]]
                curNode.probability[char] += probability
                curNode.children[char] = {}
            else:
                curNode = nodeList[t9Map[char]]
                if char in curNode.probability:
                    curNode.probability[char] += probability
                else:
                    curNode.probability[char] = probability 
            nodeList = curNode.children[char]
                




trie = Trie()

w = int(stdin.readline())

for line in range(w):
    word, prob = stdin.readline().split()
    prob = int(prob)
    trie.insert(word, prob)

p = int(stdin.readline())

for line in range(p):
    t9Input =  list(stdin.readline())
