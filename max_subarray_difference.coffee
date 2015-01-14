###
Maximum Subarray Difference
Given an array, find two disjoint contiguous subarrays such that the
difference between their sums is a maximum.

Using an adaptation of the maximum subarray problem (Kadane's algorithm),
we find the minimum and maximum subarrays left and right of every index.
We cache the results, trading O(n) space to achieve O(n) time.
###

max_subarray_difference = (arr) ->
    size = arr.length

    maxLeft = (0 for _ in [0..size])
    minLeft = (0 for _ in [0..size])
    for i in [0...size]
        maxLeft[i+1] = Math.max(0, maxLeft[i] + arr[i])
        minLeft[i+1] = Math.min(0, minLeft[i] + arr[i])

    maxRight = (0 for _ in [0..size])
    minRight = (0 for _ in [0..size])
    for i in [size-1..0]
        maxRight[i] = Math.max(0, maxRight[i+1] + arr[i])
        minRight[i] = Math.min(0, minRight[i+1] + arr[i])

    difference = []
    for i in [0...size]
        difference.push(Math.max(maxLeft[i] - minRight[i], maxRight[i] - minLeft[i]))
    return Math.max.apply(Math, difference)

test_cases = [
    [[4, 3, -1, -4, 1, -5, 8, 4, -2, 3, -1], 22],
    [[-1, 3, 2, 5, 2, -5, 1, -4, -3, -1, 2], 24]
]

for [test_case, ans] in test_cases
    console.log(max_subarray_difference(test_case) == ans)
