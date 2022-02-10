from typing import List


def find_time(tasks: List[int], cooldown: int):
    starts = {}
    time = 0
    for task in tasks:
        if task in starts and time - starts[task] <= cooldown:
            time = cooldown + starts[task] + 1
        starts[task] = time
        print(starts)
        time += 1

    return time


print(find_time([1, 1, 2, 1], 2))
