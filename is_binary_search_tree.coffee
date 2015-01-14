###
A binary search tree (BST) is a fundamental data structure

To satisfy the BST property, every node on the right subtree must be greater
than the current node and every node on the left subtree must be less than
the current node.

Determine whether a tree satisfies the BST property.

For more info,
Wikipedia: http://en.wikipedia.org/wiki/Binary_search_tree
Algorithms 4th Ed: http://algs4.cs.princeton.edu/32bst/
###
# Determines whether the tree satisfies the BST property
is_binary_search_tree = (node, minimum, maximum) ->
  if node == null
    return true
  return ((not minimum? or node.el > minimum) and
          (not maximum? or node.el < maximum) and
          is_binary_search_tree(node.left, minimum, node.el) and
          is_binary_search_tree(node.right, node.el, maximum))

# These binary tree are in preorder: [left_subtree, node_element, right_subtree]
# so that it is easy for a human to verify whether it is or is not a valid BST.
test_cases = [
  [[[[2, 4, 5], 9, 10], 12, [null, 15, 17]], true],
  [[[-7, -5, -2], 0, [null, 2, [null, 4, 5]]], true],     # zero & negative
  [[[7, 3, 6], 13, 19], false],
  [[[1, 3, 5], 7, [9, 11, 10]], false],
  [[2, 4, 5], true],                  # basic case
  [[[null, 2, null], 4, 5], true],    # extraneous leaf nodes don't mess it up
  [[12, 12, 15], false],              # duplicate nodes disqualify it
  [5, true],                          # edge case - single element
  [null, true]                        # edge case - null element
]

BinaryNode = (el, left=null, right=null) -> {
  el: el
  left: left
  right: right
}

binary_tree_from_inorder_array = (arr) ->
  if not arr?
    return null
  return BinaryNode(arr) if not Array.isArray(arr)
  return BinaryNode(arr[1],
                    binary_tree_from_inorder_array(arr[0]),
                    binary_tree_from_inorder_array(arr[2]))

for [test_case, isBST] in test_cases
  binary_tree = binary_tree_from_inorder_array(test_case)
  throw "wah" if is_binary_search_tree(binary_tree) != isBST

console.log("All is Good")
