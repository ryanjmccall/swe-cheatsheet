def quickselect(array, k):
    # Ave: O(n) O(1)
    # Worst: O(n^2) O(1)
    k_idx = k - 1

    def helper(start_idx, end_idx):
        while start_idx <= end_idx:
            right = partition(start_idx, end_idx, array)
            if right == k_idx:
                return array[k_idx]
            elif right < k_idx:
                start_idx = right + 1
            else:
                end_idx = right - 1

    return helper(0, len(array) - 1)


def partition(start, end, array):
    # (pivot) (left) ............ (right)
    pivot, left, right = start, start + 1, end
    while left <= right:
        if array[right] < array[pivot] < array[left]:
            array[left], array[right] = array[right], array[left]
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    array[pivot], array[right] = array[right], array[pivot]
    return right



def swap(a_idx, b_idx, array):
    array[a_idx], array[b_idx] = array[b_idx], array[a_idx]


print(quickselect(array=[8, 5, 2, 9, 7, 6, 3], k=3))