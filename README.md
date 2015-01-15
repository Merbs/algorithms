# algorithms
Fun programming puzzles and my algorithmic solutions  

***Arrays***  

- **Maximum Subarray Problem**  
  Given an array of numbers, find the contiguous subarray with the largest sum.
  If multiple subarrays have the same value, return the shortest subarray
  (the subarray with the least number of elements). If multiple subarrays are
  equally short, return the subarray starting at the earliest index.
  If there are no positive elements, return None. Otherwise, return the subarray.
 - [3, 2, -6, 2, 9, -12, 10] should return [2, 9]
 - [-4, 12, 3, -5, 4, 3, -2] should return [12, 3, -5, 4, 3]
 - [4, 5, -12, 9] should return [9]
 - [3, 4, -11, 2, 5] should return [3, 4]

- **Maximum Subarray Difference**  
  Given an array, find two disjoint contiguous subarrays such that the
  difference between their sums is a maximum.
 - [4, 3, -1, -4, 1, -5, 8, 4, -2, 3, -1] should return 22
 - [-1, 3, 2, 5, 2, -5, 1, -4, -3, -1, 2] should return 24

- **Pots of Gold**  
  Given an array of numbers (pots of gold in a line), two players alternate
  turns choosing from one of the two ends. Whoever gets the larger sum wins.
  Design an algorithm that plays optimally with the smallest time complexity.
  Return the scores of the two players
 - pots [9, 7, 5, 3, 1, 0, 2, 4, 6, 8] should return (25, 20)
 - pots [1, 3, 4, 12, 5, 7] might return (22, 10)

- **In-Place Array Reversal**  
  Given an array, reverse the elements using only constant space
 - [1, 2, 3, 4, 5] should return [5, 4, 3, 2, 1]
 - [1, 2, 3, 4] should return [4, 3, 2, 1]

***Sorted Arrays***  
- **Symmetric Difference**  
  Given two sorted lists, return a list of elements not in the intersection
 - A = [1, 2, 3, 4], B = [1, 3, 5] => [2, 4, 5]
 - A = [2, 3], B = [1, 3, 3, 3, 3] => [1, 2]

***Trees***  
Although the below inputs are arrays, assume we have functions that convert the
arrays (in the specified order) to Node(element, left_subtree, right_subtree).
- **Binary Search Trees (BST)**  
  Given a tree, determine whether the tree satisfies the BST property:
  every node on the right subtree must be greater than the current node
  and every node on the left subtree must be less than the current node
  - (inorder) [[[2, 4, 5], 9, 10], 12, [None, 15, 17]] should return *True*
  - (inorder) [[1, 3, 5], 7, [9, 11, 10]] should return *False*
- **Tree Reversal**  
  Given a tree, switch the left and right children for each node.
  - (preorder) [2, [3, [4, 5, None], 6], [7, 8, 9]] should return [2, [7, 9, 8], [3, 6, [4, None, 5]]]
  - (preorder) ['A', ['B', ['C', 'D', None], None], None] should return ['A', None, ['B', None, ['C', None, 'D']]]

***Linked Lists***
- Reverse a linked list
  - (A -> B -> C -> None) should returns (C -> B -> A -> None)

***Strings***
- Reverse the words in a string
  - "hello world" should return "world hello"
  - "these words reversed" should return "reversed words these"