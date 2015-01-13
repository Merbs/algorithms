###
# Maximum Subarray Problem
# Given an array of numbers, find the contiguous subarray with the largest sum.
# If multiple subarrays have the same value, return the shortest subarray
# (the subarray with the least number of elements). If multiple subarrays are
# equally short, return the subarray starting at the earliest index.
# If there are no positive elements, return None. Otherwise, return the subarray.
###


# This is the basic version, which only returns the value of the max subarray,
# without returning the subarray itself.
def find_max_subarray_value(arr):
    max_ending_here, max_so_far = 0, 0
    for el in arr:
        max_ending_here = max(max_ending_here + el, 0)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far

test_cases = [
    ([3, 2, -6, 2, 9, -12, 10], 11), # [2, 9] is the maximum subarray
    ([-4, 12, 3, -5, 4, 3, -2], 17),     # [12, 3, -5, 4, 3] is max subarray
    ([1, 2, 4, 1, 5], 13),               # entire array is max subarray
    ([4, 5, -12, 9], 9)
]

for arr, ans in test_cases:
    assert find_max_subarray_value(arr) == ans

# This is a more extensive version, which finds the first subarray with the
# max value, and does not necessarily have the least number of elements.
def find_max_subarray(arr):
    max_ending_here, max_so_far = 0, 0
    start_index, end_index, curr_start_index = 0, 0, 0
    for i, el in enumerate(arr):
        if max_ending_here + el > 0:
            max_ending_here = max_ending_here + el
        else:
            max_ending_here = 0
            curr_start_index = i + 1
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start_index, end_index = curr_start_index, i
    if max_so_far == 0:
        return None
    return arr[start_index:end_index+1]

test_cases = [
    ([3, 2, -6, 2, 9, -12, 10], [2, 9]),
    ([-4, 12, 3, -5, 4, 3, -2], [12, 3, -5, 4, 3]),
    ([1, 2, 4, 1, 5], [1, 2, 4, 1, 5]),
    ([-4, -1], None),
    ([4, 5, -12, 9], [4, 5])            # Both [4, 5] and [9] are max subarrays
]

for arr, ans in test_cases:
    assert find_max_subarray(arr) == ans

# This finds the shortest subarray with the max value at the earliest index.
def find_shortest_max_subarray(arr):
    max_ending_here, max_so_far, length_of_max = 0, 0, len(arr)
    start_index, end_index, curr_start_index = 0, 0, 0
    for i, el in enumerate(arr):
        if max_ending_here + el > 0:
            max_ending_here = max_ending_here + el
        else:
            max_ending_here = 0
            curr_start_index = i + 1
        length_ending_here = i + 1 - curr_start_index
        if max_ending_here > max_so_far or \
          (max_ending_here == max_so_far and length_ending_here < length_of_max):
            max_so_far = max_ending_here
            length_of_max = length_ending_here
            start_index, end_index = curr_start_index, i
    if max_so_far == 0:
        return None
    return arr[start_index:end_index+1]

test_cases = [
    ([3, 2, -6, 2, 9, -12, 10], [2, 9]),
    ([-4, 12, 3, -5, 4, 3, -2], [12, 3, -5, 4, 3]),
    ([1, 2, 4, 1, 5], [1, 2, 4, 1, 5]),
    ([-4, -1], None),
    ([4, 5, -12, 9], [9]),              # [4, 5] is also max, but not shortest
    ([3, 4, -11, 2, 5], [3, 4])         # [3, 4] and [2, 5] are equal length
]

for arr, ans in test_cases:
    assert find_shortest_max_subarray(arr) == ans

print 'All is Good'
