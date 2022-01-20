# Game Boarrd
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if Game is still going
gameStillGoing = True

# Who won or tie?
winner = None

# whose turn is it
currentPlayer = "X"


def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def playGame():
    # Display initial board
    displayBoard()
    # while the game is still going
    while gameStillGoing:

        # handle a single turn of an arbitrary player
        handleTurn(currentPlayer)

        # check if the game is ended
        checkIfGameOver()

        # flip to other player
        flipPlayer()
    # The game if ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# handle a single turn of an arbitrary player


def handleTurn(player):
    print(player + "'s Turn.")
    position = input("Choose a position from 1 to 9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't there. Go again")

    board[position] = player
    displayBoard()


def checkIfGameOver():
    checkForWinner()
    checkIfTie()


def checkForWinner():
    global winner
    # check rows
    rowWinner = checkRows()
    # check columns
    columnWinner = checkColumns()
    # checks diagonals
    diagonalWinner = checkDiagonals()
    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        winner = None
    return


def checkRows():
    global gameStillGoing

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        gameStillGoing = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def checkColumns():
    global gameStillGoing
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        gameStillGoing = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return


def checkDiagonals():
    global gameStillGoing
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        gameStillGoing = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    return


def checkIfTie():
    global gameStillGoing
    if "-" not in board:
        gameStillGoing = False
    return


def flipPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    return


playGame()
