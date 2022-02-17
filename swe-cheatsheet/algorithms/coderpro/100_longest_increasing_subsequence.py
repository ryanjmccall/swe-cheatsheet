


def longest_increasing_subsequence(a: list) -> int:
    sub = [1] * len(a)
    for i in range(1, len(a)):
        for j in range(i):
            if a[j] < a[i]:
                sub[i] = max(sub[i], sub[j] + 1)

    return max(sub)


test = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3]
print(longest_increasing_subsequence(test))
