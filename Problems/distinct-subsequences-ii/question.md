# 940. Distinct Subsequences II

**Difficulty:** Hard
**Topics:** String, Dynamic Programming

[View on LeetCode](https://leetcode.com/problems/distinct-subsequences-ii/)

## Description

Given a string s, return *the number of **distinct non-empty subsequences** of* `s`. Since the answer may be very large, return it **modulo** `10^9 + 7`.
 A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"<u>a</u>b<u>c</u>d<u>e</u>"` while `"aec"` is not.

**Example 1:**

```
Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
```

**Example 2:**

```
Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".
```

**Example 3:**

```
Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
```

**Constraints:**

- `1 <= s.length <= 2000`
- `s` consists of lowercase English letters.

## Similar Questions

- [Number of Unique Good Subsequences](https://leetcode.com/problems/number-of-unique-good-subsequences/) - Hard
- [Count K-Subsequences of a String With Maximum Beauty](https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
