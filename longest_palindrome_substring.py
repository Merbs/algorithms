###
# Longest Palindrome Substring
# Find the longest substring which is a palindrome. If there are
# multiple longest strings, find the one which starts at the earliest index.
###

# Uses dynamic programming to find the longest palindrome substring
# In order for a substring(i, j) to be a palindrome, substring(i+1,j-1)
# must also be a palindrome (assuming i does not equal j). The conditional
# if statements ensure that the longest palindrome which starts at the
# earliest index is returned (rather than the one starting at the latest)
def find_longest_palindrome_substring(string):
    if not string: return ""

    L = len(string)

    is_palindrome = [[False for j in range(L)] for i in range(L)]
    length_so_far, indices_so_far = 1, (0, 0)

    # Base Cases
    for i in range(L):
        # All substrings of length 1 are palindromes
        is_palindrome[i][i] = True
    for i in range(L-1):
        # Substrings of length 2 are palindromes IF both letters are the same
        if string[i] == string[i+1]:
            is_palindrome[i][i+1] = True
            if 2 > length_so_far:
                length_so_far, indices_so_far = 2, (i, i+1)

    # Inductive Step
    for substring_length in xrange(3, L+1):
        for i in xrange(0, L+1 - substring_length):
            j = i + (substring_length - 1)
            if is_palindrome[i+1][j-1] and string[i] == string[j]:
                is_palindrome[i][j] = True
                if substring_length > length_so_far:
                    length_so_far = substring_length
                    indices_so_far = (i, j)

    i, j = indices_so_far
    return string[i:j+1]

test_cases = [
    ("xyabcdcba", "abcdcba"),                # Odd palindrome
    ("xyabcdeedcbaz", "abcdeedcba"),         # Even palindrome
    ("xyabcbazdefedw", "abcba"),             # Two equal-length palindromes
    ("abcba", "abcba")                       # Whole substring is palindrome
]

for test_case, ans in test_cases:
    assert find_longest_palindrome_substring(test_case) == ans

print 'All is Good'
