import collections
import heapq
from typing import List
from itertools import chain

_DUM = []
class Solution:
    def minMeetingRooms_(self, intervals: List[List[int]]) -> int:
        max_rooms = 0
        cur_rooms = 0  # current number of rooms required
        ends_to_count = collections.defaultdict(int)  # endtime of current mtgs to count of meetings
        mtgs = collections.defaultdict(list)  # all meetings
        for start, end in intervals:
            mtgs[start].append(end)

        times = sorted(chain.from_iterable(intervals))
        for t in times:
            for end in mtgs.get(t, _DUM):
                # start a meeting
                ends_to_count[end] += 1
                cur_rooms += 1

            # end all meetings ending at t
            cur_rooms -= ends_to_count[t]
            max_rooms = max(max_rooms, cur_rooms)

        return max_rooms

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])
        ends = [intervals[0][1]]  # min heap will maintain earliest meeting end
        for s, e in intervals[1:]:
            if ends[0] <= s:
                # earliest end has passed and meeting room has been freed
                # how do we know multiple rooms haven't been freed up?
                heapq.heappop(ends)
            heapq.heappush(ends, e)  # add another ongoing meeting
        return len(ends)


print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
