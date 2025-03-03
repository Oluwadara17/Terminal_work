import random

# create the board
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
currentPlayer ="X"
winner = None 
gameRuning = True


# printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("--------------")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("--------------")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | ")


# take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >=1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] =currentPlayer
    else:
        print("Ooops player is always in that spots!")


# check for the win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0] 
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[0] 
        return True
    if board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6] 
        return True


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0] 
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1] 
        return True
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2] 
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0] 
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2] 
        return True


def checktie(board):
    global gameRuning
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        gameRuning = False

def checkWin():
    if checkDiagonal(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")


#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "o"
    else:
        currentPlayer = "X"

# computer

def computer(board):
    while currentPlayer == "0":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "o"
            switchPlayer()


#check for win or tie again
while gameRuning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checktie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checktie