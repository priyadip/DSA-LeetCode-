# 5. Longest Palindromic Substring

**Difficulty:** Medium
**Topics:** Two Pointers, String, Dynamic Programming, Manacher

[View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)

## Description

Given a string `s`, return *the longest* *palindromic* *substring* in `s`.

**Example 1:**

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**

```
Input: s = "cbbd"
Output: "bb"
```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Hints

<details>
<summary>Hint 1</summary>

How can we reuse a previously computed palindrome to compute a larger palindrome?

</details>

<details>
<summary>Hint 2</summary>

If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?

</details>

<details>
<summary>Hint 3</summary>

Complexity based hint: If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

</details>

## Similar Questions

- [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) - Hard
- [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) - Easy
- [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) - Hard
- [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) - Medium
- [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) - Medium
- [Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
