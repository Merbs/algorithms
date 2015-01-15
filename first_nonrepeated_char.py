###
# First Nonrepeated Character
# Given a UTF-8 string, find the first nonrepeated character.
# If no characters are nonrepeated, return None.
###

# A great opportunity to use bucket sort!
SEEN_ONCE = True
SEEN_MORE_THAN_ONCE = False
def find_first_nonrepeated_char(string):
    arr = [None] * 256
    for el in string:
        arr[ord(el)] = SEEN_ONCE if arr[ord(el)] == None else SEEN_MORE_THAN_ONCE
    for el in string:
        if arr[ord(el)] == SEEN_ONCE:
            return el
    return None


test_cases = [
    ("abcdefabde", "c"),        # c and f are nonrepeated, c is first
    ("abcabc", None)            # no character is nonrepeated
]

for test_case, ans in test_cases:
    assert find_first_nonrepeated_char(test_case) == ans

print 'All is Good'
