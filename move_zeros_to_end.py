###
# Move Zeros to End
# Given an array of numbers, move all the zeros to the end (constant space).
###


def move_zeros_to_end(arr):
    non_zeros = 0
    for i in xrange(len(arr)):
        if arr[i] != 0:
            arr[non_zeros] = arr[i]
            non_zeros += 1
    for i in xrange(non_zeros, len(arr)):
        arr[i] = 0

    return arr

test_cases = [
    ([1, 2, 0, 3, 0, 0, 4, 5, 0], [1, 2, 3, 4, 5, 0, 0, 0, 0]),
    ([0, 0, 0], [0, 0, 0]),
    ([1, 2, 3], [1, 2, 3])

]

for test_case, ans in test_cases:
    print move_zeros_to_end(test_case)
