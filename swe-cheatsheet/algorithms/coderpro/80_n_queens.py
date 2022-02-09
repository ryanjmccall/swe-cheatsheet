
EMPTY = '_'
QUEEN = 'Q'


def add_queens(board, row: int, col: int, n: int) -> bool:
    if n == 0:
        return True

    for i in range(row, len(board)):
        for j in range(col, len(board[0])):
            if can_add(board, i, j):
                board[i][j] = QUEEN
                if add_queens(board, i + 1, 0, n - 1):
                    return True

                board[i][j] = EMPTY

    return False


def can_add(board, row, col) -> bool:
    # row
    if any(c == QUEEN for c in board[row]):
        return False
    # column
    if any(r[col] == QUEEN for r in board):
        return False

    # forward diag, loop while in bounds, up-right, down-left
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == QUEEN:
            return False
        i -= 1
        j += 1

    i, j = row + 1, col - 1
    while i < len(board) and j >= 0:
        if board[i][j] == QUEEN:
            return False
        i += 1
        j -= 1

    # backward diag, loop while in bound, up-left, down-right
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == QUEEN:
            return False
        i -= 1
        j -= 1

    i, j = row + 1, col + 1
    while i < len(board) and j < len(board):
        if board[i][j] == QUEEN:
            return False
        i += 1
        j += 1

    return True


def main():
    # TODO: replace with boolean arrays for col, row, asc_diag, desc_diag
    n = 8
    board = [[EMPTY] * n for _ in range(n)]
    res = add_queens(board, 0, 3, n)
    print('can add:', res)
    print('\n'.join(''.join(r) for r in board))


if __name__ == '__main__':
    main()
