###
# Cyclic Linked List
# Given a linked list, determine if there is a cycle. A cycle is when any
# node loops back to a previous node (causing an infinite cylce of nodes).
# The cycle may not begin at the first node (i.e. a chain, then a cycle).
###

# The gist here is to imagine we're on a track with a runner and walker:
# if there is a cycle, the runner will eventually catch up to the walker
# If not, the runner will get to the end, and determine there is no cycle.
def is_cycle(node):
    ptr1 = node
    ptr2 = node
    while ptr2.next and ptr2.next.next:
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
        if ptr1 == ptr2:
            return True
    return False

# This is an alternate trivial version (uses more space, saves time)
def is_cycle_flag(node):
    while node:
        if node.flag:
            return True
        node.flag = True
        node = node.next
    return False

# If the nodes can't be modified, we can keep their memory id
def is_cycle_mem_id(node):
    seen = {}
    while node:
        if id(node) in seen:
            return True
        seen[id(node)] = True
        node = node.next
    return False


class Node:
    def __init__(self, el, next=None):
        self.el = el
        self.next = next
        self.flag = False

test_cases = [
    (['A', 'B', 'C', 'B'], True),        # cycle (not total)
    (['A', 'B', 'C', 'A'], True),        # total cycle
    (['A', 'B', 'C', 'D'], False),       # not a cycle
    (['A', 'A'], True)                   # a cycle of one
]

# This is an idiosyncratic way to translate an array into a linked list
# The 'loops' are if the el is present twice (which is not really what
# a cycle in a linked list would look like, but this is just for testing)
# So A -> B -> C -> (loops to B) is the first test, and if no el is
# repeated, it looks like A -> B -> C -> D -> None. Strangely, this is a
# non-space efficient version of the actual function I'm testing. That is
# to determine if there is a loop (and to make it), I'm just using
# additional space (a dict to hold the index, and an array for the nodes).
def noderize_with_loops(arr):
    head = Node(arr[0])
    seen = {}
    seen[arr[0]] = 0
    nodes = [head]
    curr = head
    for i, el in enumerate(arr[1:]):
        if el in seen:
            curr.next = nodes[seen[el]]
            return head
        seen[el] = i
        curr.next = Node(el)
        nodes.append(curr.next)
        curr = curr.next
    curr.next = None
    return head

for test_case, ans in test_cases:
    assert is_cycle(noderize_with_loops(test_case)) == ans
    assert is_cycle_flag(noderize_with_loops(test_case)) == ans
    assert is_cycle_mem_id(noderize_with_loops(test_case)) == ans

print "All is Good"
