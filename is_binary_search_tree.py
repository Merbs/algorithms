###
# A binary search tree (BST) is a fundamental data structure
#
# To satisfy the BST property, every node on the right subtree must be greater
# than the current node and every node on the left subtree must be less than
# the current node.
#
# Determine whether a tree satisfies the BST property.
#
# For more info,
# Wikipedia: http://en.wikipedia.org/wiki/Binary_search_tree
# Algorithms 4th Ed: http://algs4.cs.princeton.edu/32bst/


def is_binary_search_tree(node, minimum=None, maximum=None):
    """Determines whether the tree satisfies the BST property"""
    if node == None:
        return True
    return (minimum == None or node.el > minimum) and \
           (maximum == None or node.el < maximum) and \
           is_binary_search_tree(node.left, minimum=minimum, maximum=node.el) and \
           is_binary_search_tree(node.right, minimum=node.el, maximum=maximum)

# These binary tree are in preorder: [left_subtree, node_element, right_subtree]
# so that it is easy for a human to verify whether it is or is not a valid BST.
test_cases = [
    ([[[2, 4, 5], 9, 10], 12, [None, 15, 17]], True),
    ([[-7, -5, -2], 0, [None, 2, [None, 4, 5]]], True),     # zero & negative
    ([[7, 3, 6], 13, 19], False),
    ([[1, 3, 5], 7, [9, 11, 10]], False),
    ([2, 4, 5], True),                  # basic case
    ([[None, 2, None], 4, 5], True),    # extraneous leaf nodes don't mess it up
    ([12, 12, 15], False),              # duplicate nodes disqualify it
    (5, True),                          # edge case - single element
    (None, True),                       # edge case - null element
]

class BinaryNode:
    def __init__(self, el, left=None, right=None):
        self.el = el
        self.left = left
        self.right = right

def binary_tree_from_inorder_array(arr):
    if arr is None:
        return None
    if type(arr) != list:
        return BinaryNode(arr)
    return BinaryNode(arr[1],
                      binary_tree_from_inorder_array(arr[0]),
                      binary_tree_from_inorder_array(arr[2]))

for test_case, isBST in test_cases:
    binary_tree = binary_tree_from_inorder_array(test_case)
    assert is_binary_search_tree(binary_tree) == isBST

print 'All is Good'
