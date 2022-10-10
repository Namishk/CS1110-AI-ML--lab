'''
knight tour -- cover all the positions

Possible moves for knight:
    1: uur
    2: uul
    3: ddr
    4: ddl
    5: rru
    6: rrd
    7: llu
    8: lld

Algo --
1. check avilable moves
2. if no moves avilable reset move and backtrack
3. play a move select next move recursively

end condition --- all blocks are filled ie. step 64 is executed..

'''


N = 8
board = [[-1 for i in range(N)] for j in range(N)]

#print the board
def printBoard(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()


#check if block is empty.
def check(board, row, col):
    if(row >= 0 and row < N and col >= 0 and col < N and board[row][col] == -1): return True
    return False

def solver(board, knights, row, col):
    
    if(knights == N*N):
        printBoard(board)
        # print(board)
        return True
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)] #list of possible moves;

    for i in moves:
        if(check(board, row + i[0], col + i[1])):
            board[row+i[0]][col+i[1]] = knights
            # print(board)
            if(solver(board, knights+1, row+i[0], col+i[1])):
                return True
            board[row+i[0]][col+i[1]] = -1
    # printBoard(board)
    # print()
    return False

board[0][0] = 0
solver(board, 1, 0, 0)
