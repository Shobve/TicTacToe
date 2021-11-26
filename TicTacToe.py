from graphics import *

count = 0
winner = None
currentPlayer = "X"

win = GraphWin("Tic Tac Toe", 500, 500)

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def main():
    drawUI()
    playGame()

def drawLine(win, width, position1, position2, colour):
    line = Line(position1, position2)
    line.setFill(colour)
    line.setWidth(width)
    line.draw(win)

def drawRectangle(win, position1, position2, colour, outline):
    rect = Rectangle(position1, position2)
    rect.setFill(colour)
    rect.setOutline(outline)
    rect.draw(win)

def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawText(win, position, text, colour, size):
    text = Text(position, text)
    text.setTextColor(colour)
    text.setSize(size)
    text.draw(win)

def drawUI():
    #background
    drawRectangle(win, Point(0, 0), Point(500, 500), "white", "white")

    #Title of game
    drawText(win, Point(250, 50), "Tic Tac Toe", "black", 20)

    #Box around board
    drawRectangle(win, Point(100, 100), Point(400, 400), "white", "black")

    #Displays game board
    drawLine(win, 4, Point(200, 400), Point(200, 100), "black")
    drawLine(win, 4, Point(300, 400), Point(300, 100), "black")
    drawLine(win, 4, Point(100, 300), Point(400, 300), "black")
    drawLine(win, 4, Point(100, 200), Point(400, 200), "black")

    #Restart button
    drawRectangle(win, Point(100, 450), Point(200, 475), "light grey", "black")

    #Restart button text
    drawText(win, Point(150, 463), "Restart", "black", 10)

    #Exit button
    drawRectangle(win, Point(300, 450), Point(400, 475), "light grey", "black")

    #Exit button text
    drawText(win, Point(350, 463), "Exit", "black", 10)

def drawO(centre):
    drawCircle(win, centre, 30, "black")
    drawCircle(win, centre, 28, "white")

def drawX(position1, position2, position3, position4):
    drawLine(win, 4, position1, position2, "black")
    drawLine(win, 4, position3, position4, "black")


def checkForWinner():
    global winner
    rowWinner = rowWin()
    columnWinner = columnWin()
    diagonalWinner = diagonalWin()

    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        winner = None

    if winner != None:
        drawText(win, Point(250, 420), (winner + " has won."), "black", 10)
        afterGame()

def checkForTie():
    if "-" not in board:
        drawText(win, Point(250, 420), "Game is a tie.", "black", 10)
        return True, afterGame()
    else:
        return False

def rowWin():
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        checkIfGameFinished = True
    if row1:
        drawLine(win, 4, Point(100, 150), Point(400, 150), "red")
        return board[0]
    if row2:
        drawLine(win, 4, Point(100, 250), Point(400, 250), "red")
        return board[3]
    if row3:
        drawLine(win, 4, Point(100, 350), Point(400, 350), "red")
        return board[6]
    else:
        return None

def columnWin():
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        checkIfGameFinished = True
    if column1:
        drawLine(win, 4, Point(150, 100), Point(150, 400), "red")
        return board[0]
    elif column2:
        drawLine(win, 4, Point(250, 100), Point(250, 400), "red")
        return board[1]
    elif column3:
        drawLine(win, 4, Point(350, 100), Point(350, 400), "red")
        return board[2]
    else:
        return None

def diagonalWin():
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:
        checkIfGameFinished = True
    if diagonal1:
        drawLine(win, 4, Point(100, 100), Point(400,400), "red")
        return board[0]
    elif diagonal2:
        drawLine(win, 4, Point(100, 400), Point(400,100), "red")
        return board[2]
    else:
        return None

def restart():
    global count
    global board
    global winner
    winner = None
    count = 0
    for i in range(9):
        board[i] = "-"
    drawUI()
    playGame()

def playGame():
    global count
    global currentPlayer
    global winner
    global board

    while count < 9 and winner == None:
            p = win.getMouse()
            pRow = (p.getX() - 100) // 100
            pColumn = (p.getY() - 100) // 100

            x = pRow * 100
            y = pColumn * 100

            #Converts the coordinate value of click to value in array e.g. clicking top left square = board[0], clicking middle square = board[4]
            i = int(pRow) + int(pColumn) + int(pColumn * 2)

            #changes player
            if (count % 2) == 0:
                currentPlayer = "X"
            else:
                currentPlayer = "O"

            if p.getX() > 100 and p.getX() < 400 and p.getY() > 100 and p.getY() < 400:
                if currentPlayer == "X" and board[i] == "-":
                    drawX(Point(x + 120, y + 120), Point(x + 180, y + 180), Point(x + 120, y + 180), Point(x + 180, y + 120))
                    count += 1
                    board[i] = currentPlayer
                elif currentPlayer == "O" and board[i] == "-":
                    drawO(Point(x + 150, y + 150))
                    count += 1
                    board[i] = currentPlayer

            elif (p.getX() > 100 and p.getX() < 200) and (p.getY() > 450 and p.getY() < 475):
                    restart()
                    print(board)
            elif (p.getX() > 300 and p.getX() < 400) and (p.getY() > 450 and p.getY() < 475):
                    win.close()
                    raise SystemExit()

            checkForWinner()
            checkForTie()

def afterGame():
    p=win.getMouse()
    if (p.getX() > 100 and p.getX() < 200) and (p.getY() > 450 and p.getY() < 475):
            restart()
            print(board)
    elif (p.getX() > 300 and p.getX() < 400) and (p.getY() > 450 and p.getY() < 475):
            win.close()
            raise SystemExit()
    else:
        drawRectangle(win, Point(10, 410), Point(490, 440), "white", "white")
        drawText(win, Point(250, 420), "Click [Restart] to play again or Click [Exit] to quit.", "black", 10)
        p=win.getMouse()
        if (p.getX() > 100 and p.getX() < 200) and (p.getY() > 450 and p.getY() < 475):
                restart()
                print(board)
        elif (p.getX() > 300 and p.getX() < 400) and (p.getY() > 450 and p.getY() < 475):
                win.close()
                raise SystemExit()
        else:
            afterGame()



main()