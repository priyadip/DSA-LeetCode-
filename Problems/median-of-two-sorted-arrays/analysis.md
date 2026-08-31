# 4. Median of Two Sorted Arrays - Solution Analysis

## Problem Understanding
Given two sorted arrays of lengths `m` and `n`, find the median of the combined sorted array. The median is the middle element for odd total length, or the average of the two middle elements for even total length. The required time complexity is `O(log(m+n))`, which rules out merging (O(m+n)) and forces a binary-search approach. Constraints allow empty arrays (`m` or `n` can be 0) but guarantee at least one element total.

## Approach
The solution uses **binary search on the partition of the smaller array**. The brute-force merge takes O(m+n) time and O(m+n) space (or O(1) space with two pointers but still O(m+n) time). The key insight is that the median splits the combined array into two halves of equal size (or differing by one); if we pick a partition in the smaller array, the partition in the larger array is forced by the required total left size. We then only need to verify that the largest element on the left side of each array is ≤ the smallest element on the right side of the other array. This reduces the search space to the smaller array, giving O(log(min(m,n))) time and O(1) space.

## Algorithm
1. Ensure `nums1` is the smaller array (swap if necessary).
2. Set binary search bounds `left = 0`, `right = m` (number of elements taken from `nums1` can range from 0 to m).
3. While `left <= right`:
   - `partition1 = (left + right) // 2` (elements from `nums1` in left half).
   - `partition2 = (m + n + 1) // 2 - partition1` (elements from `nums2` in left half).
   - `left1 = nums1[partition1-1]` if `partition1 > 0` else `-inf`.
   - `right1 = nums1[partition1]` if `partition1 < m` else `+inf`.
   - `left2 = nums2[partition2-1]` if `partition2 > 0` else `-inf`.
   - `right2 = nums2[partition2]` if `partition2 < n` else `+inf`.
   - If `left1 <= right2` and `left2 <= right1`: correct partition found.
     - If total length odd: return `max(left1, left2)`.
     - Else: return `(max(left1, left2) + min(right1, right2)) / 2`.
   - Else if `left1 > right2`: move `right = partition1 - 1` (too many from `nums1`).
   - Else: move `left = partition1 + 1` (too few from `nums1`).

## Line-by-Line Explanation
- `if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1`: guarantees binary search runs on the smaller array for O(log(min(m,n))) complexity.
- `m = len(nums1); n = len(nums2)`: store lengths for repeated use.
- `left = 0; right = m`: search space for how many elements to take from `nums1` (0 … m inclusive).
- `while left <= right:`: standard binary search loop.
- `partition1 = (left + right) // 2`: candidate split point in `nums1`.
- `partition2 = (m + n + 1) // 2 - partition1`: forced split in `nums2` so total left count = ceil((m+n)/2).
- `left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]`: max of left part of `nums1`, `-inf` if empty.
- `right1 = float('inf') if partition1 == m else nums1[partition1]`: min of right part of `nums1`, `+inf` if empty.
- `left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]`: max of left part of `nums2`.
- `right2 = float('inf') if partition2 == n else nums2[partition2]`: min of right part of `nums2`.
- `if left1 <= right2 and left2 <= right1:`: partition is valid (all left elements ≤ all right elements).
- `if (m + n) % 2 == 1: return float(max(left1, left2))`: odd total length → median is the larger left element.
- `return (max(left1, left2) + min(right1, right2)) / 2`: even total length → average of two middle elements.
- `elif left1 > right2: right = partition1 - 1`: `nums1` contributes too many large elements; shrink its left part.
- `else: left = partition1 + 1`: `nums1` contributes too few; expand its left part.

## Dry Run
Example: `nums1 = [1,3]`, `nums2 = [2]` (m=2, n=1). After swap (since m>n): `nums1=[2]`, `nums2=[1,3]`, m=1, n=2.

| Step | left | right | partition1 | partition2 | left1 | right1 | left2 | right2 | Condition | Action |
|------|------|-------|------------|------------|-------|--------|-------|--------|-----------|--------|
| 1    | 0    | 1     | 0          | (3+1)//2-0=2 | -inf  | 2      | 3     | +inf   | left2(3) > right1(2) → else | left = 1 |
| 2    | 1    | 1     | 1          | 2-1=1      | 2     | +inf   | 1     | 3      | left1(2)≤right2(3) & left2(1)≤right1(inf) ✓ | odd total → return max(2,1)=2.0 |

Result: 2.0 ✓

## Complexity
- Time: O(log(min(m,n))), because binary search runs on the smaller array of length min(m,n) and each iteration does O(1) work.
- Space: O(1), only a constant number of variables are used regardless of input size.

## Edge Cases
- **One array empty**: e.g., `nums1=[]`, `nums2=[1]`. Swap makes `nums1=[1]`, `nums2=[]`. Loop runs with `m=1,n=0`. `partition2 = (1+0+1)//2 - partition1 = 1 - partition1`. When `partition1=1`, `partition2=0`. `left1=1`, `right1=inf`, `left2=-inf`, `right2=inf`. Condition holds, odd total → returns 1.0. Works.
- **All elements equal**: e.g., `nums1=[2,2]`, `nums2=[2,2]`. Partitions will satisfy `left1<=right2` and `left2<=right1` immediately; median computed correctly as 2.0.
- **Negative numbers**: Handled because comparisons use actual values; `-inf`/`inf` sentinels work for any integer range.
- **Maximum size (1000 each)**: Binary search depth ≤ log₂(1000) ≈ 10 iterations, well within limits.
- **Already sorted / reverse sorted**: Input is guaranteed sorted ascending; algorithm does not assume anything about relative ordering between arrays.

## Possible Improvements
The solution is already optimal in asymptotic complexity (O(log(min(m,n))) time, O(1) space) for the given constraints. A minor readability improvement would be to rename `left`/`right` to `lo`/`hi` or `low`/`high` to avoid confusion with the partition boundary variables `left1`/`left2`, but this is purely stylistic. No algorithmic improvement is possible without changing the complexity class.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
