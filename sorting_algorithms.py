from random import shuffle, random
from math import floor

def merge(arr1, arr2):
    if len(arr1) == 0: return arr2
    if len(arr2) == 0: return arr1
    if arr1[0] < arr2[0]:
        return [arr1[0]] + merge(arr1[1:], arr2)
    else:
        return [arr2[0]] + merge(arr2[1:], arr1)

def mergesort(arr):
    n = len(arr)
    return merge(mergesort(arr[n/2:]), mergesort(arr[:n/2])) if n > 1 else arr


def randInt(n):
    return int(floor(random() * n))

def quicksort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[randInt(n)]
    lt, eq, gt = [], [], []
    for el in arr:
        if el < pivot:
            lt.append(el)
        elif el == pivot:
            eq.append(el)
        else:
            gt.append(el)
    return quicksort(lt) + eq + quicksort(gt)

def determinePivot(arr, start, end):
    p = start + randInt(end - start + 1)
    return (p, arr[p])

def inplace_quicksort(arr, start, end):
    if end > start:
        p, pivot = determinePivot(arr, start, end)

        arr[end], arr[p] = arr[p], arr[end]

        p = start
        for i in xrange(start, end):
            if arr[i] < pivot:
                arr[p], arr[i] = arr[i], arr[p]
                p += 1

        arr[end], arr[p] = arr[p], arr[end]

        inplace_quicksort(arr, start, p-1)
        inplace_quicksort(arr, p+1, end)


def shuffled(arr):
    shuffle(arr)
    return arr

test_cases = [
    (shuffled(range(10)), range(10)),
    (list(reversed(range(20))), range(20)),
]

for test_case, ans in test_cases:
    assert quicksort(test_case) == ans
    assert mergesort(test_case) == ans
    inplace_quicksort(test_case, 0, len(test_case)-1)
    assert test_case == ans

print 'All is Good'
