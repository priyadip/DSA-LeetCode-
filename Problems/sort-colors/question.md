# 75. Sort Colors

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Sorting, Quicksort, Bubble Sort

[View on LeetCode](https://leetcode.com/problems/sort-colors/)

## Description

You are given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm) **so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

**Example 1:**

**Input:** nums = [2,0,2,1,1,0]

**Output:** [0,0,1,1,2,2]

**Explanation:**

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

**Example 2:**

**Input:** nums = [2,0,1]

**Output:** [0,1,2]

**Explanation:**

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

**Constraints:**

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either 0, 1, or 2.

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?

## Hints

<details>
<summary>Hint 1</summary>

A rather straight forward solution is a two-pass algorithm using counting sort.

</details>

<details>
<summary>Hint 2</summary>

Iterate the array counting number of 0's, 1's, and 2's.

</details>

<details>
<summary>Hint 3</summary>

Overwrite array with the total number of 0's, then 1's and followed by 2's.

</details>

## Similar Questions

- [Sort List](https://leetcode.com/problems/sort-list/) - Medium
- [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/) - Medium
- [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
