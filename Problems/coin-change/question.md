# 322. Coin Change

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Breadth-First Search, Knapsack Problem, Complete Knapsack

[View on LeetCode](https://leetcode.com/problems/coin-change/)

## Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the fewest number of coins that you need to make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**

```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3:**

```
Input: coins = [1], amount = 0
Output: 0
```

**Constraints:**

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Similar Questions

- [Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/) - Medium
- [Maximum Value of K Coins From Piles](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/) - Hard
- [Minimum Number of Operations to Convert Time](https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/) - Easy
- [Minimum Cost to Split an Array](https://leetcode.com/problems/minimum-cost-to-split-an-array/) - Hard
- [Count of Sub-Multisets With Bounded Sum](https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/) - Hard
- [Length of the Longest Subsequence That Sums to Target](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/) - Medium
- [Minimum Number of Coins to be Added](https://leetcode.com/problems/minimum-number-of-coins-to-be-added/) - Medium
- [Most Expensive Item That Can Not Be Bought](https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/) - Medium
- [Inverse Coin Change](https://leetcode.com/problems/inverse-coin-change/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
