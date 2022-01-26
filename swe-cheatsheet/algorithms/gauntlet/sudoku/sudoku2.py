board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(bo):
    # checkpoint
    row, col = find_empty(bo)
    if row is None and col is None:
        return True

    for val in range(1, 10):
        if valid(bo, val, (row, col)):
            bo[row][col] = val

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = (pos[1] // 3) * 3
    box_y = (pos[0] // 3) * 3

    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(b):
    return '\n'.join(' '.join(str(v) for v in row) for row in b) + '\n'


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j

    return None, None

print(print_board(board))
solve(board)
print(print_board(board))

assert board == [[7, 8, 5, 4, 3, 9, 1, 2, 6],
[6, 1, 2, 8, 7, 5, 3, 4, 9],
[4, 9, 3, 6, 2, 1, 5, 7, 8],
[8, 5, 7, 9, 4, 3, 2, 6, 1],
[2, 6, 1, 7, 5, 8, 9, 3, 4],
[9, 3, 4, 1, 6, 2, 7, 8, 5],
[5, 7, 8, 3, 9, 4, 6, 1, 2],
[1, 2, 6, 5, 8, 7, 4, 9, 3],
[3, 4, 9, 2, 1, 6, 8, 5, 7]]