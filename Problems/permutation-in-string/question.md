# 567. Permutation in String

**Difficulty:** Medium
**Topics:** Hash Table, Two Pointers, String, Sliding Window

[View on LeetCode](https://leetcode.com/problems/permutation-in-string/)

## Description

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example 1:**

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

**Constraints:**

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Obviously, brute force will result in TLE. Think of something else.

</details>

<details>
<summary>Hint 2</summary>

How will you check whether one string is a permutation of another string?

</details>

<details>
<summary>Hint 3</summary>

One way is to sort the string and then compare. But, Is there a better way?

</details>

<details>
<summary>Hint 4</summary>

If one string is a permutation of another string then they must have one common metric. What is that?

</details>

<details>
<summary>Hint 5</summary>

Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?

</details>

<details>
<summary>Hint 6</summary>

What about hash table? An array of size 26?

</details>

## Similar Questions

- [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) - Hard
- [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
