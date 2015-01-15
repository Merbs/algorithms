###
# Symmetric Difference
# Given two sorted lists, return a list of elements not in the intersection.
###

def symmetric_difference_pythonic(A, B):
    return list(set(A) ^ set(B))

# O(n^2) approach
def symmetric_difference_n2(A, B):
    C = []
    for a in A:
        if a not in B:
            C.append(a)
    for b in B:
        if b not in A:
            C.append(b)
    return sorted(C)

def symmetric_difference(A, B):
    """Returns the elements in A and B that are not in the intersection

    Inputs A and B are sorted lists which may have duplicates
    """

    C = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        elif B[j] < A[i]:
            C.append(B[j])
            j += 1
        else: # A[i] == B[j]
            temp = A[i]
            while i < len(A) and A[i] == temp:
                i += 1
            while j < len(B) and B[j] == temp:
                j += 1
    if i < len(A):
        C += A[i:]
    if j < len(B):
        C += B[j:]

    return C

test_cases = [
    (([1, 2, 3, 4], [1, 3, 5]),      [2, 4, 5]),    # Typical case
    (([2, 3], [1, 3, 3, 3, 3]),         [1, 2]),    # Duplicates at end
    (([1, 2, 3, 4, 5], [2, 4]),      [1, 3, 5]),    # No elements from B in C
    (([1, 2, 3], [1, 2, 2, 3]),             [])     # SymDiff is []
]

for test_case, ans in test_cases:
    A, B = test_case
    assert symmetric_difference(A, B) == ans

print 'All is Good'
