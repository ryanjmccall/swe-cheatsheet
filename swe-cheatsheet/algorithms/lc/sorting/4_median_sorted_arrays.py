from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None
        merged = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged += nums1[i:] or nums2[j:]
        mid = len(merged) // 2
        if len(merged) % 2:
            return merged[mid]
        return (merged[mid] + merged[mid + 1]) / 2


print(Solution().findMedianSortedArrays(nums1=[2], nums2=[1, 3]))
