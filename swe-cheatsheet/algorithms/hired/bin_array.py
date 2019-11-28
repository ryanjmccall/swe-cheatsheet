def solution(arr):
    def get_size(index: int) -> int:
        memo = dict()
        stack = [index]
        while stack:
            i = stack[-1]
            if i >= len(arr) or arr[i] == -1:
                memo[i] = 0
                stack.pop()
            else:
                left = 2 * i + 1  # could be pushed into call stack
                right = 2 * i + 2
                if right not in memo:
                    stack.append(right)

                if left not in memo:
                    stack.append(left)

                if left in memo and right in memo:
                    memo[i] = memo[left] + memo[right] + arr[i]
                    stack.pop()

        return memo[index]

    left_size = get_size(1)
    right_size = get_size(2)
    if left_size > right_size:
        return 'Left'
    elif right_size > left_size:
        return 'Right'
    else:
        return ''


assert solution([3, 6, 2, 9, -1, 10]) == 'Left'


# def get_size_recur(i: int) -> int:
#     if i >= len(arr):
#         return 0
#
#     if arr[i] == -1:
#         return 0
#
#     return get_size(2 * i + 1) + get_size(2 * i + 2) + arr[i]
