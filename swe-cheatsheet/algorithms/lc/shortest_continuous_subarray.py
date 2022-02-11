def min_window_n2(unique: set, array: list):
    indices = dict()
    max_left = 0
    max_right = len(array) - 1
    smallest_size = len(array)
    for i, v in enumerate(array):
        if v in unique:
            indices[v] = i
            if len(indices) == len(unique):
                left = len(array) - 1
                right = 0

                for index in indices.values():
                    left = min(left, index)
                    right = max(right, index)

                if right - left < smallest_size:
                    smallest_size = right - left
                    max_left, max_right = left, right

    return array[max_left: max_right+1]


from collections import Counter, defaultdict


def min_window(s: list, t: set):
    if not s or not t:
        return []

    target_counts = Counter(t)
    window_counts = defaultdict(int)
    targets_in_window = 0
    left = 0
    min_len, min_left, min_right = float('inf'), None, None
    for right, rc in enumerate(s):
        window_counts[rc] += 1
        if rc in target_counts and target_counts[rc] == window_counts[rc]:
            targets_in_window += 1

        while left <= right and targets_in_window == len(target_counts):
            if right - left + 1 < min_len:
                min_len, min_left, min_right = right - left + 1, left, right

            lc = s[left]  # update window to remove left char
            window_counts[lc] -= 1
            if lc in target_counts and window_counts[lc] < target_counts[lc]:
                targets_in_window -= 1

            left += 1

    return [] if min_len == float('inf') else s[min_left: min_right+1]


print(min_window([1, 2, 2, -5, -4, 0, 1, 1, 2, 2, 0, 3, 3], {1, 3, 2}))
