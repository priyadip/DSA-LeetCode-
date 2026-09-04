# 746. Min Cost Climbing Stairs

**Difficulty:** Easy
**Topics:** Array, Dynamic Programming

[View on LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/)

## Description

You are given an integer array `cost` where `cost[i]` is the cost of `i^th` step on a staircase.

Once you pay the cost, you can either climb **one** or **two** steps.

You can either start from the step with index 0, or the step with index 1.

Return the **minimum** cost to reach the top of the staircase, which is the position just past the last step (index `cost.length`).

**Example 1:**

```
Input: cost = [10,<u>15</u>,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

**Example 2:**

```
Input: cost = [<u>1</u>,100,<u>1</u>,1,<u>1</u>,100,<u>1</u>,<u>1</u>,100,<u>1</u>]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

**Constraints:**

- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`

## Hints

<details>
<summary>Hint 1</summary>

Build an array dp where dp[i] is the minimum cost to climb to the top starting from the ith staircase.

</details>

<details>
<summary>Hint 2</summary>

Assuming we have n staircase labeled from 0 to n - 1 and assuming the top is n, then dp[n] = 0, marking that if you are at the top, the cost is 0.

</details>

<details>
<summary>Hint 3</summary>

Now, looping from n - 1 to 0, the dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]). The answer will be the minimum of dp[0] and dp[1]

</details>

## Similar Questions

- [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) - Easy
- [Find Number of Ways to Reach the K-th Stair](https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
