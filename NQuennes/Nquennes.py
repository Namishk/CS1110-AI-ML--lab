'''


check in row, col, diagonal

recursively place queens in board
'''


N = int(input("Enter Size of board : "))
# N = 4

#empty chess board
# board = [
    # ["0", "0", "0", "0", "0", "0", "0", "0"],
    # ["0", "0", "0", "0", "0", "0", "0", "0"],
    # ["0", "0", "0", "0", "0", "0", "0", "0"],
    # ["0", "0", "0", "0", "0", "0", "0", "0"],
    # ["0", "0", "0", "0", "0", "0", "0", "0"],
    # ["0", "0", "0", "0", "0", "0", "0", "0"],
    # ["0", "0", "0", "0", "0", "0", "0", "0"],
    # ["0", "0", "0", "0", "0", "0", "0", "0"],
# ]

board = [["0" for i in range(N)] for j in range(N)]

RTLarr = [0]*(2*N-1)
LTRarr = [0]*(2*N-1)

def printBoard(board):

    for i in board:
        for j in i:
            if(j == "1"):
                print("#", end=" ")
            else: print("0", end=" ")
        print()



def check(board, row, col):
    
    #chacking in row

    for i in board[row]:
        if(i == "1"):
            return False


    #chacking in  col
    rowCounter = 0
    for i in board:
        if((i[col] == "1")  & (rowCounter != row)):
            return False
        rowCounter+=1
    

    psudoRTL = row+col
    psudoLTR = row-col
    
    if(LTRarr[psudoLTR + N - 1] == 1 | RTLarr[psudoRTL] == 1): return False


    return True


def solver(board, startRow, qCount):
    if(qCount > N):
        printBoard(board)
        return True
        
    for i in range(N):
        if(check(board, startRow, i)):
            board[startRow][i] = "1"
            LTRarr[startRow - i + N -1] = RTLarr[startRow + i] = 1
            if(solver(board, startRow+1,qCount+1)):
                return True
            board[startRow][i] = "0"
            LTRarr[startRow - i + N -1] = RTLarr[startRow + i] = 0
    # printBoard(board)
    return False

solver(board, 0, 1)
# print(board[1][2])
# check(board, 1, 2)
