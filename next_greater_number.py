###
# Next Greater Number
# Given an array, construct an array which, for every index in the original array,
# has the next greatest number in the original array. If no greater number exists,
# have that element be None/null.
###

def next_greater_number(arr):
    next_greater = []
    stack = []
    for el in reversed(arr):
        while stack and el >= stack[-1]:
            stack.pop()
        if stack:
            next_greater.append(stack[-1])
        else:
            next_greater.append(None)
        stack.append(el)
    return list(reversed(next_greater))


test_cases = [
    ([4, 5, 7, 4, 2, 7, 9, 3, 5], [5, 7, 9, 7, 7, 9, None, 5, None]),
    ([1, 3, 5], [3, 5, None]),
    ([5, 3, 1], [None, None, None])
]

for test_case, ans in test_cases:
    assert next_greater_number(test_case) == ans

print 'All is Good'
