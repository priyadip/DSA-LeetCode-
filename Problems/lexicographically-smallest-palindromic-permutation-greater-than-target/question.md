# 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target

**Difficulty:** Hard
**Topics:** Two Pointers, String, Enumeration

[View on LeetCode](https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/)

## Description

You are given two strings `s` and `target`, each of length `n`, consisting of lowercase English letters.

Return the **lexicographically smallest string** that is **both** a **palindromic permutation** of `s` and **strictly** greater than `target`. If no such permutation exists, return an empty string.

**Example 1:**

**Input:** s = "baba", target = "abba"

**Output:** "baab"

**Explanation:**

- The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`.
- The lexicographically smallest permutation that is strictly greater than `target` is `"baab"`.

**Example 2:**

**Input:** s = "baba", target = "bbaa"

**Output:** ""

**Explanation:**

- The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`.
- None of them is lexicographically strictly greater than `target`. Therefore, the answer is `""`.

**Example 3:**

**Input:** s = "abc", target = "abb"

**Output:** ""

**Explanation:**

`s` has no palindromic permutations. Therefore, the answer is `""`.

**Example 4:**

**Input:** s = "aac", target = "abb"

**Output:** "aca"

**Explanation:**

- The only palindromic permutation of `s` is `"aca"`.
- `"aca"` is strictly greater than `target`. Therefore, the answer is `"aca"`.

**Constraints:**

- `1 <= n == s.length == target.length <= 300`
- `s` and `target` consist of only lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

A palindromic permutation exists only if at most one character has an odd count (for odd-length strings) or all counts are even (for even-length strings).

</details>

<details>
<summary>Hint 2</summary>

Focus on constructing the first half of the palindrome. The second half is determined by mirroring.

</details>

<details>
<summary>Hint 3</summary>

To be lexicographically greater than target, the first half must be greater than or equal to target's first half, with careful handling of the middle character for odd-length strings.

</details>

<details>
<summary>Hint 4</summary>

Use a backtracking approach or greedy selection for each position in the first half, trying the smallest available character that can still produce a valid palindrome.

</details>

<details>
<summary>Hint 5</summary>

After building the first half, mirror it (and add the middle character if needed) to form the full palindrome and verify it is strictly greater than target.

</details>

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
