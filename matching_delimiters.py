###
# Matching Delimiters
# Given a string, determine if the delimiters (), {}, [] are matching and valid.
# That is, there are equal numbers of opening/closing delimiters and for each
# closing delimiter, it should match the most recent unmatched opening delimiter.
###

def closing_delimiter(opening_delimiter):
    if opening_delimiter == '(':
        return ')'
    elif opening_delimiter == '{':
        return '}'
    elif opening_delimiter == '[':
        return ']'

def matching_delimiters(string):
    stack = []
    for el in string:
        if el in ['(','{','[']:
            stack.append(el)
        elif el in [')','}',']']:
            if el != closing_delimiter(stack.pop()):
                return False
    if stack == []:
        return True
    return False

test_cases = [
    ("(this[is{true}])", True),
    ("([)]", False),
    ("(this[is]false", False)
]

for test_case, ans in test_cases:
    assert matching_delimiters(test_case) == ans

print 'All is Good'
