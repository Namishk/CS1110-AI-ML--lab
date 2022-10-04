N = 9


def printBoard(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()


def isValueAllowed(board, row, col, val):

    for x in range(9):
        if board[row][x] == val:
            return False

    for x in range(9):
        if board[x][col] == val:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == val:
                return False
    return True


def solver(board, row, col):

    if (row == N - 1 and col == N):
        return True

    if col == N:
        row += 1
        col = 0

    if board[row][col] > 0:
        return solver(board, row, col + 1)
    for i in range(1, N + 1, 1):

        if isValueAllowed(board, row, col, i):

            board[row][col] = i

            if solver(board, row, col + 1):
                return True

        board[row][col] = 0
    return False


board = [
    [3, 0, 0, 8, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 4, 1, 5, 0, 0, 8, 3, 0],
    [0, 2, 0, 0, 0, 1, 0, 0, 0],
    [8, 5, 0, 4, 0, 3, 0, 1, 7],
    [0, 0, 0, 7, 0, 0, 0, 2, 0],
    [0, 8, 5, 0, 0, 9, 7, 4, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 7, 0, 0, 6]
]

if (solver(board, 0, 0)):
    printBoard(board)
else:
    print("ERROR")
