# algorithms
Fun programming puzzles and my algorithmic solutions

### Arrays

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

- **Longest Increasing Subsequence**  
  Given a sequence of numbers, find the longest subsequence with strictly
  increasing numbers.
 - [10, 1, 3, 9, 2, 7, 5, 6] returns length 4 ([1, 2, 5, 6] or [1, 3, 5, 6])
 - [5, 4, 3, 2, 1] returns length 1 ([1] or [2] or [3] or [4] or [5])

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

### Sorted Arrays
- **Symmetric Difference**  
  Given two sorted lists, return a list of elements not in the intersection
 - A = [1, 2, 3, 4], B = [1, 3, 5] => [2, 4, 5]
 - A = [2, 3], B = [1, 3, 3, 3, 3] => [1, 2]

### Trees (Recursion)
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
  - (preorder) [2, [3, [4, 5, None], 6], [7, 8, 9]] should return
  [2, [7, 9, 8], [3, 6, [4, None, 5]]]
  - (preorder) ['A', ['B', ['C', 'D', None], None], None] should return
  ['A', None, ['B', None, ['C', None, 'D']]]

### Linked Lists
- **Linked List Reversal**  
  - (A -> B -> C -> None) should returns (C -> B -> A -> None)
- **Maximum Sum Path**  
  Given two sorted linked lists, construct the linked list with the maximum
  sum path. The path must start at the beginning of one of the two linked lists
  and may only crossover when the value of the two linked lists is the same.
  Only constant extra space may be used. If there are multiple maximum sum
  paths, return the path that has the lowest number at the divergence.
  - A = [1, 5, 6, 9], B = [2, 3, 6, 7, 8] should return [1, 5, 6, 7, 8]
  - A = [2, 4, 6], B = [1, 3, 5] should return [2, 4, 6]

### Strings
- **Reverse the Words**  
  - "hello world" should return "world hello"
  - "these words reversed" should return "reversed words these"
- **Matching Delimiters**  
  Given a string, determine if the delimiters (), {}, [] are matching and valid.
  That is, there are equal numbers of opening/closing delimiters and for each
  closing delimiter, it should match the most recent unmatched opening delimiter.
  - "(this[is{true}])" should return *True*
  - "([)]" should return *False*
  - "(this[is]false" should return *False*
- **Valid Interleaving**  
  Given strings A, B, and C, determine if C is an valid interleaving of A and B.
  A valid interleaving is one where each character in C from A is in the same
  order as it was in A, and each character in C from B is in the same order as
  it was in B.
  - A = 'abcd', B = 'efgh', C = 'aefbgchd' should return *True*
  - A = 'abc', B = 'abd', C = 'abcdab' should return *False*
- **Duplicate Characters**  
  Given a UTF-8 string (or just a string with letters and numbers), find the
  most frequent character. If there is a tie, return the character that appears
  first in the string.
  - "abcdae' should return "a"
  - "a2a2b3" should return "a"
- **Longest Palindrome Substring**  
  Find the longest substring which is a palindrome. If there are multiple
  longest palindromes, find the one which starts at the earliest index.
  - "xyabcdeedcbaz" should return "abcdeedcba"
  - "xyabcbazdefedw" should return "abcba"
- **First Nonrepeated Character**  
  Given a UTF-8 string, find the first nonrepeated character.
  If no characters are nonrepeated, return None.
  - "abcdefabde" should return "c"
  - "abcabc" should return *None*

### Sorting
 - Quicksort
 - In-Place Quicksort
 - Merge sort
 - Bucket Sort
