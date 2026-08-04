# 600. Non-negative Integers without Consecutive Ones

**Difficulty:** Hard
**Topics:** Dynamic Programming

[View on LeetCode](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/)

## Description

Given a positive integer `n`, return the number of the integers in the range `[0, n]` whose binary representations **do not** contain consecutive ones.

**Example 1:**

```
Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
```

**Example 2:**

```
Input: n = 1
Output: 2
```

**Example 3:**

```
Input: n = 2
Output: 3
```

**Constraints:**

- `1 <= n <= 10^9`

## Similar Questions

- [House Robber](https://leetcode.com/problems/house-robber/) - Medium
- [House Robber II](https://leetcode.com/problems/house-robber-ii/) - Medium
- [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) - Medium
- [Generate Binary Strings Without Adjacent Zeros](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
