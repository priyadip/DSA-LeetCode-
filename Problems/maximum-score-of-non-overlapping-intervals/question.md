# 3414. Maximum Score of Non-overlapping Intervals

**Difficulty:** Hard
**Topics:** Array, Binary Search, Dynamic Programming, Sorting

[View on LeetCode](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/)

## Description

You are given a 2D integer array `intervals`, where `intervals[i] = [l_i, r_i, weight_i]`. Interval `i` starts at position `l_i` and ends at `r_i`, and has a weight of `weight_i`. You can choose *up to* 4 **non-overlapping** intervals. The **score** of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from `intervals` with **maximum** score, representing your choice of non-overlapping intervals.

Two intervals are said to be **non-overlapping** if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

**Example 1:**

**Input:** intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

**Output:** [2,3]

**Explanation:**

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

**Example 2:**

**Input:** intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

**Output:** [1,3,5,6]

**Explanation:**

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

**Constraints:**

- `1 <= intevals.length <= 5 * 10^4`
- `intervals[i].length == 3`
- `intervals[i] = [l_i, r_i, weight_i]`
- `1 <= l_i <= r_i <= 10^9`
- `1 <= weight_i <= 10^9`

## Hints

<details>
<summary>Hint 1</summary>

Use Dynamic Programming.

</details>

<details>
<summary>Hint 2</summary>

Sort `intervals` by right boundary.

</details>

<details>
<summary>Hint 3</summary>

Let `dp[r][i]` denote the maximum score having picked `r` intervals from the prefix of `intervals` ending at index `i`.

</details>

<details>
<summary>Hint 4</summary>

`dp[r][i] = max(dp[r][i - 1], intervals[i][2] + dp[r][j])` where `j` is the largest index such that `intervals[j][1] < intervals[i][0]`.

</details>

<details>
<summary>Hint 5</summary>

Since `intervals` is sorted by right boundary, we can find index `j` using binary search.

</details>

## Similar Questions

- [Two Best Non-Overlapping Events](https://leetcode.com/problems/two-best-non-overlapping-events/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
