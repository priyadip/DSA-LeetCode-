# 49. Group Anagrams

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Sorting

[View on LeetCode](https://leetcode.com/problems/group-anagrams/)

## Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

**Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

- There is no string in strs that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

**Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

**Constraints:**

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Similar Questions

- [Valid Anagram](https://leetcode.com/problems/valid-anagram/) - Easy
- [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/) - Medium
- [Find Resultant Array After Removing Anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/) - Easy
- [Count Anagrams](https://leetcode.com/problems/count-anagrams/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
