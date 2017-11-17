#Exam Scratch
import turtle

turtle.setworldcoordinates(-10,-10,190,190)

board = [
['U','U','U','U','U','U','U','U'],
['U','U','U','U','U','U','U','U'],
['U','U','U','U','U','U','U','U'],
['U','U','U','W','B','U','U','U'],
['U','U','U','B','W','U','U','U'],
['U','U','U','U','U','U','U','U'],
['U','U','U','U','U','U','U','U'],
['U','U','U','U','U','U','U','U']
]

def grid(t):
    t.shapesize(3.5)
    t.speed(0)
    t.shape("square")
    t.color('green')
    t.pu()
    x = 10
    y = 10
    while (x <= 200) and (y <= 200):
        if (x == 190) and (y == 167.5):
            x += 10
            y += 10
        if (x == 190) and (y != 167.5):
            x = 10
            y += 22.5
        else:
            t.goto(x,y)
            t.stamp()
            x += 22.5

def gridNum(t):
    t.pu()
    t.color('black')
    x = -5
    y = 7.5
    num = 7
    while y != 187.5:
        t.goto(x,y)
        t.write(num, True, align = "left", font=("Arial",12,"normal"))
        num -= 1
        y += 22.5
    if y == 187.5:
        x = 7.5
        y = 180
        num = 0
        while x != 187.5:
            t.goto(x,y)
            t.write(num, True, align = "left", font=("Arial",12,"normal"))
            num += 1
            x += 22.5

'''def boardPos():
    boardMatrix = []
    for i in range(8):
        boardMatrix.append([0,1,2,3,4,5,6,7])
    fill = False
    x = 10
    y = 10
    row = 7
    col = 0
    while fill == False:
        if x == 167.5 and y != 167.5:
            boardMatrix[row][col] = x,y
            y += 22.5
            x = 10
            col = 0
            row -= 1
        if x == 167.5 and y == 167.5:
            boardMatrix[row][col] = x,y
            fill = True
        else:
            boardMatrix[row][col] = x,y
            x += 22.5
            col += 1
    return boardMatrix

def boardCol():
    boardMatrix = []
    row = 0
    col = 0
    fill = False
    for i in range(8):
        boardMatrix.append([0,1,2,3,4,5,6,7])
    while fill == False:
        if col == 7 and row != 7:
            boardMatrix[row][col] = 'U'
            col = 0
            row += 1
        if col == 7 and row == 7:
            boardMatrix[row][col] = 'U'
            fill = True
        else:
            boardMatrix[row][col] = 'U'
            col += 1
    return boardMatrix'''

def rowToY(row):
    y = 10 + (22.5 * (7 - row))
    return y

def colToX(col):
    x = 10 + (22.5 * col)
    return x

def neighbors(row,col):
    neighbors = []
    #Top and Bottom Border
    if row == 0:
        if col in range(1-7):
            neighbors.append([
            (row, col - 1),
            (row, col + 1),
            (row + 1, col - 1]),
            (row + 1, col),
            (row + 1, col + 1)
            ])
            return neighbors
        if col == 0:
            neighbors.append([
            (row, col + 1),
            (row + 1, col),
            (row + 1, col + 1)
            ])
            return neighbors
        if col == 7:
            neighbors.append([
            [row, col - 1],
            [row + 1, col],
            [row + 1, col - 1]
            ])
            return neighbors
    elif row == 7:
        if col in range(1-7):
            neighbors.append([
            [row, col - 1],
            [row, col + 1],
            [row - 1, col - 1],
            [row - 1, col],
            [row - 1, col + 1]
            ])
            return neighbors
        if col == 0:
            neighbors.append([
            [row, col + 1],
            [row - 1, col],
            [row - 1, col + 1]
            ])
            return neighbors
        if col == 7:
            neighbors.append([
            [row, col - 1],
            [row - 1, col],
            [row - 1, col - 1]
            ])
            return neighbors
    #Left and Right border
    elif col == 0:
        if row in range(1-7):
            neighbors.append([
            [row - 1, col],
            [row + 1, col],
            [row - 1, col + 1],
            [row, col + 1],
            [row + 1, col + 1]
            ])
            return neighbors
        if row == 0:
            neighbors.append([
            [row, col + 1],
            [row + 1, col],
            [row + 1, col + 1]
            ])
            return neighbors
        if row == 7:
            neighbors.append([
            [row, col - 1],
            [row + 1, col],
            [row + 1, col - 1]
            ])
            return neighbors
    elif col == 7:
        if row in range(1-6):
            neighbors.append([
            [row - 1, col],
            [row + 1, col],
            [row - 1, col - 1],
            [row, col - 1],
            [row + 1, col - 1]
            ])
            return neighbors
        if row == 0:
            neighbors.append([
            [row, col + 1],
            [row - 1, col],
            [row - 1, col + 1]
            ])
            return neighbors
        if row == 7:
            neighbors.append([
            [row, col - 1],
            [row - 1, col],
            [row - 1, col - 1]
            ])
            return neighbors
    eif row in range(1,7) and col in range(1,7):
        neighbors.append([
        [row-1, col-1],
        [row-1, col],
        [row-1, col+1],
        [row, col -1],
        [row,col +1],
        [row+1, col-1],
        [row+1, col],
        [row+1, col+1]
        ])
        return neighbors



def isValidMove(brd, row, col, color):
    if brd[row][col] == color:
        return False
    else:
        return True

def makeValidMove(t, brd, row, col, color):
    brd[row][col] = color
    col = colToX(col)
    row = rowToY(row)
    if color == 'W':
        t.color('white')
        t.shape('circle')
        t.goto(col,row)
        t.stamp()
    if color == 'B':
        t.color('black')
        t.shape('circle')
        t.goto(col,row)
        t.stamp()

def checkBoard(t,brd):
    row = 0
    col = 0
    while row <= 7 and col <= 8:
        if col == 8:
            col = 0
            row += 1
        elif brd[row][col] == 'W':
            makeValidMove(t, board, row, col, 'W')
            col += 1
        elif brd[row][col] == 'B':
            makeValidMove(t, board, row, col, 'B')
            col += 1
        elif brd[row][col] == 'U':
            col += 1



'''def main():
    t = turtle.Turtle()
    grid(t)
    gridNum(t)
    done = False
    checkBoard(t, board)
    while done == False:
        row = int(turtle.textinput("","Enter a row number: "))
        col = int(turtle.textinput("","Enter a col number: "))
        player = turtle.textinput("","Enter a color W or B: ")
        user_done = turtle.textinput("","Done? y or n: ")
        move = isValidMove(board,row,col)
        if move == True:
            makeValidMove(t, board,row,col,player)
        if move == False:
            print("Not a valid move")
        if user_done == 'y':
            done == True

if __name__ == "__main__":
    main()'''
