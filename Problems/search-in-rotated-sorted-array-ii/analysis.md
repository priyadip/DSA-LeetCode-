# 81. Search in Rotated Sorted Array II - Solution Analysis

## Problem Understanding
The input is a rotated sorted array that may contain duplicate values. We must determine whether a target integer exists in the array. The rotation splits the array into two sorted subarrays, but duplicates prevent us from reliably identifying which half is sorted when the values at `left`, `mid`, and `right` are equal. The constraints (n ≤ 5000) allow an O(n) worst case, but the goal is to retain O(log n) performance when possible.

## Approach
The solution uses a **modified binary search**. In the classic rotated-array search (without duplicates), we compare `nums[left]` and `nums[mid]` to decide which half is sorted, then check whether the target lies in that sorted half. With duplicates, the equality `nums[left] == nums[mid] == nums[right]` makes it impossible to know which side is sorted; the key insight is that when all three are equal and not the target, we can safely discard both ends because the target cannot be at `left` or `right` (it would have been caught at `mid`). This shrinks the search space linearly in the worst case (O(n)), but preserves logarithmic behavior when duplicates are sparse.

## Algorithm
1. Set `left = 0`, `right = len(nums) - 1`.
2. While `left <= right`:
   a. Compute `mid = (left + right) // 2`.
   b. If `nums[mid] == target`, return `True`.
   c. If `nums[left] == nums[mid] == nums[right]`, increment `left` and decrement `right`.
   d. Else if `nums[left] <= nums[mid]` (left half is sorted):
        - If `nums[left] <= target < nums[mid]`, set `right = mid - 1`.
        - Otherwise, set `left = mid + 1`.
   e. Else (right half is sorted):
        - If `nums[mid] < target <= nums[right]`, set `left = mid + 1`.
        - Otherwise, set `right = mid - 1`.
3. Return `False`.

## Line-by-Line Explanation
- `left = 0`: Start of the current search interval.
- `right = len(nums) - 1`: End of the current search interval.
- `while left <= right:`: Continue while the interval is non-empty.
- `mid = (left + right) // 2`: Middle index of the current interval.
- `if nums[mid] == target: return True`: Target found at mid.
- `if nums[left] == nums[mid] == nums[right]:`: Ambiguous case — cannot tell which half is sorted.
- `left += 1`: Discard leftmost element; it cannot be the target (mid already checked).
- `right -= 1`: Discard rightmost element for the same reason.
- `elif nums[left] <= nums[mid]:`: Left half `[left..mid]` is sorted (non-decreasing).
- `if nums[left] <= target < nums[mid]:`: Target lies in the sorted left half.
- `right = mid - 1`: Narrow search to left half.
- `else:`: Target not in left half.
- `left = mid + 1`: Narrow search to right half.
- `else:`: Right half `[mid..right]` must be sorted.
- `if nums[mid] < target <= nums[right]:`: Target lies in the sorted right half.
- `left = mid + 1`: Narrow search to right half.
- `else:`: Target not in right half.
- `right = mid - 1`: Narrow search to left half.
- `return False`: Exhausted search space without finding target.

## Dry Run
Trace of Example 2: `nums = [2,5,6,0,0,1,2]`, `target = 3`.

| Step | left | right | mid | nums[mid] | nums[left] | nums[right] | Condition / Action |
|------|------|-------|-----|-----------|------------|-------------|---------------------|
| 1 | 0 | 6 | 3 | 0 | 2 | 2 | `nums[mid] != target`; `nums[left]==nums[mid]==nums[right]` false; `nums[left] <= nums[mid]` (2<=0) false → right half sorted; `nums[mid] < target <= nums[right]` (0<3<=2) false → `right = mid-1 = 2` |
| 2 | 0 | 2 | 1 | 5 | 2 | 6 | `nums[mid] != target`; all-equal false; `nums[left] <= nums[mid]` (2<=5) true → left half sorted; `nums[left] <= target < nums[mid]` (2<=3<5) true → `right = mid-1 = 0` |
| 3 | 0 | 0 | 0 | 2 | 2 | 2 | `nums[mid] != target`; `nums[left]==nums[mid]==nums[right]` true → `left=1`, `right=-1` |
| 4 | 1 | -1 | – | – | – | – | Loop exits (`left <= right` false) → return `False` |

## Complexity
- **Time:** O(n) worst-case, O(log n) average.  
  *Justification:* In the worst case (e.g., all elements equal except one), the `nums[left] == nums[mid] == nums[right]` branch triggers repeatedly, shrinking the search space by only one element per iteration, leading to linear time. When duplicates are sparse, binary search halves the range each step, giving logarithmic time.  
- **Space:** O(1).  
  *Justification:* Only a constant number of integer variables (`left`, `right`, `mid`) are used, independent of input size `n = len(nums)`.

## Edge Cases
- **Single element:** `left == right`; the loop runs once, correctly returns `True` if that element equals `target`, else `False`.
- **All elements equal:** The triple-equality branch fires every iteration, moving `left` rightward and `right` leftward until they cross. Returns `True` if `target` equals that value, else `False`.
- **Target not present:** The loop terminates with `left > right` and returns `False`.
- **Array not rotated (pivot 0):** The condition `nums[left] <= nums[mid]` correctly identifies the left half as sorted, and binary search proceeds normally.
- **Negative numbers / zero:** Handled naturally by comparisons; no special cases needed.
- **Maximum input size (5000):** Well within Python's recursion/iteration limits; no stack overflow risk.

## Possible Improvements
The solution is already optimal for the given constraints. The worst-case O(n) time is unavoidable when duplicates prevent deciding which half is sorted (as noted in the problem's follow-up). The variable names (`left`, `right`, `mid`) are clear and conventional. The triple-equality check `nums[left] == nums[mid] == nums[right]` is the standard way to handle duplicates without missing the target. No redundant passes or data structures are present.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
