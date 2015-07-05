###
# Finding the Median
# Given two sorted arrays, find the median.
# - If both have length N
# - If they have unequal lengths
###

# By definition, the median is the 'middle element' of a sorted list
# If the list has even length though, we take the average of the two
# middle elements. We don't check whether the list is sorted or not
# because that would take O(n) time and we want this to be O(1).
def median_of_sorted_list(arr):
    N = len(arr)
    if N % 2 == 0:
        return (arr[N/2 - 1] + arr[N/2]) / 2.0
    else:
        return arr[(N-1)/2]

# If we don't care about time, we can append B to A and sort it.
# Since A and B are of equal length, the combined array has an even
# number of elements, so we take the average of the two middle elements
def find_median_of_two_equal_sized_sorted_lists_O_of_n_log_n(A, B):
    n = len(A) # == len(B)
    return sum(sorted(A + B)[n-1:n+1]) / 2.0

# However, we should care about time. So let's do a little better
# We can improve to O(n) time by simply keeping a count and doing
# what we've done for mergesort and just iterate through both lists
# from the beginning until the count is equal to N-1. Then we take
# the average of the N-1 and N-th elements. Note that if every element
# in A is less than every element in B, we take the last element in A
# and average it with the first element in B (or vice versa). Otherwise
# once we've found the (N-1)th element, we need to determine which is the
# Nth element by comparing the next in the list (of the (N-1)th element)
# and the current-indexed element of other list.
def find_median_of_two_equal_sized_sorted_lists_O_of_n(A, B):
    N = len(A)
    i, j = 0, 0
    for m in xrange(N-1):
        if A[i] <= B[j]:
            i += 1
        else:
            j += 1
    if i == N-1 or j == N-1:
        return (A[i] + B[j]) / 2.0
    elif A[i] <= B[j]:
        return (A[i] + min(A[i+1], B[j])) / 2.0
    else:
        return (B[j] + min(A[i], B[j+1])) / 2.0

# Of course, we can do even better. One method is to do binary search.
# This is the other method, which is a recursive call of comparing the
# medians and eliminating the two halfs that don't contain the medians.
# The justification is simple: if median_A < median_B then everything
# less than median_A must be less than at least N other elements. The
# same goes for everything greater than B. So we eliminate those elements.
# In practice, this function has a fatal flaw, which is that, in Python,
# doing arr[x:] is a slice that copies the array. So this function is
# actually taking O(n) time for all the copies it's doing. To rectify this,
# we should either make this iterative (as the next function is), or pass
# in the arrays A, B and additional parameter A_start, A_end, B_start, B_end.
# The next function (albeit named for unequal lists), also handles equal lists
# so you can see how it would be done there.
def find_median_of_two_equal_sized_sorted_lists_O_of_log_n(A, B):
    find_median = find_median_of_two_equal_sized_sorted_lists_O_of_log_n
    assert len(A) == len(B)
    N = len(A)

    if N == 1: return (A[0] + B[0]) / 2.0
    if N == 2: return (max(A[0], B[0]) + min(A[1], B[1])) / 2.0
    m = (N-2)/2 if N % 2 == 0 else (N-1)/2

    if median_of_sorted_list(A) < median_of_sorted_list(B):
        return find_median(A[m:], B[:N-m])
    else:
        return find_median(A[:N-m], B[m:])

def median_of_3(a, b, c):
    return a + b + c - max(a, b, c) - min(a, b, c)

def median_of_4(a, b, c, d):
    return (a + b + c + d - max(a, b, c, d) - min(a, b, c, d)) / 2.0

