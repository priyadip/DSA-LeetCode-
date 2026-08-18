# 209. Minimum Size Subarray Sum

**Difficulty:** Medium
**Topics:** Array, Binary Search, Sliding Window, Prefix Sum

[View on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)

## Description

Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a **subarray** whose sum is greater than or equal to* `target`. If there is no such subarray, return `0` instead.

**Example 1:**

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

**Example 2:**

```
Input: target = 4, nums = [1,4,4]
Output: 1
```

**Example 3:**

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

**Constraints:**

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

 **Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## Similar Questions

- [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) - Hard
- [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) - Medium
- [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) - Medium
- [Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) - Medium
- [K Radius Subarray Averages](https://leetcode.com/problems/k-radius-subarray-averages/) - Medium
- [Maximum Product After K Increments](https://leetcode.com/problems/maximum-product-after-k-increments/) - Medium
- [Shortest Subarray With OR at Least K I](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/) - Easy
- [Minimum Positive Sum Subarray ](https://leetcode.com/problems/minimum-positive-sum-subarray/) - Easy

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
