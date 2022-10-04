size = int(input('enter size:'))

def init_matrix(matrix):
    for _ in range(size):
        row = []
        for __ in range(size):
            row.append(0)

        matrix.append(row)

    return matrix

def set_value(matrix, value, pos):
    x, y = pos[0], pos[1]
    matrix[x][y] = value

def print_matrix(matrix):
    for i in range(size):
        for j in range(size):
            if j == size - 1:
                print(matrix[i][j])
            else:
                print(matrix[i][j], end="   |   ")
        print('--------' * size)

    print("\n")

def magicSquare():
    counter = 1

    row = 0
    col = int(size/2)

    matrix = init_matrix([]) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    print('insert: 1')
    set_value(matrix, counter, [row, col])

    print_matrix(matrix)

    while counter != size * size:

        # up instruction
        x = (row - 1) % size # -1 up

        # right instruction
        y = (col + 1) % size # +1 right

        counter += 1

        if (matrix[x][y] == 0):
            row = x
            col = y

            set_value(matrix, counter, [x, y])
        else:
            x = (row + 1) % size
            #down
            row = x
            set_value(matrix, counter, [x, col])
        
        print('insert:', counter)
        print_matrix(matrix)


magicSquare()
