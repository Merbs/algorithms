###
# Merge k Sorted Arrays
###

import heapq # I'm cheating b/c I don't want to implement a heap

def merge_k_sorted_arrays(*args):
    C = []
    heap = []
    arr_index = [0 for _ in range(len(args))]
    max_index = [len(arr) for arr in args]

    for arr_num, arr in enumerate(args):
        if arr:
            heapq.heappush(heap, (arr[0], arr_num))
            arr_index[arr_num] += 1

    while heap:
        value, arr_num = heapq.heappop(heap)
        C.append(value)

        if arr_index[arr_num] < max_index[arr_num]:
            value = args[arr_num][arr_index[arr_num]]
            heapq.heappush(heap, (value, arr_num))
            arr_index[arr_num] += 1

    return C

test_cases = [
    ([[1, 2, 4, 6], [2, 3, 5]], [1, 2, 2, 3, 4, 5, 6]),
    ([[1, 1, 2, 4], [3, 5, 6]], [1, 1, 2, 3, 4, 5, 6]),
    ([[1, 2, 3], [4, 5, 6], [2, 7]], [1, 2, 2, 3, 4, 5, 6, 7]),
    ([[2, 4], [1, 3, 5, 7], [6, 9], [8]], range(1, 10))
]

for test_case, ans in test_cases:
    assert merge_k_sorted_arrays(*test_case) == ans


print 'All is Good'
