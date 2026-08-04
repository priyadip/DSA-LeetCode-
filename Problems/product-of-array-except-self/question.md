# 238. Product of Array Except Self

**Difficulty:** Medium
**Topics:** Array, Prefix Sum

[View on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

## Description

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```
**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints:**

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

## Hints

<details>
<summary>Hint 1</summary>

Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?

</details>

<details>
<summary>Hint 2</summary>

Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?

</details>

## Similar Questions

- [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) - Hard
- [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) - Medium
- [Paint House II](https://leetcode.com/problems/paint-house-ii/) - Hard
- [Minimum Difference in Sums After Removal of Elements](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/) - Hard
- [Construct Product Matrix](https://leetcode.com/problems/construct-product-matrix/) - Medium
- [Find Sum of Array Product of Magical Sequences](https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
