from typing import Tuple, List


class Solution(object):
    def can_fulfill(self, meetings: List[Tuple[int, int]]) -> bool:
        if not meetings: return True
        meetings.sort()
        start, end = meetings[0]
        for s, e in meetings[1:]:
            if s < end:
                return False
            start, end = s, e
        return True

    def doctors_to_fulfill(self, meetings) -> int:
        if not meetings: return True
        meetings.sort()
        doctors = 0
        to_cover = list(range(1, len(meetings)))
        while to_cover:
            remaining = []
            for i in to_cover:
                _, prev_end = meetings[i - 1]
                cur_start, _ = meetings[i]
                if cur_start < prev_end:
                    remaining.append(i)

            to_cover = remaining
            doctors += 1

        return doctors

    def minMeetingRooms(self, intervals):
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        e = 0
        rooms = 0
        for start in starts:
            end = ends[e]
            if start < end:
                rooms += 1
            else:
                e += 1
        return rooms


def test():
    # m = [(3, 4), (1, 2), (3.5, 4), (3, 3.5)]
    # print(Solution().can_fulfill(m))
    # m = [(1, 2), (2, 3), (3, 4)]
    # print(Solution().can_fulfill(m))

    m = [(1, 2), (3, 4), (3.5, 4)]
    print(Solution().minMeetingRooms(m))


test()
