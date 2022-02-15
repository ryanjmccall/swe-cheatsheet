


def bin_search(a: list, val: int) -> bool:
    i, j = 0, len(a) - 1
    while i <= j:
        mid = (i + j) // 2
        if a[mid] < val:
            i = mid + 1
        elif a[mid] > val:
            j = mid - 1
        else:
            return True

    return False



def search_matrix1(a: list, n: int) -> bool:
    # This solution is OK but requires extra code
    # better solution is to use a 1d pointer and translate to 2d
    if not a:
        return False

    i, j = 0, len(a) - 1
    while i < j:
        mid = (i + j) // 2
        row = a[mid]
        if row[-1] < n:
            i = mid + 1
        elif row[0] > n:
            j = mid - 1
        else:
            return bin_search(row, n)

    return False


def search_matrix(a, n):
    if not a:
        return False

    rows, cols = len(a), len(a[0])
    left, right = 0, rows * cols
    while left <= right:
        mid = (left + right) // 2
        if a[mid // cols][mid % cols] < n:
            left = mid + 1
        elif a[mid // cols][mid % cols] > n:
            right = mid - 1
        else:
            return True

    return False



# search a sorted matrix for a number
matrix = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31]
]
print(search_matrix(matrix, n=4))
print(search_matrix(matrix, n=10))


