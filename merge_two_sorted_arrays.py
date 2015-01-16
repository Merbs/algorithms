###
# Merge Two Sorted Arrays
###

def merge_two_sorted_arrays(A, B):
    C = []
    i, j= 0, 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
        else: # A[i] == B[j]
            C.append(A[i])
            C.append(B[j])
            i += 1
            j += 1
    if i < len(A):
        C += A[i:]
    if j < len(B):
        C += B[j:]

    return C

test_cases = [
    (([1, 2, 4, 6], [2, 3, 5]), [1, 2, 2, 3, 4, 5, 6]),
    (([1, 1, 2, 4], [3, 5, 6]), [1, 1, 2, 3, 4, 5, 6])
]

for test_case, ans in test_cases:
    A, B = test_case
    assert merge_two_sorted_arrays(A, B) == ans


print 'All is Good'
