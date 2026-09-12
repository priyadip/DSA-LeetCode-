# 3414. Maximum Score of Non-overlapping Intervals - Solution Analysis

## Problem Understanding
We are given `n` intervals, each with a left endpoint `l_i`, right endpoint `r_i`, and a weight `weight_i`. We may select **at most 4** intervals that are pairwise non-overlapping (sharing a boundary counts as overlapping, so we need `r_a < l_b` or `r_b < l_a`). The goal is to maximize the sum of weights of the chosen intervals. If multiple sets achieve the same maximum weight, we must return the lexicographically smallest array of original indices (0‑based). Constraints: `n ≤ 5·10⁴`, coordinates up to `10⁹`, weights up to `10⁹`.

## Approach
The solution uses **Dynamic Programming with Binary Search** (a classic Weighted Interval Scheduling pattern extended to a fixed small number of selections).  
- **Brute force** would try all combinations of up to 4 intervals → `O(n⁴)`, infeasible.  
- **Key insight**: After sorting intervals by right endpoint, any optimal set of non‑overlapping intervals appears in increasing order of right endpoints. For each interval we can quickly find the last interval that ends before it starts using binary search.  
- **DP state**: `dp[k][i]` = (maximum total weight, lexicographically smallest tuple of original indices) achievable by choosing exactly `k` intervals from the first `i` intervals in the sorted order.  
- **Transition**: For the `i`‑th sorted interval (1‑indexed), either skip it (`dp[k][i-1]`) or take it (`weight_i + dp[k-1][p]` where `p` is the number of intervals with right endpoint `< l_i`). Tie‑break by lexicographic order of the index tuples.  
- Because `k ≤ 4`, the DP table has only 5 rows, making the `O(n log n)` time and `O(n)` space easily fast enough.

## Algorithm
1. Attach each interval’s original index: `arr = [(l, r, w, idx) for idx, (l, r, w) in enumerate(intervals)]`.
2. Sort `arr` by right endpoint `r`.
3. Build `ends = [r for (_, r, _, _) in arr]` for binary search.
4. For each interval `i` (0‑based in `arr`), compute `prev[i] = bisect_left(ends, arr[i][0])` – the count of intervals ending strictly before `arr[i]` starts.
5. Initialise `dp[0..4][0..n]` with `(0, ())`.
6. For `k = 1 .. 4`:
   For `i = 1 .. n`:
   - `not_take = dp[k][i-1]`
   - `l, r, w, idx = arr[i-1]`
   - `p = prev[i-1]`
   - `old_score, old_indices = dp[k-1][p]`
   - `new_indices = tuple(sorted(old_indices + (idx,)))`
   - `take = (old_score + w, new_indices)`
   - `dp[k][i] = take` if `take[0] > not_take[0]` else `min(take, not_take)` if equal else `not_take`.
7. Return `list(dp[4][n][1])`.

## Line-by-Line Explanation
```python
n = len(intervals)
```
Number of intervals.

```python
arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
```
Attach original indices for final output.

```python
arr.sort(key=lambda x: x[1])
```
Sort by right endpoint – essential for the non‑overlap condition and binary search.

```python
ends = [x[1] for x in arr]
```
Array of right endpoints in sorted order.

```python
prev = [0] * n
for i in range(n):
    prev[i] = bisect_left(ends, arr[i][0])
```
`prev[i]` = number of intervals with right endpoint `< arr[i][0]`. Because `ends` is sorted, `bisect_left` gives the first position where `arr[i][0]` could be inserted, which equals the count of intervals ending before `arr[i]` starts.

```python
dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]
```
`dp[k][i]` stores a pair `(max_score, indices_tuple)` for choosing `k` intervals from the first `i` sorted intervals. `k` ranges 0..4, `i` ranges 0..n.

```python
for k in range(1, 5):
    for i in range(1, n + 1):
```
Iterate over number of chosen intervals (1 to 4) and over prefixes of sorted intervals.

```python
not_take = dp[k][i - 1]
```
Option 1: skip the `i`‑th sorted interval.

```python
l, r, w, idx = arr[i - 1]
```
Current interval’s data (1‑indexed `i` corresponds to `arr[i-1]`).

```python
p = prev[i - 1]
```
Number of intervals that end before this one starts.

```python
old_score, old_indices = dp[k - 1][p]
```
Best result using `k-1` intervals from those `p` compatible intervals.

```python
new_indices = tuple(sorted(old_indices + (idx,)))
```
Add current original index and keep the tuple sorted for lexicographic comparison.

```python
take = (old_score + w, new_indices)
```
Option 2: take current interval.

```python
if take[0] > not_take[0]:
    dp[k][i] = take
elif take[0] == not_take[0]:
    dp[k][i] = min(take, not_take)
else:
    dp[k][i] = not_take
```
Choose higher score; on tie pick lexicographically smaller index tuple (Python’s tuple comparison does exactly that).

