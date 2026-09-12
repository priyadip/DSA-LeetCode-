# 2054. Two Best Non-Overlapping Events

**Difficulty:** Medium
**Topics:** Array, Binary Search, Dynamic Programming, Sorting, Heap (Priority Queue)

[View on LeetCode](https://leetcode.com/problems/two-best-non-overlapping-events/)

## Description

You are given a **0-indexed** 2D integer array of `events` where `events[i] = [startTime_i, endTime_i, value_i]`. The `i^th` event starts at `startTime_i`_ and ends at `endTime_i`, and if you attend this event, you will receive a value of `value_i`. You can choose **at most** **two** **non-overlapping** events to attend such that the sum of their values is **maximized**.

Return *this **maximum** sum.*

Note that the start time and end time is **inclusive**: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time `t`, the next event must start at or after `t + 1`.

**Example 1:**
 ![](https://assets.leetcode.com/uploads/2026/01/03/untitled-diagramdrawio.png)
```
Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
```

**Example 2:**
 ![Example 1 Diagram](https://assets.leetcode.com/uploads/2026/01/03/2054b.png)
```
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.
```

**Example 3:**
 ![](https://assets.leetcode.com/uploads/2026/01/03/2054c.png)
```
Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
```

**Constraints:**

- `2 <= events.length <= 10^5`
- `events[i].length == 3`
- `1 <= startTime_i <= endTime_i <= 10^9`
- `1 <= value_i <= 10^6`

## Hints

<details>
<summary>Hint 1</summary>

How can sorting the events on the basis of their start times help? How about end times?

</details>

<details>
<summary>Hint 2</summary>

How can we quickly get the maximum score of an interval not intersecting with the interval we chose?

</details>

## Similar Questions

- [Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) - Hard
- [Maximum Number of Events That Can Be Attended II](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/) - Hard
- [Maximize Win From Two Segments](https://leetcode.com/problems/maximize-win-from-two-segments/) - Medium
- [Maximum Score of Non-overlapping Intervals](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
