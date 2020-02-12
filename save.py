# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Save the Manatees

from sys import (stdin, stdout, argv)
from urllib.request import urlopen

def buildboard(mapData):
    gameMap = [[]]
    row= 0
    for element in mapData:
        if element is "\n":
            gameMap.append([])
            row += 1
            continue
        gameMap[row].append(element)

    del gameMap[row] # last new line creats empty list

    maxWidth = 0
    for row in gameMap:
        if len(row) > maxWidth:
            maxWidth = len(row)
    
    for row in gameMap:
        if len(row) < maxWidth:
            for index in range(maxWidth - len(row)):
                row.append(' ')

    manateePos, gatePos, index = 0, 0, 0
    boats = []
    for row in gameMap:
        for element in row:
            if element is "*":
                boats.append(index)
            elif element is "M":
                manateePos = index
            elif element is ("G" or "O"):
                gatePos = index
    
            index += 1

    return gameMap, maxWidth, manateePos, gatePos, boats

def printBoard(gameMap):
    for row in gameMap:
        stdout.write("{}\n".format("".join(row)))
    stdout.write("\n")

def validMove(gameMap, row, col, manRow, manCol):
    element = gameMap[row][col]

    if row < 0 or col < 0:
        return False
    elif row >= len(gameMap) or col >= len(gameMap[0]):
        return False
    elif element is '#' or element is 'G':
        return False
    elif element is '*':
        if not boatCheck(gameMap, row, col, manRow, manCol):
            return False
        
    return True

def boatCheck(gameMap, boatRow, boatCol, manRow, manCol):
    if manRow - boatRow is 1: #meaning boat is above manatee
        return False
    moveAxis = gameMap[boatRow]

    if (((moveAxis[boatCol + 1] is ' ') and  (moveAxis[boatCol - 1] is 'M')) 
    or ((moveAxis[boatCol - 1] is ' ') and (moveAxis[boatCol + 1] is 'M'))):
        return True

    if ((gameMap[boatRow + 1] is ' ') and (gameMap[boatRow - 1] is 'M')):
        return True

    return False

def makeMove(gameMap, row, col, hycount, gatePos, boatsLoc, movedBoat):
    gameState = 0 # 0 = continue; 1 = win; -1 = injured
    value = gameMap[row][col]

    if value is '\\':
        hycount += 1
        gameMap[row][col] = '_' # have to remove hy for check
        checkGate(gameMap, gatePos)

    elif value is 'O':
        gameState = 1

    elif value is '*':
        curIndex = ((row * len(gameMap[0])) + col)

        if gameMap[row][col + 1] is 'M': # push boat left
            gameMap[row][col - 1] = '*'
            boatsLoc[boatsLoc.index(curIndex)] = curIndex - 1
            movedBoat = curIndex - 1
        elif gameMap[row][col - 1] is 'M': # push boat right
            gameMap[row][col + 1] = '*'
            boatsLoc[boatsLoc.index(curIndex)] = curIndex + 1
            movedBoat = curIndex + 1
        else:   # push boat down
            gameMap[row + 1][col] = '*'
            boatsLoc[boatsLoc.index(curIndex)] = curIndex + width
            movedBoat = curIndex + width

    gameMap[row][col] = 'M'
    return hycount, gameState, movedBoat

def checkGate(gameMap, gatePos):
    hyacinth = False
    for line in gameMap:
        if '\\' in line:
            hyacinth = True

    if not hyacinth:
        gameMap[gatePos // width][gatePos % width] = 'O'

def updateBoats(gameMap, boatsLoc, width, state, movedBoat):
    boatsLoc.sort(reverse = True)

    for boat in boatsLoc:
        if boat is movedBoat:
            continue

        row = boat // width
        col = boat % width
        below = gameMap[row + 1][col]

        if below is '*':
            if gameMap[row + 1][col + 1] is ' ' and gameMap[row][col + 1] is ' ':
                gameMap[row][col] = ' '
                gameMap[row + 1][col + 1] = '*'
                boatsLoc[boatsLoc.index(boat)] = ((row + 1) * width + (col + 1))
                col += 1

            elif gameMap[row + 1][col - 1] is ' ' and gameMap[row][col - 1] is ' ':
                gameMap[row][col] = ' '
                gameMap[row + 1][col - 1] = '*'
                boatsLoc[boatsLoc.index(boat)] = ((row + 1) * width + (col - 1))
                col -= 1
            else:
                continue

            if gameMap[row + 2][col] is 'M': # for if manatee gets hit
                state = -1
                gameMap[row + 2][col] = 'W'
                 
        elif below is ' ':
            gameMap[row][col] = ' '
            gameMap[row + 1][col] = "*"
            boatsLoc[boatsLoc.index(boat)] = ((row + 1) * width + col)
             
            if gameMap[row + 2][col] is 'M': # for if manatee gets hit
                state = -1
                gameMap[row + 2][col] = 'W'

    return state


mapData = urlopen(argv[1]).read().decode()

gameMap, width, manateePos, gatePos, boatsLoc = buildboard(mapData)

height = len(gameMap)

printBoard(gameMap)

moves = list(stdin.readline())
manRow = manateePos // width
manCol = manateePos % width
score, hyCount, state, movedBoat = 0, 0, 0, -1
multiplier = 1

checkGate(gameMap, gatePos)
for move in moves:
    movedBoat = -1 # reset the boat check
    score -= 1
    if move is "U":
        if validMove(gameMap, manRow - 1, manCol, manRow, manCol):
            hyCount, state, movedBoat = makeMove(gameMap, manRow - 1, manCol, hyCount, 
                                                            gatePos, boatsLoc, movedBoat)
            gameMap[manRow][manCol] = ' '
            manRow -= 1

    elif move is "D":
        if validMove(gameMap, manRow + 1, manCol, manRow, manCol):
            hyCount, state, movedBoat = makeMove(gameMap, manRow + 1, manCol, hyCount,
                                                            gatePos, boatsLoc, movedBoat)
            gameMap[manRow][manCol] = ' '
            manRow += 1

    elif move is "L":
        if validMove(gameMap, manRow, manCol - 1, manRow, manCol):
            hyCount, state, movedBoat = makeMove(gameMap, manRow, manCol - 1, hyCount,
                                                            gatePos, boatsLoc, movedBoat)
            gameMap[manRow][manCol] = ' '
            manCol -= 1

    elif move is "R":
        if validMove(gameMap, manRow, manCol + 1, manRow, manCol):
            hyCount, state, movedBoat = makeMove(gameMap, manRow, manCol + 1, hyCount,
                                                            gatePos, boatsLoc, movedBoat)
            gameMap[manRow][manCol] = ' '
            manCol += 1

    elif move is "A":
        score += 1               # "refund" this moves point loss
        stdout.write(f"quit\n")
        multiplier = 2
        break

    state = updateBoats(gameMap, boatsLoc, width, state, movedBoat)
    printBoard(gameMap)
    if state is not 0:
        break
    

if state is 1:
    stdout.write("win\n")
    multiplier = 3
elif state is -1:
    stdout.write("injured\n")
score = score + (25 * hyCount * multiplier)
stdout.write(f"score:{score}\n")