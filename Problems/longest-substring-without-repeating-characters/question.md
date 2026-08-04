# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Topics:** Hash Table, String, Sliding Window

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Description

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Constraints:**

- `0 <= s.length <= 10^5`
- `s` consists of English letters, digits, symbols and spaces.

## Hints

<details>
<summary>Hint 1</summary>

There are less than 100 unique characters. We can check all substrings with length at most 100 for example. This is a good enough approximation.

</details>

## Similar Questions

- [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) - Medium
- [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) - Medium
- [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) - Hard
- [Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/) - Medium
- [Number of Equal Count Substrings](https://leetcode.com/problems/number-of-equal-count-substrings/) - Medium
- [Minimum Consecutive Cards to Pick Up](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/) - Medium
- [Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray/) - Medium
- [Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/) - Medium
- [Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array/) - Medium
- [Find Longest Special Substring That Occurs Thrice II](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/) - Medium
- [Find Longest Special Substring That Occurs Thrice I](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
