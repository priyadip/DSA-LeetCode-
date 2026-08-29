# 2948. Make Lexicographically Smallest Array by Swapping Elements - Solution Analysis

## Problem Understanding
We are given an array `nums` of positive integers and a positive integer `limit`. We may swap any two elements `nums[i]` and `nums[j]` if `|nums[i] - nums[j]| <= limit`, and we can perform any number of such swaps. The goal is to return the lexicographically smallest array obtainable. Swaps are transitive: if `a` can swap with `b` and `b` with `c`, then `a` can effectively reach `c`'s position. Thus the elements partition into connected components where any permutation within a component is achievable. To minimize lexicographical order, the smallest values in each component should occupy the smallest indices of that component. Constraints: `n ≤ 10^5`, values and `limit ≤ 10^9`, so an `O(n log n)` solution is required.

## Approach
The solution uses **Sorting + Connected Components via Linear Scan** (a common alternative to Union-Find for this problem).  
Brute force would consider all pairs (`O(n^2)`) or build a graph and run DSU (`O(n^2)` edges worst-case). The key insight is that after sorting the values, two values belong to the same component **iff** there is a chain of consecutive sorted values where each adjacent difference is `≤ limit`. Therefore each component corresponds to a contiguous segment in the sorted array. Once components are identified, we greedily assign the smallest values in the component to the smallest original indices in that component.

## Algorithm
1. Create a list `pairs` of `(value, original_index)` and sort it by value.
2. Initialize `start = 0`.
3. While `start < n`:
   - Set `end = start`.
   - Extend `end` while `end + 1 < n` and `pairs[end+1].value - pairs[end].value <= limit`. This finds the maximal contiguous segment where consecutive differences are within `limit`; all these elements form one connected component.
   - Extract the original indices from `pairs[start..end]` and sort them.
   - The values in `pairs[start..end]` are already sorted. For each `k` from `0` to `end-start`, assign `pairs[start+k].value` to `nums[indices[k]]`.
   - Set `start = end + 1` to process the next component.
4. Return the modified `nums`.

## Line-by-Line Explanation
- `pairs = sorted((v, i) for i, v in enumerate(nums))`: creates value-index pairs sorted by value; this orders potential component members by value.
- `n = len(nums)`: length of the array.
- `start = 0`: beginning of the current component in the sorted list.
- `while start < n:`: loop over all components.
- `end = start`: `end` will mark the last index of the current component.
- `while end + 1 < n and pairs[end + 1][0] - pairs[end][0] <= limit:`: extends the component while the next value is within `limit` of the current last value. Because the list is sorted, this condition exactly captures the transitive connectivity.
- `end += 1`: includes the next element in the component.
- `indices = sorted(i for _, i in pairs[start:end + 1])`: collects the original indices of this component and sorts them so the smallest index gets the smallest value.
- `for k, idx in enumerate(indices): nums[idx] = pairs[start + k][0]`: assigns the `k`-th smallest value of the component to the `k`-th smallest index.
- `start = end + 1`: moves to the next component.
- `return nums`: the array is now lexicographically smallest.

## Dry Run
Example 1: `nums = [1,5,3,9,8]`, `limit = 2`.

Sorted `pairs`: `[(1,0), (3,2), (5,1), (8,4), (9,3)]`.

| Step | start | end | Component values | Component indices (sorted) | Assignment |
|------|-------|-----|------------------|----------------------------|------------|
| 1    | 0     | 2   | 1, 3, 5          | [0, 1, 2]                  | nums[0]=1, nums[1]=3, nums[2]=5 |
| 2    | 3     | 4   | 8, 9             | [3, 4]                     | nums[3]=8, nums[4]=9 |

Result: `[1,3,5,8,9]`.

## Complexity
- **Time**: `O(n log n)`. Sorting `pairs` dominates. The while loops scan each element once, and sorting indices per component sums to `O(n log n)` in the worst case (if one component contains all elements, sorting its indices is `O(n log n)`; otherwise the sum of `m_i log m_i` over components is bounded by `n log n`).
- **Space**: `O(n)` for the `pairs` list and the temporary `indices` list.

## Edge Cases
- **Single element**: `start=0`, `end=0`, indices sorted (single), value assigned to same index → unchanged.
- **All elements equal**: differences are `0 ≤ limit`, one component; indices sorted, values identical → unchanged.
- **No valid swaps** (e.g., Example 3): each element forms its own component; each component has one index and one value → array unchanged.
- **Large limit** (all elements in one component): effectively sorts the whole array, which is the lexicographically smallest permutation.
- **Duplicates**: difference `0 ≤ limit`, they group together; sorting indices ensures stable assignment of equal values to smallest indices.

## Possible Improvements
The solution is already optimal for the given constraints. Time complexity `O(n log n)` is the best possible because any algorithm must at least sort the values (or indices) to determine the lexicographically smallest arrangement. Space `O(n)` is also optimal. The code is clean, uses clear variable names, and modifies the input array in place (acceptable per LeetCode conventions). No material improvements are needed.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
