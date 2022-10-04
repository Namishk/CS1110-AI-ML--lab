from shutil import move


board = ["X", "X", "_",
         "_", "O", "_",
         "_", "O", "_"]

human = "O"
ai = "X"


def emptyIndexes(board):
    a = []
    for i in range(9):
        if (board[i] == "_"):
            a.append(i)
    return (a)


def winning(board, player):
    if (
        ((board[0] == player) & (board[1] == player) & (board[2] == player)) |
        ((board[3] == player) & (board[4] == player) & (board[5] == player)) |
        ((board[6] == player) & (board[7] == player) & (board[8] == player)) |
        ((board[0] == player) & (board[3] == player) & (board[6] == player)) |
        ((board[1] == player) & (board[4] == player) & (board[7] == player)) |
        ((board[2] == player) & (board[5] == player) & (board[8] == player)) |
        ((board[0] == player) & (board[4] == player) & (board[8] == player)) |
        ((board[2] == player) & (board[4] == player) & (board[6] == player))
    ):
        return True
    else:
        return False

# print(winning(board, ai))

def winner(board, ai, human):

    if(winning(board, ai)):
        return -10
    elif(winning(board, human)):
        return 10
    elif (len(emptyIndexes(board)) == 0):
        return 0
    else:
        return 1


def minmax(board, ai, human):
    
    avilable = emptyIndexes(board)

    print(avilable)
    moves = []

    for i in avilable:
        temp = board.copy()
        temp[i]  = ai
        # print(temp)
        
        moves.append(temp)

    print(moves)



minmax(board, ai, human)