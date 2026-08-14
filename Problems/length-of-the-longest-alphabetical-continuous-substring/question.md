# 2414. Length of the Longest Alphabetical Continuous Substring

**Difficulty:** Medium
**Topics:** String

[View on LeetCode](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/)

## Description

An **alphabetical continuous string** is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string `"abcdefghijklmnopqrstuvwxyz"`.

- For example, `"abc"` is an alphabetical continuous string, while `"acb"` and `"za"` are not.

Given a string `s` consisting of lowercase letters only, return the *length of the **longest** alphabetical continuous substring.*

**Example 1:**

```
Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.
```

**Example 2:**

```
Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.
```

**Constraints:**

- `1 <= s.length <= 10^5`
- `s` consists of only English lowercase letters.

## Hints

<details>
<summary>Hint 1</summary>

What is the longest possible continuous substring?

</details>

<details>
<summary>Hint 2</summary>

The size of the longest possible continuous substring is at most 26, so we can just brute force the answer.

</details>

## Similar Questions

- [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) - Medium
- [Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/) - Medium
- [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) - Easy
- [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) - Medium
- [Number of Zero-Filled Subarrays](https://leetcode.com/problems/number-of-zero-filled-subarrays/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
