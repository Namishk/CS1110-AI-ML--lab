ai, human = 'x', 'o'

def isMovesLeft(board) :

	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == '_') :
				return True
	return False

def evaluate(board) :

	for row in range(3) :	
		if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) :	
			if (board[row][0] == ai) :
				return 10
			elif (board[row][0] == human) :
				return -10

	for col in range(3) :
	
		if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) :
		
			if (board[0][col] == ai) :
				return 10
			elif (board[0][col] == human) :
				return -10

	if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
	
		if (board[0][0] == ai) :
			return 10
		elif (board[0][0] == human) :
			return -10

	if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) :
	
		if (board[0][2] == ai) :
			return 10
		elif (board[0][2] == human) :
			return -10

	return 0

def minimax(board, depth, isMax) :
	score = evaluate(board)

	if (score == 10) :
		return score

	if (score == -10) :
		return score

	if (isMovesLeft(board) == False) :
		return 0

	if (isMax) :	
		best = -100

		for i in range(3) :		
			for j in range(3) :
			
				if (board[i][j]=='_') :
				
					board[i][j] = ai

					best = max( best, minimax(board,
											depth + 1,
											not isMax) )

					board[i][j] = '_'
		return best

	else :
		best = 100

		for i in range(3) :		
			for j in range(3) :
			
				if (board[i][j] == '_') :
				
					board[i][j] = human

					best = min(best, minimax(board, depth + 1, not isMax))

					board[i][j] = '_'
		return best

def findBestMove(board):
	bestVal = -1000
	bestMove = (-1, -1)

	for i in range(3) :	
		for j in range(3) :
		
			if (board[i][j] == '_') :
			
				board[i][j] = ai

				moveVal = minimax(board, 0, False)

				board[i][j] = '_'

				if (moveVal > bestVal) :			
					bestMove = (i, j)
					bestVal = moveVal

	print("The value of the best Move is :", bestVal)
	print()
	return bestMove
# Driver code
board = [
	[ '_', '_', '_' ],
	[ '_', '_', '_' ],
	[ '_', '_', '_' ]
]

def printBoard(board):
    for i in board:
        print(i)

# ---------MAIN----------
print("-------------------------")
print("\tYOU ARE : o")
print("-------------------------")
print("\n")


while(True):
    printBoard(board)
    print("\n")

    print ("Enter row : ")
    row = int(input())
    print ("Enter column : ")
    col = int(input())
    print("\n")

    board[row][col] = human

    bestMove = findBestMove(board)
    if(bestMove[0] == -1 | bestMove[1] == -1):
        break
    board[bestMove[0]][bestMove[1]] = ai
    printBoard(board)
    print("\n")

