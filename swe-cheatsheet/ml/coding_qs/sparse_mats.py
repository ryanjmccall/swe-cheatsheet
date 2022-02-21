def sparse_matrix_multiplication(matrix_a, matrix_b):
    if not matrix_a or not matrix_b:
        return [[]]

    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
    if cols_a != rows_b:
        return [[]]

    sparse_a = as_sparse(matrix_a)
    sparse_b = as_sparse(matrix_b)
    res = [[0] * cols_b for _ in range(rows_a)]
    for i, k in sparse_a:
        for j in range(cols_b):
            if (k, j) in sparse_b:
                res[i][j] += sparse_a[(i, k)] * sparse_b[(k, j)]
    return res


def as_sparse(m) -> dict:
    return {(i, j): m[i][j]
            for i, r in enumerate(m)
            for j, v in enumerate(r)}