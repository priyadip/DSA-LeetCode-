# 3090. Maximum Length Substring With Two Occurrences

**Difficulty:** Easy
**Topics:** Hash Table, String, Sliding Window

[View on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)

## Description

Given a string `s`, return the **maximum** length of a substring such that it contains *at most two occurrences* of each character.

**Example 1:**

**Input:** s = "bcbbbcba"

**Output:** 4

**Explanation:**
 The following substring has a length of 4 and contains at most two occurrences of each character: `"bcbb<u>bcba</u>"`.

**Example 2:**

**Input:** s = "aaaa"

**Output:** 2

**Explanation:**
 The following substring has a length of 2 and contains at most two occurrences of each character: `"<u>aa</u>aa"`.

**Constraints:**

- `2 <= s.length <= 100`
- `s` consists only of lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

We can try all substrings by brute-force since the constraints are very small.

</details>

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
