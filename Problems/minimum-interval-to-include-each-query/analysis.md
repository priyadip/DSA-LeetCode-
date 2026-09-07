# 1851. Minimum Interval to Include Each Query - Solution Analysis

## Problem Understanding
Given a list of intervals `[left_i, right_i]` and a list of query points, for each query we must find the size (`right_i - left_i + 1`) of the smallest interval that contains the query point. If no interval contains the query, the answer is `-1`. The constraints (up to 10^5 intervals and queries) rule out any O(n·m) brute-force approach; an O((n+m) log n) solution is required. Order of queries in the output must match the original input order.

## Approach
The solution uses an **offline sweep line with a min-heap** (priority queue).  
- **Brute force**: For each query, scan all intervals → O(n·m), too slow.  
- **Chosen approach**: Sort intervals by `left` and queries by value. Sweep through queries in increasing order. Maintain a min-heap of intervals that have started (`left <= query`) keyed by interval size. Before answering a query, remove intervals that have already ended (`right < query`). The heap top then gives the smallest active interval covering the query.  
**Key insight**: Processing queries in sorted order lets us incrementally add intervals as they become relevant and discard them once they no longer cover the current query, so each interval is pushed and popped at most once.

## Algorithm
1. Sort `intervals` by their left endpoint.
2. Create a list `qs` of `(query, original_index)` pairs and sort it by query value.
3. Initialise `ans` array with `-1`, an empty min-heap `heap`, and an interval pointer `i = 0`.
4. For each `(q, idx)` in `qs` (in increasing order of `q`):
   a. While `i < len(intervals)` and `intervals[i][0] <= q`:  
      Push `(size, right)` of `intervals[i]` into `heap`; increment `i`.
   b. While `heap` is not empty and `heap[0][1] < q`:  
      Pop from `heap` (interval ended before `q`).
   c. If `heap` is not empty: `ans[idx] = heap[0][0]` (smallest size covering `q`).
5. Return `ans`.

## Line-by-Line Explanation
- `intervals.sort()`: Sort intervals by left endpoint so we can add them in order as the sweep progresses.
- `qs = sorted((q, i) for i, q in enumerate(queries))`: Pair each query with its original index and sort by query value; this allows offline processing while preserving output order.
- `an = [-1] * len(queries)`: Pre-fill answer array with `-1` (default when no interval covers the query).
- `heap = []`: Min-heap storing tuples `(interval_size, right_endpoint)`. The heap orders by size, so the smallest active interval is at the top.
- `i = 0`: Pointer into the sorted `intervals` list; tracks how many intervals have been added to the heap.
- `for q, idx in qs:`: Iterate queries from smallest to largest.
- `while i < len(intervals) and intervals[i][0] <= q:`: Add all intervals whose left endpoint is ≤ current query. These intervals have started and might cover `q`.
- `l, r = intervals[i]`: Unpack the current interval.
- `heappush(heap, (r - l + 1, r))`: Push interval size and its right endpoint. The right endpoint is needed later to know when the interval expires.
- `i += 1`: Advance interval pointer.
- `while heap and heap[0][1] < q:`: Remove intervals that end before the current query (they cannot cover `q` or any future query because queries only increase).
- `heappop(heap)`: Discard the expired interval with the smallest size (any expired interval is removed; the heap property ensures we check the smallest first, but we must pop all expired ones).
- `if heap:`: If any active interval remains, the one at the top has the minimum size.
- `an[idx] = heap[0][0]`: Record the size for the original query index.
- `return an`: Return answers in the original query order.

## Dry Run
Example 1:  
`intervals = [[1,4],[2,4],[3,6],[4,4]]`, `queries = [2,3,4,5]`

Sorted intervals (by left): `[[1,4], [2,4], [3,6], [4,4]]`  
Sorted queries `qs`: `[(2,0), (3,1), (4,2), (5,3)]`

| Step | q | idx | i | intervals added (l,r,size) | heap after adds (size,right) | heap after removals | an[idx] |
|------|---|-----|---|----------------------------|------------------------------|---------------------|---------|
| 1    | 2 | 0   | 0 | add [1,4] size=4; add [2,4] size=3 | [(3,4), (4,4)] | none (both right≥2) | 3 |
| 2    | 3 | 1   | 2 | add [3,6] size=4 | [(3,4), (4,4), (4,6)] | none (all right≥3) | 3 |
| 3    | 4 | 2   | 3 | add [4,4] size=1 | [(1,4), (3,4), (4,6), (4,4)] | none (all right≥4) | 1 |
| 4    | 5 | 3   | 4 | (no more intervals) | [(1,4), (3,4), (4,6), (4,4)] | pop (1,4) right=4<5; pop (3,4) right=4<5; pop (4,4) right=4<5 → heap = [(4,6)] | 4 |

Final `an = [3,3,1,4]` matches expected output.

## Complexity
- **Time**: O(n log n + m log m) for sorting intervals and queries. Each interval is pushed once and popped at most once from the heap → O(n log n) heap operations. Total O((n+m) log n) (since n,m ≤ 10^5, log factors are similar).
- **Space**: O(n + m) for the sorted intervals, sorted queries, heap (up to n elements), and answer array.

## Edge Cases
- **Queries smaller than all interval lefts**: The first `while` adds nothing, heap stays empty → answer `-1`.
- **Queries larger than all interval rights**: All intervals are added then removed in the second `while` → heap empty → `-1`.
- **Multiple intervals with same size**: Heap orders by size then by right (tuple comparison), but any minimum size is correct.
- **Single interval / single query**: Works trivially.
- **Large coordinate values (up to 10^7)**: No impact; algorithm depends only on ordering, not coordinate magnitude.
- **Already sorted queries**: Sorting still O(m log m) but could be optimised to O(m) if guaranteed; not required by constraints.

## Possible Improvements
The solution is already optimal in asymptotic complexity for the given constraints.  
- **Micro-optimisation**: Using `heapq.heapify` on a pre-built list of intervals added per query is not possible because intervals are added incrementally.  
- **Variable names**: `an` → `ans`, `qs` → `sorted_queries`, `i` → `interval_idx` would improve readability without changing logic.  
- **Alternative**: A segment tree or binary indexed tree over compressed coordinates could achieve O((n+m) log (n+m)) but with higher constant factors; the heap sweep line is simpler and faster in practice.  
No material algorithmic improvement exists; the current approach is the standard optimal solution.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
