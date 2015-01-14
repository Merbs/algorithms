# algorithms
Fun programming puzzles and my algorithmic solutions

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

- **Pots of Gold**  
  Given an array of numbers (pots of gold in a line), two players alternate
  turns choosing from one of the two ends. Whoever gets the larger sum wins.
  Design an algorithm that plays optimally with the smallest time complexity.
  Return the scores of the two players
 - pots [9, 7, 5, 3, 1, 0, 2, 4, 6, 8] should return (25, 20)
 - pots [1, 3, 4, 12, 5, 7] might return (22, 10)
