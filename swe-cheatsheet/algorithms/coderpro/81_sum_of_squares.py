from math import sqrt


# def fewest_sum_of_squares(n, count=0) -> int:
#     if n == 0:
#         return count
#
#     sqr = int(sqrt(n))
#     print('use', sqr)
#     remain = n - sqr * sqr
#     return fewest_sum_of_squares(remain, count + 1)
#
# print(fewest_sum_of_squares(57))
# print(fewest_sum_of_squares(30))
# print(fewest_sum_of_squares(12))

# time: O(n Sqrt(n))
# space: O(n)

def square_sums(n):
    i = 1
    squares = []
    while i*i <= n:
        squares.append(i*i)
        i += 1

    min_sums = [0] + [n] * n
    for i in range(n + 1):
        for s in squares:
            val = i + s
            # print(min_sums)
            if val < len(min_sums):
                min_sums[val] = min(min_sums[val], min_sums[i] + 1)
            else:
                break

    return min_sums[-1]


print(square_sums(13))  # 2
print(square_sums(52))  # 2
