###
In-Place Array Reversal
Reverse an array using only constant extra space.
###

reverse = (arr) ->
  for i in [0...Math.floor(arr.length/2)]
    j = arr.length - i - 1
    [arr[i], arr[j]] = [arr[j], arr[i]]
  return arr

test_cases =[
  [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],   # odd elements
  [[1, 2, 3, 4], [4, 3, 2, 1]],         # even elements
  [[2, 3], [3, 2]],                     # two elements
  [[2], [2]]                            # single element
]

for [test_case, ans] in test_cases
  throw "wah" if "#{reverse(test_case)}" != "#{ans}"

console.log 'All is Good'