# 1679. Max Number of K-Sum Pairs

**Difficulty:** Medium
**Topics:** Array, Hash Table, Two Pointers, Sorting

[View on LeetCode](https://leetcode.com/problems/max-number-of-k-sum-pairs/)

## Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return *the maximum number of operations you can perform on the array*.

**Example 1:**

```
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
```

**Example 2:**

```
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

## Hints

<details>
<summary>Hint 1</summary>

The abstract problem asks to count the number of disjoint pairs with a given sum k.

</details>

<details>
<summary>Hint 2</summary>

For each possible value x, it can be paired up with k - x.

</details>

<details>
<summary>Hint 3</summary>

The number of such pairs equals to min(count(x), count(k-x)), unless that x = k / 2, where the number of such pairs will be floor(count(x) / 2).

</details>

## Similar Questions

- [Two Sum](https://leetcode.com/problems/two-sum/) - Easy
- [Count Good Meals](https://leetcode.com/problems/count-good-meals/) - Medium
- [Divide Players Into Teams of Equal Skill](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
