###
# Longest Increasing Subsequence
# Given a sequence of numbers find the longest (perhaps noncontiguous) subsequence
# of strictly increasing numbers.
###

def longest_increasing_subsequence(seq):
    if not seq: return

    longest_stack = [(1, seq[-1])]
    for i in reversed(range(len(seq))):
        seq[i]

    # We record the longest increasing subsequences ending at index i
    lis = {0: [seq[0]]}
    for i in range(1, len(seq)):
        temp_length, temp_path = 0, []
        for j in range(i):
            if seq[j] < seq[i] and len(lis[j]) > temp_length:
                temp_length = len(lis[j])
                temp_path = lis[j]
        lis[i] = temp_path + [seq[i]]

    # Now we search over all increasing subsequences to find the longest
    longest_length, longest_path = 0, []
    for i in range(len(seq)):
        if len(lis[i]) > longest_length:
            longest_length = len(lis[i])
            longest_path = lis[i]
    return longest_path

# There is another version which trades time complexity for space complexity
# The basic gist is to keep a heap (or binary search through an array) and
# instead of the 'for j in range(i)' loop, which makes this take O(n^2) time,
# it finds each longest subsequence ending at index i in O(log(n)) time for a
# total O(n log(n)) time with O(n) space used. I'll consider adding it later.

test_cases = [
    ([10, 1, 3, 9, 2, 7, 5, 6], 4),
    ([5, 4, 3, 2, 1], 1)
]

for test_case, ans in test_cases:
    assert len(longest_increasing_subsequence(test_case)) == ans

print 'All is Good'