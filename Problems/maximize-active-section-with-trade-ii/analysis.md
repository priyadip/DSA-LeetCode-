# 3501. Maximize Active Section with Trade II - Solution Analysis

## Problem Understanding
We are given a binary string `s` and multiple queries `[l, r]`. For each query we consider the substring `s[l..r]` augmented with a `'1'` at both ends. We may perform at most one trade: choose a `'1'` block surrounded by `'0'`s, turn it into `'0'`s, then choose a `'0'` block surrounded by `'1'`s, turn it into `'1'`s. The goal is to maximize the total number of `'1'`s in the whole string after the trade. The trade only affects the substring; the rest of `s` stays unchanged. Constraints: `n, q ≤ 10^5`, so an `O(n + q log n)` or similar solution is required.

## Approach
The solution uses **zero-block segmentation** combined with a **segment tree for range maximum queries**.  
The key insight: a valid trade always picks a `'1'` block that lies between two `'0'` blocks (in the augmented string). Converting that `'1'` block to `'0'` merges the two `'0'` blocks, and then converting the merged `'0'` block to `'1'` yields a net gain equal to the sum of the lengths of the two original `'0'` blocks. Therefore, for a given substring, the optimal gain is the maximum sum of lengths of two adjacent zero blocks that lie (fully or partially) inside the query range, with the boundary zero blocks clipped to the query interval.

Brute force would examine every possible `'1'` block for each query, costing `O(n)` per query. By precomputing all zero blocks and the sums of adjacent pairs, we reduce each query to a few boundary calculations and a range maximum query over the precomputed pair sums.

## Algorithm
1. Count total `'1'`s in `s` → `t1`.
2. Scan `s` to collect all maximal contiguous `'0'` blocks: store `(start, end)` for each block.
3. Let `m` be the number of zero blocks. Create arrays `starts`, `ends`, `lengths`.
4. Build array `pair` of length `m-1` where `pair[i] = lengths[i] + lengths[i+1]` (sum of two adjacent zero blocks).
5. Build a segment tree over `pair` to answer range maximum queries in `O(log m)`.
6. For each query `[l, r]`:
   - `first` = index of first zero block with `end ≥ l` (binary search on `ends`).
   - `last` = index of last zero block with `start ≤ r` (binary search on `starts`).
   - If `first ≥ last`, fewer than two zero blocks intersect the query → no trade possible, answer = `t1`.
   - Otherwise compute `best` as the maximum of:
        * Clipped sum of zero blocks `first` and `first+1`.
        * Clipped sum of zero blocks `last-1` and `last`.
        * Maximum `pair` value for fully internal pairs (indices `first+1` to `last-2`) via segment tree.
   - Answer = `t1 + best`.
7. Return all answers.

## Line-by-Line Explanation
- `t1 = s.count("1")`: total `'1'`s in the original string, used as base for every query.
- `hmz` construction loop: extracts all zero blocks as `(start, end)` tuples.
- `starts`, `ends`, `lengths`: separate arrays for binary search and length access.
- `pair` loop: computes sum of lengths for each adjacent zero-block pair.
- Segment tree build: `size` is the smallest power of two ≥ `len(pair)`; `seg` array of size `2*size`; leaves filled with `pair` values; internal nodes store max of children.
- `range_max(left, right)`: standard iterative segment tree range maximum query (inclusive bounds).
- `cl(index, l, r)`: returns the length of the intersection of zero block `index` with `[l, r]` (clipped length).
- Query processing loop:
   - `first = bisect_left(ends, l)`: first zero block that ends at or after `l`.
   - `last = bisect_right(starts, r) - 1`: last zero block that starts at or before `r`.
   - `if first >= last`: fewer than two intersecting zero blocks → trade impossible.
   - `best` initialized with clipped sum of the first two intersecting zero blocks.
   - `best` updated with clipped sum of the last two intersecting zero blocks.
   - `best` updated with segment tree query over fully internal pairs (`first+1` to `last-2`).
   - `answer.append(t1 + best)`.

## Dry Run
Example: `s = "0100"`, `queries = [[0,3],[0,2],[1,3],[2,3]]`.

- `t1 = 1`.
- Zero blocks: `hmz = [(0,0), (2,3)]` → `starts=[0,2]`, `ends=[0,3]`, `lengths=[1,2]`.
- `pair = [3]` (only one pair, index 0).
- Segment tree: `size=1`, `seg=[0,3]`.

**Query [0,3]**:
- `first = bisect_left([0,3], 0) = 0`.
- `last = bisect_right([0,2], 3) - 1 = 2 - 1 = 1`.
- `first < last` → proceed.
- `cl(0,0,3) = min(0,3)-max(0,0)+1 = 1`.
- `cl(1,0,3) = min(3,3)-max(2,0)+1 = 2`.
- `best = 1+2 = 3`.
- `cl(last-1,0,3)+cl(last,0,3)` same → `best=3`.
- `range_max(1, -1) = 0`.
- Answer = `1+3=4`.

**Query [0,2]**:
- `first = bisect_left([0,3], 0) = 0`.
- `last = bisect_right([0,2], 2) - 1 = 2 - 1 = 1`.
- `cl(0,0,2)=1`, `cl(1,0,2)=min(3,2)-max(2,0)+1=1` → `best=2`.
- `range_max(1,-1)=0`.
- Answer = `1+2=3`.

**Query [1,3]**:
- `first = bisect_left([0,3], 1) = 1` (block (2,3) ends at 3 ≥ 1).
- `last = bisect_right([0,2], 3) - 1 = 2 - 1 = 1`.
- `first >= last` → answer = `t1 = 1`.

**Query [2,3]**:
- `first = bisect_left([0,3], 2) = 1`.
- `last = bisect_right([0,2], 3) - 1 = 1`.
- `first >= last` → answer = `1`.

Output `[4,3,1,1]` matches example.

## Complexity
- **Time**: `O(n + q log m)` where `n = len(s)`, `m = number of zero blocks (≤ n)`, `q = number of queries`.
  - Scanning `s` and building arrays: `O(n)`.
  - Segment tree build: `O(m)`.
  - Each query: two binary searches `O(log m)` + segment tree query `O(log m)`.
- **Space**: `O(n)` for zero-block arrays and segment tree (`O(m)`).

## Edge Cases
- **No zero blocks** (`m = 0`): `pair` empty, segment tree size 1 with zeros. For any query `first = 0`, `last = -1` → `first >= last` → answer `t1`. Correct because no `'1'` block can be surrounded by `'0'`s.
- **Single zero block** (`m = 1`): `pair` empty, same logic → no trade possible.
- **Query covers only part of a zero block**: `cl` correctly clips the length.
- **Query boundaries exactly at zero-block edges**: binary searches handle inclusive/exclusive correctly (`bisect_left` on `ends`, `bisect_right` on `starts`).
- **All `'1'`s string**: `t1 = n`, `m = 0` → all answers `n`.
- **All `'0'`s string**: `t1 = 0`, `m = 1` → all answers `0`.

## Possible Improvements
The solution is already optimal in asymptotic complexity for the given constraints. The segment tree could be replaced by a sparse table for `O(1)` queries (since `pair` is static), but `O(log m)` is fast enough and the code is simpler. Variable names are clear (`hmz`, `cl`, `pair`). No redundant passes or structures.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
