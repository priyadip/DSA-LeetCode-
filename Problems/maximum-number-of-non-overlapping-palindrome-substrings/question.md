# 2472. Maximum Number of Non-overlapping Palindrome Substrings

**Difficulty:** Hard
**Topics:** Two Pointers, String, Dynamic Programming, Greedy

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)

## Description

You are given a string `s` and a **positive** integer `k`.

Select a set of **non-overlapping** substrings from the string `s` that satisfy the following conditions:

- The **length** of each substring is **at least** `k`.
- Each substring is a **palindrome**.

Return *the **maximum** number of substrings in an optimal selection*.

A **substring** is a contiguous sequence of characters within a string.

**Example 1:**

```
Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "<u>aba</u>cc<u>dbbd</u>". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
```

**Example 2:**

```
Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.
```

**Constraints:**

- `1 <= k <= s.length <= 2000`
- `s` consists of lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Try to use dynamic programming to solve the problem.

</details>

<details>
<summary>Hint 2</summary>

let dp[i] be the answer for the prefix s[0…i].

</details>

<details>
<summary>Hint 3</summary>

The final answer to the problem will be dp[n-1]. How do you compute this dp?

</details>

## Similar Questions

- [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) - Medium
- [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) - Medium
- [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) - Hard
- [Palindrome Partitioning III](https://leetcode.com/problems/palindrome-partitioning-iii/) - Hard
- [Maximum Number of Non-Overlapping Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) - Hard
- [Palindrome Partitioning IV](https://leetcode.com/problems/palindrome-partitioning-iv/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
