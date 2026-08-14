# 42. Trapping Rain Water - Solution Analysis

## Problem Understanding
Given an array of non-negative integers where each value represents the height of a unit-width bar, compute the total volume of water that can be trapped between the bars after rain. Water trapped at any index depends on the tallest bars to its left and right; the water level is the minimum of those two maxima minus the current bar's height. The array length can reach 20,000, so an O(n) or O(n log n) solution is required; O(1) extra space is achievable.

## Approach
The solution uses the **two pointers** pattern. A brute-force approach would compute left and right maxima for every index, costing O(n) time with O(n) extra space for prefix/suffix arrays. The two-pointer method eliminates the extra space by observing that when `height[l] <= height[r]`, the water at `l` is bounded by `left_max` (since `right_max` is at least `height[r] >= height[l]`), so we can safely process the left side and move `l` inward; symmetrically for the right side. The key insight: **the side with the lower wall determines the trapped water for its current pointer because the opposite side's maximum is guaranteed to be at least as high.**

## Algorithm
1. Initialize `l = 0`, `r = len(height) - 1`, `left_max = 0`, `right_max = 0`, `water = 0`.
2. While `l < r`:
   a. If `height[l] <= height[r]`:
      - If `height[l] >= left_max`, update `left_max = height[l]`.
      - Else, add `left_max - height[l]` to `water`.
      - Increment `l`.
   b. Else (`height[l] > height[r]`):
      - If `height[r] >= right_max`, update `right_max = height[r]`.
      - Else, add `right_max - height[r]` to `water`.
      - Decrement `r`.
3. Return `water`.

## Line-by-Line Explanation
- `l, r = 0, len(height) - 1`: start pointers at both ends of the elevation map.
- `left_max = right_max = 0`: track the highest walls seen so far from each side.
- `water = 0`: accumulator for total trapped water.
- `while l < r:`: process until pointers meet; when they meet no new water can be trapped.
- `if height[l] <= height[r]:`: the left wall is lower or equal, so left side's max is the limiting factor.
- `if height[l] >= left_max:`: current bar is a new highest wall on the left.
- `left_max = height[l]`: update the left maximum; no water trapped here because bar is the wall.
- `else:`: current bar is lower than `left_max`, so water can sit on top of it.
- `water += left_max - height[l]`: add the difference between the bounding wall and current height.
- `l += 1`: move left pointer inward after processing.
- `else:`: symmetric case where right wall is lower.
- `if height[r] >= right_max:`: new highest wall on the right.
- `right_max = height[r]`: update right maximum.
- `else:`: current right bar is lower than `right_max`.
- `water += right_max - height[r]`: accumulate trapped water on the right.
- `r -= 1`: move right pointer inward.
- `return water`: total trapped water after all positions processed.

## Dry Run
Trace of Example 1: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`

| Step | l | r | height[l] | height[r] | left_max | right_max | water | Action |
|------|---|---|-----------|-----------|----------|-----------|-------|--------|
| 0 | 0 | 11 | 0 | 1 | 0 | 0 | 0 | initial |
| 1 | 0 | 11 | 0 | 1 | 0 | 0 | 0 | 0<=1, 0>=0 → left_max=0, l=1 |
| 2 | 1 | 11 | 1 | 1 | 0 | 0 | 0 | 1<=1, 1>=0 → left_max=1, l=2 |
| 3 | 2 | 11 | 0 | 1 | 1 | 0 | 0 | 0<=1, 0<1 → water+=1, l=3 |
| 4 | 3 | 11 | 2 | 1 | 1 | 0 | 1 | 2>1 → 1>=0 → right_max=1, r=10 |
| 5 | 3 | 10 | 2 | 2 | 1 | 1 | 1 | 2<=2, 2>=1 → left_max=2, l=4 |
| 6 | 4 | 10 | 1 | 2 | 2 | 1 | 1 | 1<=2, 1<2 → water+=1, l=5 |
| 7 | 5 | 10 | 0 | 2 | 2 | 1 | 2 | 0<=2, 0<2 → water+=2, l=6 |
| 8 | 6 | 10 | 1 | 2 | 2 | 1 | 4 | 1<=2, 1<2 → water+=1, l=7 |
| 9 | 7 | 10 | 3 | 2 | 2 | 1 | 5 | 3>2 → 2>=1 → right_max=2, r=9 |
| 10 | 7 | 9 | 3 | 1 | 2 | 2 | 5 | 3>1 → 1<2 → water+=1, r=8 |
| 11 | 7 | 8 | 3 | 2 | 2 | 2 | 6 | 3>2 → 2>=2 → right_max=2, r=7 |
| 12 | 7 | 7 | – | – | 2 | 2 | 6 | loop ends (l==r) |

Final `water = 6`.

## Complexity
- Time: O(n), where n = len(height). Each pointer moves at most n steps, and each step does O(1) work.
- Space: O(1). Only a constant number of integer variables are used.

## Edge Cases
- **Single element (n=1)**: loop condition `l < r` is false immediately, returns 0. Correct because no water can be trapped.
- **All equal heights**: e.g., `[5,5,5]`. The algorithm never adds water because `height[l] >= left_max` and `height[r] >= right_max` always hold. Returns 0.
- **Strictly increasing / decreasing**: e.g., `[1,2,3,4]` or `[4,3,2,1]`. Water remains 0 because one side always updates its max without trapping.
- **Maximum constraints**: n = 2·10��, heights up to 10��. The loop runs ≤ 2·10�� iterations; water sum fits easily in Python's arbitrary-precision integers.
- **Zero heights**: Handled naturally; `left_max`/`right_max` start at 0 and update correctly.

## Possible Improvements
The solution is already optimal for the given constraints: O(n) time and O(1) space is the best possible asymptotic complexity. Variable names are clear (`left_max`, `right_max`, `water`). No redundant passes or data structures. No further improvements are necessary.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
