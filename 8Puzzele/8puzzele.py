'''
Avilable moves:
Left, right, up, down

functions:
    1> checker --> checks if the given move is valid
    2> manhatton --> returns manhatten distance of current state
    3> solver --> main solver function that calls recursion to solve using Best First Search
    4>findPos --> finds position of given values
    5> validMoves --> gets list of valid moves
    6> makeMove --> makes a move to given coordinates.
    7> printSolSteps -- prints solution
'''
from itertools import count
import math

goalState = [
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  0]
]

initial = [
    [1,  2,  3],
    [4,  8,  5],
    [7,  0,  6]
]


movesStack : "list[int]" = []

def checker(current : "list[int]") -> bool:
    return current[0] > -1  and current[0] < 3 and current[1] > -1 and current[1] < 3


def findPos(val : int, board : "list[list[int]]") -> "list[int]":
    for i in range(3):
        for j in range(3):
            if (board[i][j] == val): return [i, j]


def manhatton(board : "list[list[int]]") -> int:
    distance:int = 0 

    for i in board:
        for n in i:
            if (n!= 0):
                cur = findPos(n, board)
                gs = findPos(n, goalState)

                distance += abs(cur[0] - gs[0]) + abs(cur[1] - gs[1])
    
    return distance


def validMoves(board : "list[list[int]]") -> "list[list[int]]" :
    moves = []
    currpos = findPos(0, board)
    row, col = currpos[0], currpos[1]

    #move up
    _row, _col = row,  col - 1
    if(checker([_row, _col])):
        moves.append([_row, _col])

    #move down
    _row, _col = row,  col + 1
    if(checker([_row, _col])):
        moves.append([_row, _col])

    #move left
    _row, _col = row - 1,  col
    if(checker([_row, _col])):
        moves.append([_row, _col])

    #move down
    _row, _col = row + 1,  col
    if(checker([_row, _col])):
        moves.append([_row, _col])


    return moves


def makeMove(board:"list[list[int]]", move:list[int], curr:list[int]) -> "list[list[int]]":

    board[move[0]][move[1]], board[curr[0]][curr[1]] = board[curr[0]][curr[1]], board[move[0]][move[1]]

    return board


def solver(board: "list[list[int]]") -> bool:

    currh = manhatton(board)

    if (currh == 0): return True
    avilableMoves = validMoves(board)
    
    curPos = findPos(0, board)


    bestMove = [-1, -1]
    m = math.inf

    for i in avilableMoves:
        _board = makeMove(board, i, curPos)

        _m = manhatton(_board)

        if _m < m:
            m = _m
            bestMove = i

        makeMove(board, curPos, i)
        
    board = makeMove(board, bestMove, curPos)
    movesStack.append(board)
    # print(board)
    solver(board)

def print2DList(lis : list[list[int]]):
    for i in lis:
        for j in i:
            print(j, end=" ")
        print()

def printSolSteps(solution : "list[list[list[int]]]") :

    print("\t~--8 puzzele solution--~\t")
    print("initial State : ")
    print2DList(initial)

    print("\ngoal State : ")
    print2DList(goalState)

    print("\nSOLUTION : \n")
    count = 1
    for i in solution:
        print("STEP : ", count)
        count+=1
        print2DList(i)
        print()


solver(initial)

printSolSteps(movesStack)


