def playGameALot():
    grid = makeNxNGrid(int(10))
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
