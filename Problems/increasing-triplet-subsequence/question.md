# 334. Increasing Triplet Subsequence

**Difficulty:** Medium
**Topics:** Array, Greedy, Longest Increasing Subsequence

[View on LeetCode](https://leetcode.com/problems/increasing-triplet-subsequence/)

## Description

Given an integer array `nums`, return `true`* if there exists a triple of indices *`(i, j, k)`* such that *`i < j < k`* and *`nums[i] < nums[j] < nums[k]`. If no such indices exists, return `false`.

**Example 1:**

```
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
```

**Example 2:**

```
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
```

**Example 3:**

```
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
```

**Constraints:**

- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

 **Follow up:** Could you implement a solution that runs in `O(n)` time complexity and `O(1)` space complexity?

## Similar Questions

- [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) - Medium
- [Count Special Quadruplets](https://leetcode.com/problems/count-special-quadruplets/) - Easy
- [Count Good Triplets in an Array](https://leetcode.com/problems/count-good-triplets-in-an-array/) - Hard
- [Count Increasing Quadruplets](https://leetcode.com/problems/count-increasing-quadruplets/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
