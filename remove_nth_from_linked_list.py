
class Node:
    def __init__(self, el, next=None):
        self.el = el
        self.next = next


def noderize(arr):
    head = None
    for el in reversed(arr):
        head = Node(el, head)
    return head

def arrayize(node):
    arr = []
    while True:
        arr.append(node.el)
        if node.next == None:
            break
        node = node.next
    return arr


# remove nth node from linked list
def removeNthFromBeg(head, n):
    if head == None: return None
    if n == 0: return head.next
    initial_head = head
    i = 0
    while head.next:
        if i == n - 1:
            head.next = head.next.next
            break
        i += 1
        head = head.next

    return initial_head


test_cases = [
    ([['A', 'B', 'C', 'D'], 0], ['B', 'C', 'D']),
    ([['A', 'B', 'C', 'D'], 1], ['A', 'C', 'D']),
    ([['A', 'B', 'C', 'D'], 2], ['A', 'B', 'D']),
    ([['A', 'B', 'C', 'D'], 3], ['A', 'B', 'C']),
    ([['A', 'B', 'C', 'D'], 4], ['A', 'B', 'C', 'D'])
]

for test_case, ans in test_cases:
    linked_list, n = test_case
    assert arrayize(removeNthFromBeg(noderize(linked_list), n)) == ans
    assert arrayize(removeNthFromBeg(noderize(linked_list), n)) == ans


# remove nth node from linked list
def removeNthFromEnd(head, n):
    if head == None: return None
    laggard = head 
    runner = head
    if n == 0: return head.next
    i = 1
    while runner.next:
        if i > n:
            laggard = laggard.next
        i += 1
        runner = runner.next
    if i == n: return head.next
    if i > n:
        laggard.next = laggard.next.next

    return head



test_cases = [
    ([['A', 'B', 'C', 'D'], 1], ['A', 'B', 'C']),
    ([['A', 'B', 'C', 'D'], 2], ['A', 'B', 'D']),
    ([['A', 'B', 'C', 'D'], 3], ['A', 'C', 'D']),
    ([['A', 'B', 'C', 'D'], 4], ['B', 'C', 'D']),
    ([['A', 'B', 'C', 'D'], 5], ['A', 'B', 'C', 'D'])
]

for test_case, ans in test_cases:
    linked_list, n = test_case
    print linked_list, n, arrayize(removeNthFromEnd(noderize(linked_list), n))
    assert arrayize(removeNthFromEnd(noderize(linked_list), n)) == ans
    assert arrayize(removeNthFromEnd(noderize(linked_list), n)) == ans

