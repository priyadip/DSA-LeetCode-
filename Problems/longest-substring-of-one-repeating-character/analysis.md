# 2213. Longest Substring of One Repeating Character - Solution Analysis

## Problem Understanding
We are given a string `s` and `k` queries. Each query changes a single character in `s` at a given index. After each update we must report the length of the longest contiguous substring consisting of exactly one repeating character. The string length `n` and number of queries `k` are both up to 100,000, so an O(n) per query solution is too slow. The problem requires a data structure that supports point updates and can quickly retrieve the global maximum repeating substring length.

## Approach
The solution uses a **segment tree** where each node stores five pieces of information about its segment:
- `lc` / `rc`: the leftmost and rightmost character (as integers 0–25).
- `pre`: length of the longest prefix consisting of a single character.
- `suf`: length of the longest suffix consisting of a single character.
- `best`: length of the longest substring of a single character anywhere in the segment.

This pattern suits the problem because a point update only affects O(log n) nodes, and the answer after each update is simply `best[1]` (the root). The brute‑force approach would scan the whole string after every update, costing O(n k) time. The segment tree reduces each update to O(log n) by merging children’s information. The key insight is that the longest repeating substring in a parent segment is either entirely in the left child, entirely in the right child, or it crosses the boundary – in which case it is the suffix of the left child plus the prefix of the right child, provided the boundary characters match.

## Algorithm
1. **Convert** the input string `s` into an integer array `a` (0–25).
2. **Build** the segment tree recursively:
   - For a leaf (single character), set `lc = rc = character`, `pre = suf = best = 1`.
   - For an internal node, merge its two children:
     - `lc = lc[left]`, `rc = rc[right]`.
     - `pre = pre[left]`; if the whole left segment is uniform (`pre[left] == left_len`) and `rc[left] == lc[right]`, add `pre[right]`.
     - `suf = suf[right]`; if the whole right segment is uniform (`suf[right] == right_len`) and `rc[left] == lc[right]`, add `suf[left]`.
     - `best = max(best[left], best[right])`; if `rc[left] == lc[right]`, also consider `suf[left] + pre[right]`.
3. **Process queries** in order:
   - For each query, convert the new character to an integer.
   - **Update** the segment tree at the given index (standard point update, then re‑merge on the path back to the root).
   - Append `best[1]` (the root’s `best`) to the answer list.
4. **Return** the answer list.

## Line-by-Line Explanation
- `n = len(s)`: length of the string.
- `size = 4 * n`: standard segment tree array size (safe upper bound).
- `lc = [0] * size` … `best = [0] * size`: five parallel arrays storing node data.
- `a = [ord(c) - 97 for c in s]`: map characters to 0–25 for faster comparison.
- `build(node, l, r)`: recursive builder.
  - `if l == r:` leaf initialization.
  - `mid = (l + r) >> 1`: midpoint.
  - `left = node << 1; right = left | 1`: child indices.
  - Recursive calls on children.
  - Merge logic for `lc`, `rc`, `pre`, `suf`, `best` as described in the algorithm.
- `update(node, l, r, idx, ch)`: point update.
  - `if l == r:` update leaf with new character.
  - Recurse to the child containing `idx`.
  - After recursion, re‑merge exactly as in `build`.
- `build(1, 0, n - 1)`: construct the initial tree.
- `k = len(queryIndices); ans = [0] * k`: prepare output.
- Loop over queries:
  - `idx = queryIndices[i]; ch = ord(queryCharacters[i]) - 97`: get update parameters.
  - `update(1, 0, n - 1, idx, ch)`: apply update.
  - `ans[i] = best[1]`: root’s `best` is the answer for this query.
- `return ans`.

## Dry Run
Trace Example 1: `s = "babacc"`, `queryCharacters = "bcb"`, `queryIndices = [1,3,3]`.

| Step | i | idx | ch (char) | s after update | best[1] | Action |
|------|---|-----|-----------|----------------|---------|--------|
| 0 (initial) | – | – | – | "babacc" | 2 | build tree; longest is "aa" or "cc" (length 2) |
| 1 | 0 | 1 | 'b' | "bbbacc" | 3 | update index 1 to 'b'; root best becomes 3 ("bbb") |
| 2 | 1 | 3 | 'c' | "bbbccc" | 3 | update index 3 to 'c'; root best stays 3 ("bbb" or "ccc") |
| 3 | 2 | 3 | 'b' | "bbbbcc" | 4 | update index 3 to 'b'; root best becomes 4 ("bbbb") |

The final answer `[3,3,4]` matches the example.

## Complexity
- **Time**: O(n) for building the tree + O(k log n) for k updates. Each update visits O(log n) nodes and does O(1) work per node.
- **Space**: O(n) for the five segment‑tree arrays (each of size 4n). The recursion depth is O(log n), so call stack space is also O(log n).

## Edge Cases
- **Single character string (n = 1)**: The tree has only a leaf; every update sets `best[1] = 1`. Works correctly.
- **All characters identical initially**: `best[1] = n`. Updates that change a character may split the run; the merge logic correctly recomputes prefix/suffix/best.
- **Multiple updates to the same index**: Each update is independent; the tree reflects the latest character.
- **Maximum constraints (n = k = 100,000)**: The 4n arrays fit in memory (≈ 2 million integers total), and O(k log n) ≈ 1.7 million operations runs well within limits.
- **Empty string**: Not possible per constraints (`1 <= s.length`).

## Possible Improvements
The solution is already asymptotically optimal for the given constraints (O((n + k) log n) time, O(n) space). A minor practical improvement would be to implement the segment tree iteratively to avoid recursion overhead, but the recursive version is clear and fast enough in Python. The variable names (`lc`, `rc`, `pre`, `suf`, `best`) are descriptive and follow the standard terminology for this pattern. No redundant passes or structures exist.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
