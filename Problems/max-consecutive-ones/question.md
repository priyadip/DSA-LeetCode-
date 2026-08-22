# 485. Max Consecutive Ones

**Difficulty:** Easy
**Topics:** Array

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)

## Description

Given a binary array `nums`, return *the maximum number of consecutive *`1`*'s in the array*.

**Example 1:**

```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

**Example 2:**

```
Input: nums = [1,0,1,1,0,1]
Output: 2
```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Hints

<details>
<summary>Hint 1</summary>

You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.

</details>

## Similar Questions

- [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) - Medium
- [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) - Medium
- [Consecutive Characters](https://leetcode.com/problems/consecutive-characters/) - Easy
- [Longer Contiguous Segments of Ones than Zeros](https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/) - Easy
- [Length of the Longest Alphabetical Continuous Substring](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/) - Medium
- [Maximum Enemy Forts That Can Be Captured](https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/) - Easy

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
