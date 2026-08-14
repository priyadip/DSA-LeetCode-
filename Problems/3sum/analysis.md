# 15. 3Sum - Solution Analysis

## Problem Understanding
Given an integer array `nums`, find all unique triplets `[nums[i], nums[j], nums[k]]` with distinct indices that sum to zero. The output must not contain duplicate triplets (order within a triplet and order of triplets in the output do not matter). Constraints: `3 <= n <= 3000`, values in `[-10^5, 10^5]`. The `n <= 3000` bound rules out O(n^3) brute force but allows O(n^2). Sorting is permitted and enables the two-pointer technique.

## Approach
The solution uses the **Two Pointers** pattern on a sorted array. After sorting, we fix the first element `nums[i]` and reduce the problem to finding two numbers in the remaining subarray that sum to `-nums[i]`. Because the subarray is sorted, we can use a left pointer `l` starting at `i+1` and a right pointer `r` starting at `n-1`, moving them inward based on whether the current sum is too small or too large. This avoids the O(n) hash-map lookup per element and achieves O(n^2) time with O(1) extra space (excluding output). The key insight: **sorting lets us skip duplicates deterministically and move pointers monotonically, guaranteeing each unique triplet is found exactly once.**

Brute force would be three nested loops O(n^3) with a set to deduplicate. The two-pointer approach reduces the inner search to O(n) per fixed `i`, giving O(n^2) overall.

## Algorithm
1. Sort `nums` in non-decreasing order.
2. Initialize empty result list `ans`.
3. Loop `i` from `0` to `n-3`:
   a. If `i > 0` and `nums[i] == nums[i-1]`, skip this `i` (duplicate first element).
   b. If `nums[i] > 0`, break (all remaining numbers are positive, sum cannot be zero).
   c. Set `l = i+1`, `r = n-1`.
   d. While `l < r`:
      - Compute `total = nums[i] + nums[l] + nums[r]`.
      - If `total > 0`: decrement `r` (need smaller sum).
      - Else if `total < 0`: increment `l` (need larger sum).
      - Else (`total == 0`):
        * Append `[nums[i], nums[l], nums[r]]` to `ans`.
        * Increment `l`, decrement `r`.
        * While `l < r` and `nums[l] == nums[l-1]`: increment `l` (skip duplicate second element).
        * While `l < r` and `nums[r] == nums[r+1]`: decrement `r` (skip duplicate third element).
4. Return `ans`.

## Line-by-Line Explanation
- `nums.sort()`: sorts the array so duplicates are adjacent and two-pointer logic works.
- `n = len(nums)`: stores length for loop bounds.
- `r = n-1`: initializes `r` (overwritten inside loop, harmless).
- `ans = []`: collects valid triplets.
- `for i in range(n-2):`: iterates first element index; need at least two elements after it.
- `if i > 0 and nums[i] == nums[i-1]: continue`: skips duplicate first elements to avoid duplicate triplets.
- `if nums[i] > 0: break`: since array is sorted, all subsequent `nums[i]` are positive; three positives cannot sum to zero.
- `l = i+1`: left pointer starts just after `i`.
- `r = n-1`: right pointer starts at end.
- `while l < r:`: standard two-pointer loop.
- `total = nums[i] + nums[l] + nums[r]`: current triplet sum.
- `if total > 0: r -= 1`: sum too large, move right pointer left to decrease sum.
- `elif total < 0: l += 1`: sum too small, move left pointer right to increase sum.
- `else:`: found a zero-sum triplet.
- `ans.append([nums[i], nums[l], nums[r]])`: records the triplet.
- `l += 1; r -= 1`: moves both pointers inward to search for next distinct pair.
- `while l < r and nums[l] == nums[l-1]: l += 1`: skips over duplicate values for the second element.
- `while l < r and nums[r] == nums[r+1]: r -= 1`: skips over duplicate values for the third element.
- `return ans`: returns all unique triplets.

## Dry Run
Example: `nums = [-1,0,1,2,-1,-4]`

After sort: `[-4, -1, -1, 0, 1, 2]`, `n=6`

| Step | i | nums[i] | l | r | nums[l] | nums[r] | total | Action |
|------|---|---------|---|---|---------|---------|-------|--------|
| 1 | 0 | -4 | 1 | 5 | -1 | 2 | -3 | total<0 → l=2 |
| 2 | 0 | -4 | 2 | 5 | -1 | 2 | -3 | total<0 → l=3 |
| 3 | 0 | -4 | 3 | 5 | 0 | 2 | -2 | total<0 → l=4 |
| 4 | 0 | -4 | 4 | 5 | 1 | 2 | -1 | total<0 → l=5 (loop ends) |
| 5 | 1 | -1 | 2 | 5 | -1 | 2 | 0 | append [-1,-1,2]; l=3,r=4; skip dups none |
| 6 | 1 | -1 | 3 | 4 | 0 | 1 | 0 | append [-1,0,1]; l=4,r=3 (loop ends) |
| 7 | 2 | -1 | skip (duplicate of i=1) | | | | | continue |
| 8 | 3 | 0 | 4 | 5 | 1 | 2 | 3 | total>0 → r=4 (loop ends) |
| 9 | 4 | 1 | break (nums[i]>0) | | | | | break |

Result: `[[-1,-1,2], [-1,0,1]]`

## Complexity
- Time: O(n^2). Sorting takes O(n log n). The outer loop runs O(n) times; the inner while loop moves `l` and `r` monotonically across the remaining array, so each iteration of the outer loop does O(n) work. Total O(n^2) dominates.
- Space: O(1) extra space (excluding output list). Sorting is in-place in Python (Timsort uses O(n) worst-case auxiliary, but typically considered O(1) extra for algorithm analysis; if strict, O(n) for sort stack). The `ans` list holds output, not counted in auxiliary space.

## Edge Cases
- **All zeros**: `nums = [0,0,0]` → sorted same; `i=0` finds triplet `[0,0,0]`; `i=1` skipped as duplicate; returns `[[0,0,0]]`. Works.
- **No valid triplet**: `nums = [0,1,1]` → sorted `[0,1,1]`; `i=0` (0) with `l=1,r=2` sum=2>0 → r moves to 1, loop ends; `i=1` (1) breaks because `nums[i]>0`. Returns `[]`. Works.
- **Duplicates at start**: `nums = [-2,-2,0,0,2,2]` → `i=0` finds `[-2,0,2]`; `i=1` skipped; `i=2` (0) breaks. Correctly deduplicates.
- **Large n (3000)**: O(n^2) ≈ 9M operations, well within limits.
- **Negative numbers only**: e.g., `[-5,-4,-3,-2,-1]` → `i=0` (-5) with two pointers never reaches zero; eventually `i` reaches end, returns `[]`. Works.
- **Early break correctness**: Since array sorted, once `nums[i] > 0`, all `nums[j] >= nums[i] > 0` for `j >= i`, so any triplet including `nums[i]` sums > 0. Break is safe.

## Possible Improvements
- The initial `r = n-1` before the loop is redundant (reassigned inside); remove it.
- Variable names `l` and `r` are acceptable but `left`/`right` would be clearer.
- The solution is already optimal in asymptotic complexity for the given constraints (O(n^2) time, O(1) extra space). No algorithmic improvement exists without changing the problem constraints (e.g., using hash maps still O(n^2) with more space).

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
