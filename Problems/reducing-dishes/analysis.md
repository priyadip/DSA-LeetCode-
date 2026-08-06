# 1402. Reducing Dishes - Solution Analysis

## Problem Understanding
We are given an array `satisfaction` of length `n` (1 ≤ n ≤ 500) with values in [-1000, 1000]. We may choose any subset of dishes and cook them in any order; each dish takes 1 unit of time. The like-time coefficient of a dish cooked at time `t` is `t * satisfaction[i]`. We want the maximum possible sum of these coefficients. Because higher satisfaction should receive larger time multipliers, the optimal cooking order for any chosen subset is ascending satisfaction. The problem therefore reduces to selecting a suffix of the sorted array that maximizes the weighted sum.

## Approach
The solution uses a **greedy algorithm after sorting**. The key insight: after sorting `satisfaction` in non-decreasing order, the optimal subset of dishes to cook is always a contiguous suffix of this sorted array. We iterate from the largest satisfaction backwards, maintaining the sum of the current suffix (`suffixSum`). Adding the next dish (to the left) increases the total like-time coefficient by exactly the new `suffixSum` (all previously selected dishes get their time multiplier increased by 1). We continue while this marginal gain (`suffixSum`) is positive. This avoids O(n²) dynamic programming or brute-force subset enumeration.

## Algorithm
1. Sort `satisfaction` in non-decreasing order.
2. Initialize `suffixSum = 0` and `ans = 0`.
3. Iterate over `satisfaction` in reverse (from largest to smallest):
   a. Add current element `x` to `suffixSum`.
   b. If `suffixSum <= 0`, break the loop (further elements would only decrease the total).
   c. Add `suffixSum` to `ans`.
4. Return `ans`.

## Line-by-Line Explanation
- `satisfaction.sort()`: Sort ascending so that higher satisfaction values are at the end; the optimal cooking order for any chosen subset is this sorted order.
- `suffixSum = 0`: Tracks the sum of the currently selected suffix (dishes we have decided to cook).
- `ans = 0`: Accumulates the maximum total like-time coefficient.
- `for x in reversed(satisfaction):`: Process dishes from highest satisfaction to lowest, considering whether to prepend each to the current schedule.
- `suffixSum += x`: Include this dish in the suffix; its satisfaction contributes to the marginal gain of adding it at the front.
- `if suffixSum <= 0: break`: If the suffix sum becomes non-positive, adding this dish (and any further left dishes) would not increase the total, so stop.
- `ans += suffixSum`: The marginal increase in total like-time coefficient from prepending this dish equals the new suffix sum; add it to the answer.
- `return ans`: The accumulated maximum sum.

## Dry Run
Example 1: `satisfaction = [-1,-8,0,5,-9]`
Sorted: `[-9, -8, -1, 0, 5]`
Reverse iteration:

| Step | x    | suffixSum (before) | suffixSum (after) | suffixSum <= 0? | ans (before) | ans (after) | Action |
|------|------|--------------------|-------------------|-----------------|--------------|-------------|--------|
| 1    | 5    | 0                  | 5                 | False           | 0            | 5           | add 5  |
| 2    | 0    | 5                  | 5                 | False           | 5            | 10          | add 5  |
| 3    | -1   | 5                  | 4                 | False           | 10           | 14          | add 4  |
| 4    | -8   | 4                  | -4                | True            | 14           | 14          | break  |
| 5    | -9   | -                  | -                 | -               | -            | -           | loop ended |

Return 14. Matches example.

## Complexity
- Time: O(n log n), dominated by the sort. The reverse iteration is O(n).
- Space: O(1) extra space (ignoring the sort's internal space, which is O(n) for Timsort in Python, but typically considered O(1) auxiliary if we don't count input modification). The algorithm uses only a few variables.

## Edge Cases
- All negative satisfaction: e.g., `[-1,-4,-5]`. Sorted: `[-5,-4,-1]`. Reverse: `-1` -> `suffixSum=-1 <=0`, break immediately. `ans=0`. Correct (cook nothing).
- All positive: e.g., `[4,3,2]`. Sorted: `[2,3,4]`. Reverse: `4` (suffixSum=4, ans=4), `3` (suffixSum=7, ans=11), `2` (suffixSum=9, ans=20). Returns 20. Correct.
- Mixed with zero: zeros don't affect `suffixSum` positively but also not negatively; they are included if `suffixSum` stays positive.
- Single element: `[5]` -> `suffixSum=5`, `ans=5`. `[-5]` -> `suffixSum=-5 <=0`, break, `ans=0`.
- Large n up to 500: well within limits.
- The solution correctly handles the case where the optimal subset is empty (`ans=0`) by initializing `ans=0` and breaking before adding any negative `suffixSum`.

## Possible Improvements
The solution is already optimal in time complexity (O(n log n) due to sorting, which is necessary for the greedy suffix property) and space. One minor improvement: the loop could be written with a while loop and index to avoid creating a reversed iterator, but the difference is negligible. The variable names are clear. No redundant passes. The solution correctly implements the greedy insight and is optimal for the given constraints.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
