def longestPeak(array):
    max_peak = 0
    increase_count = 0
    decrease_count = 0
    for i, v in enumerate(array[1:], start=1):
        is_increase = array[i - 1] < v
        is_decrease = array[i - 1] > v
        if increase_count and decrease_count:
            if is_decrease:
                decrease_count += 1
            else:
                max_peak = max(max_peak, increase_count + decrease_count + 1)
                decrease_count = 0
                increase_count = 1 if is_increase else 0

            continue

        if increase_count and not decrease_count:
            if is_increase:
                increase_count += 1
            elif is_decrease:
                decrease_count += 1
            else:  # flat
                increase_count = 0
            continue

        increase_count += is_increase

    if decrease_count:
        max_peak = max(max_peak, increase_count + decrease_count + 1)
    return max_peak


print(longestPeak([5, 4, 3, 2, 1, 2, 10, 12]))

