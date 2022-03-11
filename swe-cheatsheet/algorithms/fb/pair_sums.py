from collections import Counter


def tri(n):
    return int(n * (n + 1) / 2)


def numberOfWays(arr, k):
    val_counts = Counter(arr)
    pair_count = 0
    half = k / 2
    for val, val_count in val_counts.items():
        if val <= half:
            comp = k - val
            if comp in val_counts:
                if val != comp:
                    pair_count += max(val_count, val_counts[comp])
                else:
                    pair_count += tri(val_count - 1)

    return pair_count


print(numberOfWays([1, 2, 3, 4, 3], 6))