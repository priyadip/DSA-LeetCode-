# 2213. Longest Substring of One Repeating Character

**Difficulty:** Hard
**Topics:** Array, String, Segment Tree, Ordered Set

[View on LeetCode](https://leetcode.com/problems/longest-substring-of-one-repeating-character/)

## Description

You are given a **0-indexed** string `s`. You are also given a **0-indexed** string `queryCharacters` of length `k` and a **0-indexed** array of integer **indices** `queryIndices` of length `k`, both of which are used to describe `k` queries.

The `i^th` query updates the character in `s` at index `queryIndices[i]` to the character `queryCharacters[i]`.

Return *an array* `lengths` *of length *`k`* where* `lengths[i]` *is the **length** of the **longest substring** of *`s`* consisting of **only one repeating** character **after** the* `i^th` *query** is performed.*

**Example 1:**

```
Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation:
- 1^st query updates s = "<u>bbb</u>acc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2^nd query updates s = "bbb<u>ccc</u>".
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3^rd query updates s = "<u>bbbb</u>cc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].
```

**Example 2:**

```
Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1^st query updates s = "aba<u>zz</u>". The longest substring consisting of one repeating character is "zz" with length 2.
- 2^nd query updates s = "<u>aaa</u>zz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].
```

**Constraints:**

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `k == queryCharacters.length == queryIndices.length`
- `1 <= k <= 10^5`
- `queryCharacters` consists of lowercase English letters.
- `0 <= queryIndices[i] < s.length`

## Hints

<details>
<summary>Hint 1</summary>

Use a segment tree to perform fast point updates and range queries.

</details>

<details>
<summary>Hint 2</summary>

We need each segment tree node to store the length of the longest substring of that segment consisting of only 1 repeating character.

</details>

<details>
<summary>Hint 3</summary>

We will also have each segment tree node store the leftmost and rightmost character of the segment, the max length of a prefix substring consisting of only 1 repeating character, and the max length of a suffix substring consisting of only 1 repeating character.

</details>

<details>
<summary>Hint 4</summary>

Use this information to properly merge the two segment tree nodes together.

</details>

## Similar Questions

- [Merge Intervals](https://leetcode.com/problems/merge-intervals/) - Medium
- [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) - Medium
- [Consecutive Characters](https://leetcode.com/problems/consecutive-characters/) - Easy
- [Create Sorted Array through Instructions](https://leetcode.com/problems/create-sorted-array-through-instructions/) - Hard
- [Longest Increasing Subsequence II](https://leetcode.com/problems/longest-increasing-subsequence-ii/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