```python
return list(dp[4][n][1])
```
The answer for up to 4 intervals is stored in `dp[4][n]`; we only need the indices tuple.

## Dry Run
Example 1: `intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]`  
Original indices: 0:[1,3,2], 1:[4,5,2], 2:[1,5,5], 3:[6,9,3], 4:[6,7,1], 5:[8,9,1]

After sorting by right endpoint:
| sorted i | l | r | w | orig idx |
|----------|---|---|---|----------|
| 0        | 1 | 3 | 2 | 0        |
| 1        | 4 | 5 | 2 | 1        |
| 2        | 1 | 5 | 5 | 2        |
| 3        | 6 | 7 | 1 | 4        |
| 4        | 8 | 9 | 1 | 5        |
| 5        | 6 | 9 | 3 | 3        |

`ends = [3,5,5,7,9,9]`

Compute `prev` (bisect_left on `ends` with `l`):
- i=0, l=1 → `bisect_left([3,5,5,7,9,9], 1) = 0`
- i=1, l=4 → `bisect_left(..., 4) = 1` (only interval 0 ends at 3 < 4)
- i=2, l=1 → 0
- i=3, l=6 → `bisect_left(..., 6) = 3` (intervals 0,1,2 end at 3,5,5 < 6)
- i=4, l=8 → `bisect_left(..., 8) = 4` (intervals 0..3 end at 3,5,5,7 < 8)
- i=5, l=6 → 3

DP for `k=1` (only showing best score and indices):
| i | interval (orig idx) | not_take | take (score, indices) | dp[1][i] |
|---|---------------------|----------|-----------------------|----------|
| 1 | idx 0, w=2          | (0,())   | (2,(0))               | (2,(0))  |
| 2 | idx 1, w=2          | (2,(0))  | (2,(1))               | (2,(0))  (tie, (0) < (1)) |
| 3 | idx 2, w=5          | (2,(0))  | (5,(2))               | (5,(2))  |
| 4 | idx 4, w=1          | (5,(2))  | (1+dp[0][3]=(1,(4)))  | (5,(2))  |
| 5 | idx 5, w=1          | (5,(2))  | (1+dp[0][4]=(1,(5)))  | (5,(2))  |
| 6 | idx 3, w=3          | (5,(2))  | (3+dp[0][3]=(3,(3)))  | (5,(2))  |

`k=2` (only relevant steps):
- i=4 (idx 4, w=1, p=3): `dp[1][3] = (5,(2))` → take = (6, (2,4))
- i=5 (idx 5, w=1, p=4): `dp[1][4] = (5,(2))` → take = (6, (2,5))
- i=6 (idx 3, w=3, p=3): `dp[1][3] = (5,(2))` → take = (8, (2,3)) → this becomes best for k=2.

`k=3` and `k=4` will not improve beyond 8 because no three non‑overlapping intervals sum to more.  
Final `dp[4][6][1] = (2,3)` → output `[2,3]`. Matches example.

## Complexity
- **Time**: `O(n log n)`  
  - Sorting: `O(n log n)`  
  - `n` binary searches: `O(n log n)`  
  - DP loops: `4 * n = O(n)`  
- **Space**: `O(n)`  
  - `arr`, `ends`, `prev`: `O(n)`  
  - `dp` table: `5 * (n+1)` entries, each a small tuple → `O(n)`

## Edge Cases
- **Fewer than 4 intervals**: DP still works; `dp[4][n]` will simply hold the best achievable with ≤4 intervals (since we can always “not take”).
- **All intervals overlap**: Only one interval can be chosen; DP picks the maximum weight (lexicographically smallest index on tie).
- **Ties in weight**: Lexicographic comparison of the sorted index tuples ensures the required output.
- **Intervals with identical right endpoints**: They are adjacent after sorting; `bisect_left` correctly counts only those with right `< current left`. Because they overlap (share right boundary), at most one can be taken. The DP processes them in stable order (original order for equal right), and the tie‑break on indices guarantees the lexicographically smallest set.
- **Large weights/coordinates**: Python integers handle up to `10⁹` sums (max 4·10⁹) without overflow.

## Possible Improvements
- **Memory**: The DP stores a tuple for every state (5·(n+1) tuples). For `n=5·10⁴` this is ~250k tuples, which is acceptable (~few MB). If memory were tighter, we could use a rolling array of two rows (since `dp[k]` only needs `dp[k]` and `dp[k-1]`) and store back‑pointers instead of full tuples, but the current approach is clear and fast enough.
- **Tuple construction**: `tuple(sorted(old_indices + (idx,)))` creates a new sorted tuple each time. Because `old_indices` is already sorted and `idx` is a single integer, we could insert `idx` in O(k) time (k≤4) to avoid the sort call, but the overhead is negligible for k≤4.
- **Missing import**: The code uses `bisect_left` without showing the import (`from bisect import bisect_left`). In a complete submission this must be present.
- **Optimality**: The algorithm achieves the optimal `O(n log n)` time for this problem; no asymptotic improvement is possible under the given constraints.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
