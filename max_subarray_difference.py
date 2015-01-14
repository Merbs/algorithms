###
# Maximum Subarray Difference
# Given an array, find two disjoint contiguous subarrays such that the
# difference between their sums is a maximum.
###

def max_subarray_difference(lst):
    """Finds the maximum difference between two disjoint contiguous subarrays

    Using an adaptation of the maximum subarray problem (Kadane's algorithm),
    we find the minimum and maximum subarrays left and right of every index.
    We cache the results, trading O(n) space to achieve O(n) time.

    """
    size = len(lst) + 1

    maxLeft = [0 for _ in range(size)]
    minLeft = [0 for _ in range(size)]
    for i in range(size-1):
        maxLeft[i+1] = max(0, maxLeft[i] + lst[i])
        minLeft[i+1] = min(0, minLeft[i] + lst[i])

    maxRight = [0 for _ in range(size)]
    minRight = [0 for _ in range(size)]
    for i in reversed(range(size-1)):
        maxRight[i] = max(0, maxRight[i+1] + lst[i])
        minRight[i] = min(0, minRight[i+1] + lst[i])

    difference = []
    for i in range(size):
        difference.append(max(maxLeft[i] - minRight[i], maxRight[i] - minLeft[i]))

    return max(difference)

test_cases = [
    ([4, 3, -1, -4, 1, -5, 8, 4, -2, 3, -1], 22),
    ([-1, 3, 2, 5, 2, -5, 1, -4, -3, -1, 2], 24)
]

for test_case, ans in test_cases:
    assert max_subarray_difference(test_case) == ans
