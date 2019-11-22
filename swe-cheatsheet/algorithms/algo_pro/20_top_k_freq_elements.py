# LC 347 Top K Frequent Element
import heapq
import itertools
from collections import Counter, defaultdict

from typing import List


class Solution(object):

    def top_k_freq_heap(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        q = []
        for n, count in counter.items():
            heapq.heappush(q, (count, n))
            if len(q) > k:
                heapq.heappop(q)

        return [num for _, num in q]

    def top_k_freq_bucket(self, nums: List[int], k: int):
        bucket = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)
        for n, count in counter.items():
            bucket[count].append(n)

        result = []
        for position in range(len(nums), -1, -1):
            result.extend(bucket[position])
            if len(result) >= k:
                break

        return result[:k]

    def topKFrequent(self, nums, k):
        bucket = [[] for _ in nums]
        for num, freq in Counter(nums).items():
            bucket[-freq].append(num)
        return list(itertools.chain(*bucket))[:k]


print(Solution().topKFrequent(nums=[1,1,1,2,2,3], k=2))


# q = []
# heapq.heappush(q, (20, 8))
# heapq.heappush(q, (20, 9))
# while q:
#     print(heapq.heappop(q))
