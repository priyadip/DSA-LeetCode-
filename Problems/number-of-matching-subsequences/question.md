# 792. Number of Matching Subsequences

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Binary Search, Dynamic Programming, Trie, Sorting

[View on LeetCode](https://leetcode.com/problems/number-of-matching-subsequences/)

## Description

Given a string `s` and an array of strings `words`, return *the number of* `words[i]` *that is a subsequence of* `s`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

**Example 1:**

```
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
```

**Example 2:**

```
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
```

**Constraints:**

- `1 <= s.length <= 5 * 10^4`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 50`
- `s` and `words[i]` consist of only lowercase English letters.

## Similar Questions

- [Is Subsequence](https://leetcode.com/problems/is-subsequence/) - Easy
- [Shortest Way to Form String](https://leetcode.com/problems/shortest-way-to-form-string/) - Medium
- [Count Vowel Substrings of a String](https://leetcode.com/problems/count-vowel-substrings-of-a-string/) - Easy

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
