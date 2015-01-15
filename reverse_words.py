###
# Reverse Words in a String
###

def reverse_words(string):
    reversed_string = ''
    j = len(string)
    for i in range(len(string)-1, 0, -1):
        if string[i] == ' ':
            reversed_string += string[i+1:j] + ' '
            j = i
    reversed_string += string[:j]
    return reversed_string

def reverse_words_pythonic(string):
    return ' '.join(reversed(string.split(' ')))

test_cases = [
    ("hello world", "world hello"),
    ("these words reversed", "reversed words these")
]

for test_case, ans in test_cases:
    assert reverse_words(test_case) == ans

print "All is Good"
