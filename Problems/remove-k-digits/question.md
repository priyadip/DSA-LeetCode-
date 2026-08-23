# 402. Remove K Digits

**Difficulty:** Medium
**Topics:** String, Stack, Greedy, Monotonic Stack

[View on LeetCode](https://leetcode.com/problems/remove-k-digits/)

## Description

Given string num representing a non-negative integer `num`, and an integer `k`, return *the smallest possible integer after removing* `k` *digits from* `num`.

**Example 1:**

```
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
```

**Example 2:**

```
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
```

**Example 3:**

```
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
```

**Constraints:**

- `1 <= k <= num.length <= 10^5`
- `num` consists of only digits.
- `num` does not have any leading zeros except for the zero itself.

## Similar Questions

- [Create Maximum Number](https://leetcode.com/problems/create-maximum-number/) - Hard
- [Monotone Increasing Digits](https://leetcode.com/problems/monotone-increasing-digits/) - Medium
- [Find the Most Competitive Subsequence](https://leetcode.com/problems/find-the-most-competitive-subsequence/) - Medium
- [Append K Integers With Minimal Sum](https://leetcode.com/problems/append-k-integers-with-minimal-sum/) - Medium
- [Remove Digit From Number to Maximize Result](https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/) - Easy
- [Minimum Operations to Make a Special Number](https://leetcode.com/problems/minimum-operations-to-make-a-special-number/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
