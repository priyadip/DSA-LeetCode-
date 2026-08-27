# 3720. Lexicographically Smallest Permutation Greater Than Target

**Difficulty:** Medium
**Topics:** Hash Table, String, Greedy, Counting, Enumeration

[View on LeetCode](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/)

## Description

You are given two strings `s` and `target`, both having length `n`, consisting of lowercase English letters.

Return the **lexicographically smallest permutation** of `s` that is **strictly** greater than `target`. If no permutation of `s` is lexicographically strictly greater than `target`, return an empty string.

A string `a` is **lexicographically strictly greater **than a string `b` (of the same length) if in the first position where `a` and `b` differ, string `a` has a letter that appears later in the alphabet than the corresponding letter in `b`.

**Example 1:**

**Input:** s = "abc", target = "bba"

**Output:** "bca"

**Explanation:**

- The permutations of `s` (in lexicographical order) are `"abc"`, `"acb"`, `"bac"`, `"bca"`, `"cab"`, and `"cba"`.
- The lexicographically smallest permutation that is strictly greater than `target` is `"bca"`.

**Example 2:**

**Input:** s = "leet", target = "code"

**Output:** "eelt"

**Explanation:**

- The permutations of `s` (in lexicographical order) are `"eelt"`, `"eetl"`, `"elet"`, `"elte"`, `"etel"`, `"etle"`, `"leet"`, `"lete"`, `"ltee"`, `"teel"`, `"tele"`, and `"tlee"`.
- The lexicographically smallest permutation that is strictly greater than `target` is `"eelt"`.

**Example 3:**

**Input:** s = "baba", target = "bbaa"

**Output:** ""

**Explanation:**

- The permutations of `s` (in lexicographical order) are `"aabb"`, `"abab"`, `"abba"`, `"baab"`, `"baba"`, and `"bbaa"`.
- None of them is lexicographically strictly greater than `target`. Therefore, the answer is `""`.

**Constraints:**

- `1 <= s.length == target.length <= 300`
- `s` and `target` consist of only lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Maintain frequency counts of `s`.

</details>

<details>
<summary>Hint 2</summary>

Walk left-to-right; if equal to `target[i]` is possible, take it and continue.

</details>

<details>
<summary>Hint 3</summary>

If not, try the smallest letter strictly greater than `target[i]`.

</details>

<details>
<summary>Hint 4</summary>

If neither, backtrack left to the most recent index where you matched `target` and try to bump there.

</details>

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
