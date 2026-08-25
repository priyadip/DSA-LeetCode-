# 3718. Smallest Missing Multiple of K

**Difficulty:** Easy
**Topics:** Array, Hash Table

[View on LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k/)

## Description

Given an integer array `nums` and an integer `k`, return the **smallest positive multiple** of `k` that is **missing** from `nums`.

A **multiple** of `k` is any positive integer divisible by `k`.

**Example 1:**

**Input:** nums = [8,2,3,4,6], k = 2

**Output:** 10

**Explanation:**

The multiples of `k = 2` are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from `nums` is 10.

**Example 2:**

**Input:** nums = [1,4,7,10,15], k = 5

**Output:** 5

**Explanation:**

The multiples of `k = 5` are 5, 10, 15, 20... and the smallest multiple missing from `nums` is 5.

**Constraints:**

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= k <= 100`

## Hints

<details>
<summary>Hint 1</summary>

Add the values in `nums` to a hash set

</details>

<details>
<summary>Hint 2</summary>

Iterate through the positive multiples of `k` and return the first one not in the hash set

</details>

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
