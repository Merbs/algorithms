###
Symmetric Difference
Given two sorted lists, return a list of elements not in the intersection.
###

# Returns the elements in A and B that are not in the intersection
# Inputs A and B are sorted lists which may have duplicates
symmetric_difference = (A, B) ->
    C = []
    i = 0
    j = 0
    while i < A.length and j < B.length
        if A[i] < B[j]
            C.push(A[i])
            i++
        else if B[j] < A[i]
            C.push(B[j])
            j++
        else # A[i] == B[j]
            temp = A[i]
            i++ until i == A.length or A[i] != temp
            j++ until j == B.length or B[j] != temp
    if i < A.length
        C = C.concat(A[i..])
    if j < B.length
        C = C.concat(B[j..])

    return C

test_cases = [
    [[[1, 2, 3, 4], [1, 3, 5]],      [2, 4, 5]],    # Typical case
    [[[2, 3], [1, 3, 3, 3, 3]],         [1, 2]],    # Duplicates at end
    [[[1, 2, 3, 4, 5], [2, 4]],      [1, 3, 5]],    # No elements from B in C
    [[[1, 2, 3], [1, 2, 2, 3]],             []]     # SymDiff is []
]

for [test_case, ans] in test_cases
    [A, B] = test_case
    throw 'wah' if "#{symmetric_difference(A, B)}" != "#{ans}"

console.log 'All is Good'
