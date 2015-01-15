###
# Valid Interleaving
# Given strings A, B, and C, determine if C is an valid interleaving of A and B.
# A valid interleaving is one where each character in C from A is in the same order
# as it was in A, and each character in C from B is in the same order as it was in B.
###


def is_valid_interleaving(str1, str2, interleaved_str):
    """Checks whether the interleaved string is valid in O(n) time and space"""
    # if len(str1) + len(str2) != len(interleaved_str): return False

    str1 = list(str1)
    str2 = list(str2)
    interleaved_str = list(interleaved_str)
    duplicates = []

    # We start from the back (for silly efficiency reasons)
    while interleaved_str:
        char = interleaved_str.pop()
        if str1 and str2 and str1[-1] == char and str2[-1] == char:
            str1.pop()
            str2.pop()
            duplicates.append(char)
        elif str1 and str1[-1] == char:
            str1.pop()
            str2 = str2 + duplicates
            duplicates = []
        elif str2 and str2[-1] == char:
            str2.pop()
            str1 = str1 + duplicates
            duplicates = []
        elif duplicates and duplicates[0] == char:
            # We take from the front (as if from a queue) because if we
            # are interleaving 'abc' and 'abd', and already are at 'ab'
            # and the next character is an 'a', it's still valid so far
            # but would not be if the next character was a 'b'
            duplicates.pop(0)
        else:
            return False

    if str1 or str2 or duplicates:
        # this check is unnecessary if we check the length beforehand
        return False
    return True

# Another (identical) way, using a for loop and checking from the front
def is_valid_interleaving2(str1, str2, interleaved_str):
    if len(str1) + len(str2) != len(interleaved_str):
        return False

    duplicates = ''
    i, j = 0, 0
    for k in range(len(interleaved_str)):
        char = interleaved_str[k]
        matches_str1 = i < len(str1) and str1[i] == char
        matches_str2 = j < len(str2) and str2[j] == char
        if matches_str1 and matches_str2:
            i += 1
            j += 1
            duplicates = duplicates + char
        elif matches_str1:
            i += 1
            str2 = duplicates + str2
            duplicates = ''
        elif matches_str2:
            j += 1
            str1 = duplicates + str1
            duplicates = ''
        elif duplicates != '' and duplicates[0] == char:
            duplicates = duplicates[1:]
        else:
            return False
    return True

test_cases = [
    (['abcd', 'efgh', 'aefbgchd'], True),   # Typical True case
    (['abcd', 'efgh', 'aefbhcgd'], False),  # Typical False case

    # # Does it handle duplicates?
    (['ab', 'ac', 'abc'], False),
    (['ab', 'ac', 'abca'], False),
    (['ab', 'ac', 'abac'], True),
    (['ab', 'ac', 'aabc'], True),
    (['abc', 'abd', 'abcdab'], False),
    (['abad', 'ace', 'abacade'], True),
    (['abad', 'ace', 'abacde'], False)
]

for test_case, ans in test_cases:
    str1, str2, interleaved_str = test_case
    assert is_valid_interleaving(str1, str2, interleaved_str) == ans
    assert is_valid_interleaving2(str1, str2, interleaved_str) == ans

print 'All is Good'
