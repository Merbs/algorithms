###
# Linked List Reversal
###

def reverse_iterative(node):
    """Reverses the linked list and returns the new head

    Given A -> B -> C -> None, it returns C -> B -> A -> None
    """
    prev_node = None
    while node:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node
    return prev_node      # the head changes to what was originally last node

def reverse_recursive(node, prev_node=None):
    if node.next:
        node_next = node.next
        node.next = prev_node
        return reverse_recursive(node_next, prev_node=node)
    else:
        node.next = prev_node
        return node


class Node:
    def __init__(self, el, next=None):
        self.el = el
        self.next = next

test_cases = [
    (['A', 'B', 'C', 'D', 'E'], ['E', 'D', 'C', 'B', 'A']),
    ([1, 2, 3, 4], [4, 3, 2, 1]),
    ([1, 2, 3], [3, 2, 1]),
    ([1, 2], [2, 1]),
    ([1], [1])
]

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

for test_case, ans in test_cases:
    assert arrayize(reverse_iterative(noderize(test_case))) == ans
    assert arrayize(reverse_recursive(noderize(test_case))) == ans


print "All is Good"
