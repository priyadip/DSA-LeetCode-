# 189. Rotate Array

**Difficulty:** Medium
**Topics:** Array, Math, Two Pointers

[View on LeetCode](https://leetcode.com/problems/rotate-array/)

## Description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

**Follow up:**

- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
- Could you do it in-place with `O(1)` extra space?

## Hints

<details>
<summary>Hint 1</summary>

The easiest solution would use additional memory and that is perfectly fine.

</details>

<details>
<summary>Hint 2</summary>

The actual trick comes when trying to solve this problem without using any additional memory. This means you need to use the original array somehow to move the elements around. Now, we can place each element in its original location and shift all the elements around it to adjust as that would be too costly and most likely will time out on larger input arrays.

</details>

<details>
<summary>Hint 3</summary>

One line of thought is based on reversing the array (or parts of it) to obtain the desired result. Think about how reversal might potentially help us out by using an example.

</details>

<details>
<summary>Hint 4</summary>

The other line of thought is a tad bit complicated but essentially it builds on the idea of placing each element in its original position while keeping track of the element originally in that position. Basically, at every step, we place an element in its rightful position and keep track of the element already there or the one being overwritten in an additional variable. We can't do this in one linear pass and the idea here is based on **cyclic-dependencies** between elements.

</details>

## Similar Questions

- [Rotate List](https://leetcode.com/problems/rotate-list/) - Medium
- [Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/) - Medium
- [Make K-Subarray Sums Equal](https://leetcode.com/problems/make-k-subarray-sums-equal/) - Medium
- [Maximum Number of Matching Indices After Right Shifts](https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
