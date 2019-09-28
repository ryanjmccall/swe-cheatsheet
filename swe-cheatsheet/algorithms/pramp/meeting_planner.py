def meeting_planner(slotsA: list, slotsB: list, dur: int) -> list:
    ptr_a = 0
    ptr_b = 0

    while ptr_a < len(slotsA) and ptr_b < len(slotsB):
        meeting_slot = find_meeting_slot(slotsA[ptr_a], slotsB[ptr_b], dur)
        if meeting_slot:
            return meeting_slot

        # advance ptrs
        start_a, end_a = slotsA[ptr_a]
        start_b, end_b = slotsB[ptr_b]
        if end_a < end_b:
            ptr_a += 1
        else:
            ptr_b += 1

    return []


def find_meeting_slot(slot_a: list, slot_b: list, dur: int) -> list:
    start_a, end_a = slot_a
    start_b, end_b = slot_b
    if start_a > start_b:
        # ensure start a always <= start b
        start_a, end_a = slot_b
        start_b, end_b = slot_a

        # | |
        #  |               |

    if start_b < end_a:
        # have overlap
        actual_diff = end_a - start_b
        if actual_diff >= dur:
            end_slot = min(actual_diff, dur)
            return [start_b, end_slot]

    return []

