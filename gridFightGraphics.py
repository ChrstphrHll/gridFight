import time
import sys
import random
from graphics import *

brk = "~~~~~~~~~~~~~~~"
numberOfTrials = 1000
sleep = 0.0

def printGrid(grid):
    for element in grid:
        print(element)

def drawGrid(grid, win):
    n = len(grid)
    for rowb in range(n):
        for colb in range(n):
            row = rowb * 12
            col = colb * 12
            pt1 = Point(row + 2, col + 2)
            pt2 = Point(row + 12, col + 12)
            r = Rectangle(pt1, pt2)
            if grid[rowb][colb] == 1:
                r.setFill("blue")
            elif grid[rowb][colb] == 2:
                r.setFill("red")
            r.draw(win)

def updateGrid(grid, win, cord, marker):
    row = cord[0] * 12
    col = cord[1] * 12
    pt1 = Point(row + 2, col + 2)
    pt2 = Point(row + 12, col + 12)
    r = Rectangle(pt1, pt2)
    if marker == 1:
        r.setFill("blue")
    elif marker == 2:
        r.setFill("red")
    r.draw(win)


def makeNxNGrid(n):
    grid = [0 for i in range(n)]
    for i in range(len(grid)):
        junk = [0 for i in range(n)]
        grid[i] = junk
    return grid

def fillGrid(grid, fillValue):
    for x in range(len(grid)):
        for y in range(len(grid)):
            grid[x][y] = fillValue

def copyGrid(grid):
    ret = []
    for element in grid:
        row = []
        for num in row:
            row.append(valueOf(num))
        ret.append(row)
    return ret

def checkValid(grid, row, col, marker, other):
    if row < 0 or col < 0 or row > (len(grid) - 1) or col > (len(grid[0]) - 1):
        return False
    if grid[row][col] != 0:
        return False
    if row + 1 < len(grid):
        if grid[row + 1][col] == other:
            return False
    if row - 1 > -1:
        if grid[row - 1][col] == other:
            return False
    if col + 1 < len(grid[0]):
        if grid[row][col + 1] == other:
            return False
    if col - 1 > -1:
        if grid[row][col - 1] == other:
            return False
    return True

def p1(grid, marker, other):
    attempts = 0
    while attempts < 10000:
        attempts += 1
        x = random.randint(0,len(grid)-1)
        y = random.randint(0,len(grid[0])-1)
        if checkValid(grid, x, y, marker, other):
            break
    return [x, y]

def p2(grid, marker, other):
    attempts = 0
    while attempts < 10000:
        attempts += 1
        x = random.randint(0,len(grid)-1)
        y = random.randint(0,len(grid[0])-1)
        if checkValid(grid, x, y, marker, other):
            break
    return [x, y]

def playGame():
    grid = makeNxNGrid(int(sys.argv[1]))
    n = len(grid)
    rect_Size = 12
    lent = n*rect_Size
    win = GraphWin("GridFight", lent+2, lent+2)
    drawGrid(grid, win)
    time.sleep(sleep)
    playerOne = True
    marker = 0
    other = 0

    while True:
        if playerOne:
            place = p1(grid, 1, 2)
            marker = 1
            other = 2
        else:
            place = p2(grid, 2, 1)
            marker = 2
            other = 1
        if not(checkValid(grid, place[0], place[1], marker, other)):
            break
        grid[place[0]][place[1]] = marker
        playerOne = not(playerOne)
        updateGrid(grid, win, place, marker)
        time.sleep(sleep)

    if playerOne:
        loser = "playerOne"
        winner = "playerTwo"
    else:
        winner = "playerOne"
        loser = "playerTwo"
    print(loser + " made an invalid move so " + winner + " wins!")
    y = win.getKey()
    win.close()
    return y


def playGameALot():
    grid = makeNxNGrid(int(sys.argv[1]))
    printGrid(grid)
    print(brk)
    time.sleep(1)
    playerOne = True
    marker = 0
    other = 0
    place = [0,0]
    turnIndex = 0
    loser = ""
    winner = ""
    p1wins = 0
    p2wins = 0

    for i in range(numberOfTrials):

        fillGrid(grid, 0)
        turnIndex = 0
        print("Game " + str(i) + " is beginning")

        while True:
            # print("It is turn " + str(turnIndex))
            if playerOne:
                place = p1(grid, 1, 2)
                marker = 1
                other = 2
            else:
                place = p2(grid, 2, 1)
                marker = 2
                other = 1
            # print("Player " + str(marker) + "'s turn has placed at [" + str(place[0]) + "," + str(place[1]) + "]")

            if not(checkValid(grid, place[0], place[1], marker, other)):
                break
            grid[place[0]][place[1]] = marker
            playerOne = not(playerOne)
            # printGrid(grid)
            # print(brk)
            turnIndex += 1
            time.sleep(0)

        # printGrid(grid)

        if playerOne:
            loser = "playerOne"
            winner = "playerTwo"
            p2wins += 1
        else:
            winner = "playerOne"
            loser = "playerTwo"
            p1wins += 1
        print(loser + " made an invalid move so " + winner + " wins!")

        if i % 2 == 0:
            playerOne = True
        else:
            playerOne = False

    print("Player 1 won " + str(p1wins) + " times, and Player 2 won " + str(p2wins) + " times.")
    print("Player 1 win rate: " + str(p1wins / numberOfTrials * 100) + "%")
    print("Player 2 win rate: " + str(p2wins / numberOfTrials * 100) + "%")

y = "y"
while y == "y":
    y = playGame()

#playGameALot()