# The helpers above make this nominally more readable, while sacrificing
# a very small amount of efficiency (as in a couple of comparisons x < y)
# Despite the naming of this function, you can see that we handle the cases
# N == M == 1 and N == M == 2. Since we eliminate the number of elements from
# both lists on every iteration, the list B should always be larger than A if
# it began larger (and it must, if not equal, because we switch them otherwise).
def find_median_of_two_unequal_sized_sorted_lists_with_helpers(A, B):
    # Make A the smaller of the two arrays, if it isn't already
    if len(A) > len(B):
        A, B = B, A
    N, M = len(A), len(B)

    # On each iteration, we narrow our search range by about the remaining size
    # of the smaller array, A (specifically, floor(A/2) * 2), until A only has
    # two elements left. We do this by comparing the medians of what remains of
    # A and B. For a visual, if we start with:
    #   A = [_, _, _, _, _], B = [_, _, _, _, _, _, _], then ...
    (A_start, A_end), (B_start, B_end) = (0, N-1), (0, M-1)
    while A_end - A_start > 1:
        k = ((A_end + A_start) / 2) - A_start
        if A[(A_end + A_start) / 2] < B[(B_end + B_start) / 2]:
            # A = [X, X, _, _, _], B = [_, _, _, _, _, X, X]
            A_start += k
            B_end -= k
        else:
            # A = [_, _, _, X, X], B = [X, X, _, _, _, _, _]
            A_end -= k
            B_start += k
    N, M = A_end - A_start + 1, B_end - B_start + 1

    if N == 1:
        median_A = A[A_start]
        if M == 1:
            median_B = B[B_start]
            return (median_A + median_B) / 2.0
        if M % 2 == 0:
            lower_B = B[((B_start + B_end - 1) / 2)]
            upper_B = B[((B_start + B_end + 1) / 2)]
            return median_of_3(lower_B, median_A, upper_B)
        else: # M is odd
            lower_B = B[(B_start + B_end - 2) / 2]
            median_B = B[(B_start + B_end) / 2]
            upper_B = B[(B_start + B_end + 2) / 2]
            return median_of_4(median_A, lower_B, median_B, upper_B)
    else: ## N == 2:
        lower_A = A[A_start]
        upper_A = A[A_end]
        if M == 2:
            lower_B = B[B_start]
            upper_B = B[B_end]
            return median_of_4(lower_A, lower_B, upper_A, upper_B)
        elif M % 2 == 0:
            lower_B = B[(B_start + B_end - 3) / 2]
            lower_median_B = B[(B_start + B_end - 1) / 2]
            upper_median_B = B[(B_start + B_end + 1) / 2]
            upper_B = B[(B_start + B_end + 3) / 2]

            return median_of_4(max(lower_A, lower_B), lower_median_B,
                               min(upper_A, upper_B), upper_median_B)
        else: # M is odd
            lower_B = B[(B_start + B_end - 2) / 2]
            median_B = B[(B_start + B_end) / 2]
            upper_B = B[(B_start + B_end + 2) / 2]

            return median_of_3(max(lower_A, lower_B), median_B,
                               min(upper_A, upper_B))


