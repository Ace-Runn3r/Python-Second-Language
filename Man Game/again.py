# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Save the Manatees (Again)

import pygame
from sys import (stdin, stdout, argv)
from urllib.request import urlopen

image = {
    '*' : pygame.image.load("boat.png"),
    '#' : pygame.image.load("coquina.png"),
    'G' : pygame.image.load("grate.png"),
    'M' : pygame.image.load("hugh.png"),
    'W' : pygame.image.load("injured.png"),
    'O' : pygame.image.load("open.png"),
    '.' : pygame.image.load("seagrass.png"),
    ' ' : pygame.image.load("water.png"),
    '\\' : pygame.image.load("hyacinth.png")
}

def buildboard(mapData):
    hyCount = 0
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
            elif element is "\\":
                hyCount += 1
            elif element is ("G" or "O"):
                gatePos = index
    
            index += 1

    return gameMap, maxWidth, manateePos, gatePos, boats, hyCount

def printBoard(gameMap, screen, score, hyCount, history, width, height):
    screen.fill(0)

    row = len(gameMap)
    col = len(gameMap[0])

    for r in range(row):
        for c in range(col):
            screen.blit(image[gameMap[r][c]], (c * 48, r * 48))

    scoretext = deafont.render("Score: " + str(score), True, (255,255,255))
    screen.blit(scoretext, (0, row * 48 + 2))
    hyleft = deafont.render("Remaining Hyacinths: " + str(hyCount), True, (255,255,255))
    screen.blit(hyleft, (0, row * 48 + 26))
    pastMoves = deafont.render("History: " + ''.join(history[::-1]), True, (255,255,255))
    screen.blit(pastMoves, (100, row * 48 + 2))

    pygame.display.flip()

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

def makeMove(gameMap, row, col, eatenHy, gatePos, boatsLoc, movedBoat, hyCount):
    gameState = 0 # 0 = continue; 1 = win; -1 = injured
    value = gameMap[row][col]

    if value is '\\':
        eatenHy += 1
        gameMap[row][col] = '_' # have to remove hy for check
        hyCount -= 1
        if hyCount is 0:
            gameMap[gatePos // width][gatePos % width] = 'O'

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
    return eatenHy, gameState, movedBoat, hyCount

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

gameMap, width, manateePos, gatePos, boatsLoc, hyCount = buildboard(mapData)
history = []
score = 0
height = len(gameMap)

pygame.init()
deafont = pygame.font.Font(None, 24)
screenWidth = width * 48
screenHeight = height * 48 + 48
screen = pygame.display.set_mode((screenWidth, screenHeight))

printBoard(gameMap, screen, score, hyCount, history, width, height)

manRow = manateePos // width
manCol = manateePos % width
movesCount, eatenHy, state, movedBoat = 0, 0, 0, -1
multiplier = 1

if hyCount is 0:
    gameMap[gatePos // width][gatePos % width] = 'O'

while True:
    movedBoat = -1 # reset the boat check
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == pygame.K_u:
            movesCount -= 1
            history.append('U')
            if validMove(gameMap, manRow - 1, manCol, manRow, manCol):
                eatenHy, state, movedBoat, hyCount = makeMove(gameMap, manRow - 1, manCol,
                                            eatenHy, gatePos, boatsLoc, movedBoat, hyCount)
                gameMap[manRow][manCol] = ' '
                manRow -= 1

        elif event.key == pygame.K_DOWN or event.key == pygame.K_d:
            movesCount -= 1
            history.append('D')
            if validMove(gameMap, manRow + 1, manCol, manRow, manCol):
                eatenHy, state, movedBoat, hyCount = makeMove(gameMap, manRow + 1, manCol,
                                            eatenHy, gatePos, boatsLoc, movedBoat, hyCount)
                gameMap[manRow][manCol] = ' '
                manRow += 1

        elif event.key == pygame.K_LEFT or event.key == pygame.K_l:
            movesCount -= 1
            history.append('L')
            if validMove(gameMap, manRow, manCol - 1, manRow, manCol):
                eatenHy, state, movedBoat, hyCount = makeMove(gameMap, manRow, manCol - 1,
                                            eatenHy, gatePos, boatsLoc, movedBoat, hyCount)
                gameMap[manRow][manCol] = ' '
                manCol -= 1

        elif event.key == pygame.K_RIGHT or event.key == pygame.K_r:
            movesCount -= 1
            history.append('R')
            if validMove(gameMap, manRow, manCol + 1, manRow, manCol):
                eatenHy, state, movedBoat, hyCount = makeMove(gameMap, manRow, manCol + 1,
                                            eatenHy, gatePos, boatsLoc, movedBoat, hyCount)
                gameMap[manRow][manCol] = ' '
                manCol += 1

        elif event.key == pygame.K_a:
            movesCount += 1               # "refund" this moves point loss
            multiplier = 2
            endText = "Quit"
            history.append('A')
            break
        
        elif event.key == pygame.K_SPACE or event.key == pygame.K_w:
            movesCount -= 1
            history.append('W')
                
        state = updateBoats(gameMap, boatsLoc, width, state, movedBoat)
        score = movesCount + (25 * eatenHy * multiplier)
        printBoard(gameMap, screen, score, hyCount, history, width, height)
    elif event.type == pygame.KEYUP:
        continue

    if state is not 0:
        break  

if state is 1:
    endText = "Win"
    multiplier = 3
elif state is -1:
    endText = "Injured"
score = movesCount + (25 * eatenHy * multiplier)

while True:
    printBoard(gameMap, screen, score, hyCount, history, width, height)

    final = deafont.render(endText, True, (255,255,255))
    screen.blit(final, (screenWidth - 60, screenHeight - 22))
    pygame.display.flip()

    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        pygame.quit()
        exit(0)
