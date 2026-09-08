# 149. Max Points on a Line - Solution Analysis

## Problem Understanding
Given an array of unique 2D points, find the maximum number of points that lie on a single straight line. The constraints (n ≤ 300, coordinates up to 10⁴) allow an O(n²) solution. Since all points are unique, duplicate handling is technically unnecessary but included for completeness. The core challenge is representing slopes exactly to avoid floating-point precision errors when grouping collinear points.

## Approach
The solution uses a **hash map with slope normalization** pattern. For each point i, it computes the slope to every other point j > i, normalizes the slope vector (dx, dy) by dividing by their GCD, and counts occurrences of each normalized slope in a hash map. The most frequent slope from point i indicates the line through i with the most other points. This avoids the O(n³) brute force of checking all triplets for collinearity. The key insight is that two vectors represent the same slope iff their reduced forms (dx/gcd, dy/gcd) are identical, which handles vertical/horizontal lines and sign consistency without special cases.

## Algorithm
1. If points ≤ 2, return the count (any 2 points define a line).
2. Initialize global max_points = 0.
3. For each point i from 0 to n-1:
   a. Create empty hash map slope_map and set overlap = 0, curr_max = 0.
   b. For each point j from i+1 to n-1:
      i. Compute dx = x_j - x_i, dy = y_j - y_i.
      ii. If dx == 0 and dy == 0: increment overlap (duplicate point).
      iii. Else: compute gcd_val = gcd(dx, dy), normalize slope = (dx//gcd_val, dy//gcd_val).
      iv. Increment slope_map[slope], update curr_max = max(curr_max, slope_map[slope]).
   c. Update max_points = max(max_points, curr_max + overlap + 1).
4. Return max_points.

## Line-by-Line Explanation
`if len(points) <= 2: return len(points)`: Handles trivial cases where all points are collinear by definition.

`max_points = 0`: Tracks the global maximum across all anchor points.

`for i in range(len(points)):`: Iterates each point as the anchor for slope calculations.

`slope_map = defaultdict(int)`: Maps normalized slope tuples to their frequency from point i.

`overlap = 0`: Counts duplicate points (always 0 per constraints, but kept for correctness).

`curr_max = 0`: Tracks the maximum frequency of any single slope from point i.

`for j in range(i + 1, len(points)):`: Only checks j > i to avoid double-counting pairs and self-comparison.

`dx = points[j][0] - points[i][0]`: Computes x-difference for slope vector.

`dy = points[j][1] - points[i][1]`: Computes y-difference for slope vector.

`if dx == 0 and dy == 0: overlap += 1; continue`: Detects duplicate points (not possible per constraints).

`gcd_val = self.gcd(dx, dy)`: Computes greatest common divisor to reduce the slope vector.

`slope = (dx // gcd_val, dy // gcd_val)`: Normalizes slope to canonical integer representation; handles signs and vertical/horizontal lines uniformly.

`slope_map[slope] += 1`: Increments count for this normalized slope.

`curr_max = max(curr_max, slope_map[slope])`: Updates the most frequent slope count for this anchor.

`max_points = max(max_points, curr_max + overlap + 1)`: Adds 1 for the anchor point itself; updates global maximum.

`def gcd(self, a, b): while b: a, b = b, a % b; return a`: Euclidean algorithm for GCD; works with negative inputs because Python's modulo yields non-negative remainder when divisor is positive, but here a,b can be negative - however, the loop terminates correctly and returns a non-negative GCD since the final `a` is the last non-zero remainder. The sign of the normalized slope is preserved by the division `dx // gcd_val`, `dy // gcd_val`.

## Dry Run
Trace Example 1: `points = [[1,1],[2,2],[3,3]]`

| Step | i | j | dx | dy | gcd_val | slope | slope_map | curr_max | overlap | Action |
|------|---|---|----|----|---------|-------|-----------|----------|---------|--------|
| 1 | 0 | 1 | 1 | 1 | 1 | (1,1) | {(1,1):1} | 1 | 0 | store slope |
| 2 | 0 | 2 | 2 | 2 | 2 | (1,1) | {(1,1):2} | 2 | 0 | increment slope |
| 3 | 1 | 2 | 1 | 1 | 1 | (1,1) | {(1,1):1} | 1 | 0 | store slope |

After i=0: `max_points = max(0, 2+0+1) = 3`  
After i=1: `max_points = max(3, 1+0+1) = 3`  
Return 3.

## Complexity
- Time: O(n²), where n = len(points) ≤ 300. The double loop visits each pair once; GCD runs in O(log C) with C ≤ 10⁴, treated as O(1).
- Space: O(n). The `slope_map` holds at most n‑1 entries per anchor point and is recreated each outer iteration.

## Edge Cases
- **n = 1 or 2**: Handled by the initial guard `if len(points) <= 2`.
- **All points collinear**: The slope map accumulates n‑1 entries for the first anchor, yielding correct max.
- **Vertical lines (dx = 0)**: GCD normalises to `(0, 1)` for both positive and negative dy.
- **Horizontal lines (dy = 0)**: Normalises to `(1, 0)`.
- **Negative coordinates**: GCD and integer division produce a canonical slope tuple (e.g., (1,2) and (-1,-2) both become (1,2)).
- **Duplicate points**: Constraints guarantee uniqueness, but the `overlap` counter would handle them if present.

## Possible Improvements
- **Missing import**: `defaultdict` requires `from collections import defaultdict`; the snippet relies on LeetCode's environment.
- **Redundant overlap logic**: Since points are unique, `overlap` is always 0; removing it simplifies the code.
- **Use `math.gcd`**: The standard library `math.gcd` (Python ≥3.5) returns a non‑negative GCD and is implemented in C, slightly faster.
- The algorithm is already optimal for the given constraints (O(n²) time, O(n) space); no asymptotic improvement exists.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