# Of course, the helpers don't make use of the fact that lower_A < upper_A
# and so forth, so even though that extra comparison doesn't take much time
# (and probably is more than compensated by the benefit the underlying hardware
# gets from branch prediction), let us be super purists here and go ALL THE WAY
# This question is intended to make you think through all the edge cases.
def find_median_of_two_unequal_sized_sorted_lists(A, B):
    if len(A) > len(B):
        A, B = B, A
    N, M = len(A), len(B)

    (A_start, A_end), (B_start, B_end) = (0, N-1), (0, M-1)
    while A_end - A_start > 1:
        k = ((A_end + A_start) / 2) - A_start
        if A[(A_end + A_start) / 2] < B[(B_end + B_start) / 2]:
            A_start += k
            B_end -= k
        else:
            A_end -= k
            B_start += k
    N, M = A_end - A_start + 1, B_end - B_start + 1

    if N == 1:
        median_A = A[A_start]
        if M == 1:
            median_B = B[B_start]
            return (median_A + median_B) / 2.0
        if M % 2 == 0:
            lower_B = B[((B_start + B_end - 1) / 2)]
            upper_B = B[((B_start + B_end + 1) / 2)]
            if median_A < lower_B:
                return lower_B
            elif median_A > upper_B:
                return upper_B
            else: # lower_B < median_A < upper_B
                return median_A
        else: # M is odd
            lower_B = B[(B_start + B_end - 2) / 2]
            median_B = B[(B_start + B_end) / 2]
            upper_B = B[(B_start + B_end + 2) / 2]
            if median_A < lower_B:
                return (lower_B + median_B) / 2.0
            elif median_A > upper_B:
                return (upper_B + median_B) / 2.0
            else: # lower_B < median_A ~ median_B < upperB
                # regardless of whether median_A > or < median_B
                return (median_A + median_B) / 2.0
    else: ## N == 2:
        lower_A = A[A_start]
        upper_A = A[A_end]
        if M == 2:
            # For 'a'=lower_A, 'A'=upper_A, 'b'=lower_B, 'B'=upper_B,
            # {abBA, aAbB, abAB, baAB, baBA, bBaA} are the possibilities,
            # but as seen below the answer is the same for aAbB and abAB
            # so we only need 2 comparisons to narrow down 6 possibilities.
            lower_B = B[B_start]
            upper_B = B[B_end]
            if lower_A < lower_B:
                if upper_A > upper_B:      # abBA
                    return (lower_B + upper_B) / 2.0
                else:              # aAbB or abAB
                    return (lower_B + upper_A) / 2.0
            else:
                if upper_A < upper_B:      # baAB
                    return (lower_A + upper_A) / 2.0
                else:              # baBA or bBaA
                    return (lower_A + upper_B) / 2.0
        elif M % 2 == 0:
            lower_B = B[(B_start + B_end - 3) / 2]
            lower_median_B = B[(B_start + B_end - 1) / 2]
            upper_median_B = B[(B_start + B_end + 1) / 2]
            upper_B = B[(B_start + B_end + 3) / 2]

            lower = max(lower_A, lower_B)
            upper = min(upper_A, upper_B)
            if lower > upper:
                lower, upper = upper, lower
            if lower < lower_median_B:
                if upper > upper_median_B:
                    return (lower_median_B + upper_median_B) / 2.0
                else:
                    return (lower_median_B + upper) / 2.0
            else:
                if upper < upper_median_B:
                    return (lower + upper) / 2.0
                else:
                    return (lower + upper_median_B) / 2.0
        else: # M is odd
            lower_B = B[(B_start + B_end - 2) / 2]
            median_B = B[(B_start + B_end) / 2]
            upper_B = B[(B_start + B_end + 2) / 2]

            lower = max(lower_A, lower_B)
            upper = min(upper_A, upper_B)
            if lower > upper:
                lower, upper = upper, lower
            if median_B < lower:
                return lower
            elif median_B > upper:
                return upper
            else:
                return median_B

test_cases = [
    (([4], [6]), 5),                      # M == N == 1
    (([2, 3], [4, 5]), 3.5),              # M == N == 2
    # N = 1, M odd
    (([1], [2, 4, 7]), 3),                # A[0], B[0], B[1], B[2]
    (([3], [2, 4, 7]), 3.5),              # B[0], A[0], B[1], B[2]
    (([6], [2, 4, 7]), 5),                # B[0], B[1], A[0], B[2]
    (([8], [2, 4, 7]), 5.5),              # B[0], B[1], B[2], A[0]
    # N = 1, M even
    (([1], [2, 4, 7, 9]), 4),             # A[0] < B_lower
    (([5], [2, 4, 7, 9]), 5),             # B_lower < A[0] < B_upper
    (([8], [2, 4, 7, 9]), 7),             # A[0] > B_upper
    # N = 2, M even ...
    # N = 2, M odd ...
    # N = 2, M == 2 ...
    # N > 2, M > 2 ...
]


from numpy import median
from random import randint

for _ in range(100):
    length = randint(50, 100)

    A = sorted([randint(0, 1000) for _ in range(length)])
    B = sorted([randint(0, 1000) for _ in range(length)])
    M = median(A + B)

    assert M == find_median_of_two_equal_sized_sorted_lists_O_of_log_n(A, B)
    assert M == find_median_of_two_unequal_sized_sorted_lists(A, B)
    assert M == find_median_of_two_unequal_sized_sorted_lists_with_helpers(A, B)

    lengthA = randint(50, 100)
    lengthB = randint(50, 100)

    A = sorted([randint(0, 1000) for _ in range(lengthA)])
    B = sorted([randint(0, 1000) for _ in range(lengthB)])
    M = median(A + B)

    assert M == find_median_of_two_unequal_sized_sorted_lists(A, B)
    assert M == find_median_of_two_unequal_sized_sorted_lists_with_helpers(A, B)

print 'All is Good'
