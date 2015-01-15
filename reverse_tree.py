###
# Reverse a tree, such that for every node, their left and right children are switched
#
# For more info,
# Wikipedia: http://en.wikipedia.org/wiki/Binary_search_tree
# Algorithms 4th Ed: http://algs4.cs.princeton.edu/32bst/


def reverse_tree(node):
    """Reverse a BST by recursively switching left and right children"""
    if node == None:
        return
    reverse_tree(node.left)
    reverse_tree(node.right)
    tmp = node.left
    node.left = node.right
    node.right = tmp

# These binary tree are in preorder: [node_element, left_subtree, right_subtree]
# so that it is easy for a human to verify whether it is or is not a valid BST.
test_cases = [
    ([2, [3, [4, 5, None], 6], [7, 8, 9]], [2, [7, 9, 8], [3, 6, [4, None, 5]]]),
    (['A', ['B', ['C', 'D', None], None], None], ['A', None, ['B', None, ['C', None, 'D']]]),
]

class BinaryNode:
    def __init__(self, el, left=None, right=None):
        self.el = el
        self.left = left
        self.right = right

def binary_tree_from_preorder_array(arr):
    if arr is None:
        return None
    if type(arr) != list:
        return BinaryNode(arr)
    return BinaryNode(arr[0],
                      binary_tree_from_preorder_array(arr[1]),
                      binary_tree_from_preorder_array(arr[2]))

def binary_tree_to_preorder_array(node):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return node.el
    return [node.el,
            binary_tree_to_preorder_array(node.left),
            binary_tree_to_preorder_array(node.right)]

for test_case, ans in test_cases:
    binary_tree = binary_tree_from_preorder_array(test_case)
    reverse_tree(binary_tree)
    assert binary_tree_to_preorder_array(binary_tree) == ans

print 'All is Good'
