# 650. 2 Keys Keyboard

**Difficulty:** Medium
**Topics:** Math, Dynamic Programming

[View on LeetCode](https://leetcode.com/problems/2-keys-keyboard/)

## Description

There is only one character `'A'` on the screen of a notepad. You can perform one of two operations on this notepad for each step:

- Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
- Paste: You can paste the characters which are copied last time.

Given an integer `n`, return *the minimum number of operations to get the character* `'A'` *exactly* `n` *times on the screen*.

**Example 1:**

```
Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
```

**Example 2:**

```
Input: n = 1
Output: 0
```

**Constraints:**

- `1 <= n <= 1000`

## Hints

<details>
<summary>Hint 1</summary>

How many characters may be there in the clipboard at the last step if n = 3? n = 7? n = 10? n = 24?

</details>

## Similar Questions

- [4 Keys Keyboard](https://leetcode.com/problems/4-keys-keyboard/) - Medium
- [Broken Calculator](https://leetcode.com/problems/broken-calculator/) - Medium
- [Smallest Value After Replacing With Sum of Prime Factors](https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/) - Medium
- [Distinct Prime Factors of Product of Array](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
