###
# Maximum Sum Path
# Given two sorted linked lists, construct the linked list with the
# maximum sum path. The path must start at the beginning of one of the
# two linked lists and may only crossover when the value of the two
# linked lists is the same. Only constant extra space may be used.
# If there are multiple maximum sum paths, return the path that has
# the lowest number at the divergence.
###

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def sum_of_linked_list(node):
    if not node:
        return 0
    return node.value + sum_of_linked_list(node.next)

def copy_linked_list(node):
    if not node:
        return None
    return Node(node.value, copy_linked_list(node.next))

def copy_linked_list_until(node, value, after):
    if node.value == value:
        return Node(value, after)
    return Node(node.value, copy_linked_list_until(node.next, value, after))

def maximum_sum_path(node1, node2):
    if not node1 and not node2:
        return None
    if node1 and node2 and node1.value == node2.value:
        # This check is actually unnecessary, but makes it more understandable 
        return Node(node1.value, maximum_sum_path(node1.next, node2.next))

    # Otherwise, node1.value != node2.value and we create two runners, which
    # sum up their values until they either meet at an intersection or end.
    nodeA, nodeB = node1, node2
    sumA, sumB = 0, 0
    while nodeA and nodeB and nodeA.value != nodeB.value:
        if nodeA.value < nodeB.value:
            sumA += nodeA.value
            nodeA = nodeA.next
        elif nodeB.value < nodeA.value:
            sumB += nodeB.value
            nodeB = nodeB.next

    # If there are no more intersections, determine which of the two
    # linked lists has the largest remaining sum and copy until end.
    if not nodeA or not nodeB:
        sumA += sum_of_linked_list(nodeA)
        sumB += sum_of_linked_list(nodeB)
        if sumA > sumB or (sumA == sumB and nodeA.value <= nodeB.value):
            return copy_linked_list(node1)
        else:
            return copy_linked_list(node2)

    # If the linked lists met at an intersection, first compute the
    # maximum sum path of the remaining linked list, and then determine
    # which had the largest path up to the intersection and copy that list
    next_node = maximum_sum_path(nodeA.next, nodeB.next)
    if sumA > sumB or (sumA == sumB and node1.value <= node2.value):
        return copy_linked_list_until(node1, nodeA.value, next_node)
    else:
        return copy_linked_list_until(node2, nodeB.value, next_node)

test_cases = [
    (([1, 5, 6, 9], [2, 3, 6, 7, 8]), [1, 5, 6, 7, 8]),
    (([1, 3, 5, 6, 7], [2, 3, 4, 6, 8]), [2, 3, 5, 6, 8]), # Two intersections
    (([2, 3], [1, 3, 5]), [2, 3, 5]),               # One ends on intersection
    (([2, 4, 5], [1, 3, 5]), [2, 4, 5]),            # Both end on intersection
    (([2, 4, 6], [1, 3, 5]), [2, 4, 6]),            # No intersections
    (([1, 2, 3], [1, 2, 3]), [1, 2, 3])             # A and B are identical
]

def noderize(arr):
    head = None
    for el in reversed(arr):
        head = Node(el, head)
    return head

def arrayize(node):
    arr = []
    while True:
        arr.append(node.value)
        if node.next == None:
            break
        node = node.next
    return arr

for test_case, ans in test_cases:
    A, B = map(noderize, test_case)
    assert arrayize(maximum_sum_path(A, B)) == ans


print "All is Good"
