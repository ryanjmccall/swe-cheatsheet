



def partition(a: list, k: int):
    left = 0  # end of values less than K
    right = len(a) - 1  # start of values > k
    i = 0  # current value to be sorted
    while i <= right:
        print(left, i, right)
        print(a)
        if a[i] < k:
            a[i], a[left] = a[left], a[i]
            i += 1
            left += 1
        elif a[i] > k:
            a[i], a[right] = a[right], a[i]
            right -= 1
        else:
            i += 1

    return a

# def partition2(a: list, k: int):
#     i = 0
#     for j in range(1, len(a)):
#         if a[j] <= k:
#             i += 1
#             a[i], a[j] = a[j], a[i]
#
#     a[i+1], a[len(a) - 1] = a[len(a) - 1], a[i+1]
#     return a



# def partition(nums, k):
#   low = 0
#   high = len(nums) - 1
#
#   i = 0
#   while i <= high:
#     n = nums[i]
#     if n > k:
#       nums[high], nums[i] = nums[i], nums[high]
#       high -= 1
#     if n < k:
#       nums[low], nums[i] = nums[i], nums[low]
#       low += 1
#       i += 1
#     if n == k:
#       i += 1
#
#   return nums


print(partition([6, 3, 1, 5, 4, 2], 3))
# print(partition2([9, 9, 3, 1, 3], 3))
