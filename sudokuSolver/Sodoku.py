import numpy as np

'''
Board size : 9x9

Grid sixe : 3x3
w
value 0 => empty

Rules:
    Row/Column/Grid not contains more than one instance of 1 - 9

Method:
    1) for each value check numbers present in row, column and grid, and place one of the numbers not present in that place,
    2) using backtrack check each avilable case.
'''

board = np.array([
    [3, 0, 0, 8, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 4, 1, 5, 0, 0, 8, 3, 0],
    [0, 2, 0, 0, 0, 1, 0, 0, 0],
    [8, 5, 0, 4, 0, 3, 0, 1, 7],
    [0, 0, 0, 7, 0, 0, 0, 2, 0],
    [0, 8, 5, 0, 0, 9, 7, 4, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 7, 0, 0, 6]
])


def findStartRow(currentRow):
    return (currentRow % 3) - currentRow


def findStartCol(currentCol):
    return (currentCol % 3) - currentCol


def printBoard(sodukuBoard):

    # print board
    for i in sodukuBoard:
        for j in i:
            print(j, end=" ")
        print()


def isValueAllowed(sodukuBoard, sRow, sCol, val):

    startCol = findStartCol(sCol)
    startRow = findStartRow(sRow)
    # valuesUsed = set()

    # add row elements

    for i in sodukuBoard[sRow]:
        if i == val:return False

    # add col elements

    for i in sodukuBoard:
        if i[sCol] == val:return False

    # add grid elements

    for i in range(3):
        for j in range(3):
            if sodukuBoard[startRow + i][startCol + j] == val: return False

    return True
    # val = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    # return (val.difference(valuesUsed))


def solver(sodukuBoard, row, col):
    # Solves Sodoku

    # Check if the board is complete
    if (row == 8 & col == 9):
        return True

    # if end of row is reached
    if (col == 9):
        row += 1
        col = 0

    # check if it is already filled
    if (sodukuBoard[row][col] > 0):
        return solver(sodukuBoard, row, col+1)

    # get set of all the valid values.

    # if(len(avilableValues) == 0):
    # return False

    for i in range(1, 10):
        if isValueAllowed(sodukuBoard, row, col, i):
            sodukuBoard[row][col] = i
            # print(sodukuBoard)

            if(solver(board, row, col+1)):
                return True
            
        sodukuBoard[row][col] = 0
    
    return False

printBoard(board)
if solver(board, 0, 0):
    printBoard(board)
else:
    print("ERROR")
