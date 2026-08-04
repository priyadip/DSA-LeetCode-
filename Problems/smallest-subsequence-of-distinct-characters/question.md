# 1081. Smallest Subsequence of Distinct Characters

**Difficulty:** Medium
**Topics:** String, Stack, Greedy, Monotonic Stack

[View on LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)

## Description

Given a string `s`, return *the **lexicographically smallest* *subsequence** of* `s` *that contains all the distinct characters of* `s` *exactly once*.

**Example 1:**

```
Input: s = "bcabc"
Output: "abc"
```

**Example 2:**

```
Input: s = "cbacdcbc"
Output: "acdb"
```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

 **Note:** This question is the same as 316: [https://leetcode.com/problems/remove-duplicate-letters/](https://leetcode.com/problems/remove-duplicate-letters/)

## Hints

<details>
<summary>Hint 1</summary>

Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.

</details>

## Similar Questions

- [Find the Most Competitive Subsequence](https://leetcode.com/problems/find-the-most-competitive-subsequence/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
