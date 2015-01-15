###
# Duplicate Characters
# Given a UTF-8 string, find the most frequent character.
# If there is a tie, return the character that appears first.
###

# Really, this is just an opportunity to use bucket sort
# Also, I'm evidently playing code golf, given the way I'm using max
def get_most_frequent_char(string):
    # In our bucket we have [count, first_index, char_index]
    bucket = [[0, None, c] for c in range(256)]
    for i, character in enumerate(reversed(string)):
        bucket[ord(character)][0] += 1
        bucket[ord(character)][1] = i
    return chr(max(bucket)[2])

test_cases = [
    ('abcdae', 'a'),
    ('abbaAAddb', 'b'),  # 'A' and 'a' are different
    ('a2a2b3', 'a')      # If tie, choose chr that appears first
]

for test_case, ans in test_cases:
    assert get_most_frequent_char(test_case) == ans

print 'All is Good'
