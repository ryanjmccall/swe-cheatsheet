#
# Your previous Plain Text content is preserved below:
#
# Imagine we're given the calendars for all the people at the company.  We represent a meeting in the calendar as (start_time, end_time) where the times range from 0 to 24 and times are decimals.  start_time is inclusive and end_time is exclusive
#
# Sally: [(8, 12), (14, 15), (18, 19)]
# Tina: [(11.4, 12.5), (14.5, 16)]
# Kevin: [(10, 12), (12, 12.4), (18, 18.5)]
# Bob: [(0, 2), (22, 24)]
#
# Solve: Determine which time intervals are all employees free (not in a meeting)
# [(2,8),(12.5,14),...]
#

available = [(0, 24)]

combinedSorted = [(0, 2), (8, 12), (10, 12), (11.4, 12.5), (12, 12.4), (14, 15)]
grouped = [(1, 2), (8, 12.5), (14, 15)]


def canCombineIntervals(t1, t2) -> bool:
    return t2[0] <= t1[1]


def allAvailable(schedules) -> list:
    if not schedules:
        return [(0, 24)]

    combined = list(sorted(v for sched in schedules.values for v in sched))

    groupedPtr = 0
    grouped = [combined[0]]
    for current in combined[1:]:
        prev = grouped[groupedPtr]
        if canCombineIntervals(prev, current):
            current = min(prev[0], current[0]), max(prev[1], current[1])
            grouped[groupedPtr] = current
        else:
            grouped.append(current)
            groupedPtr += 1

    available = []
    prevBooked = grouped[0]

    if prevBooked[0] != 0:
        available.append((0, prevBooked[0]))

    for currentBooked in grouped[1:]:
        available.append((prevBooked[1], currentBooked[0]))
        prevBooked = currentBooked

    if grouped[-1][1] != 24:
        available.append((grouped[-1][1], 24))

    return available


DATA = {'Sally': [(8, 12), (14, 15), (18, 19)],
        'Tina': [(11.4, 12.5), (14.5, 16)],
        'Kevin': [(10, 12), (12, 12.4), (18, 18.5)],
        'Bob': [(0, 2), (22, 24)]}

DATA_2 = {'Sally': [(3, 4)]}

print(allAvailable(DATA_2))


