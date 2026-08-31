# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points - Solution Analysis

## Problem Understanding
We are given a singly linked list and must identify *critical points* — nodes that are strictly greater than both neighbours (local maxima) or strictly smaller than both neighbours (local minima). The first and last nodes can never be critical points because they lack a previous or next node. We need the minimum distance between any two *adjacent* critical points and the maximum distance between the *first* and *last* critical points. If fewer than two critical points exist, return `[-1, -1]`. The list length is up to 10⁵, so an O(n) single-pass solution with O(1) extra space is required.

## Approach
The solution uses a **single-pass linked list traversal with three pointers** (`prev`, `curr`, `curr.next`). This pattern suits the problem because critical points are defined purely by a node's immediate neighbours, so we only need a sliding window of three nodes at any time.  

Brute force would collect all critical point indices in an array (O(n) space) then compute min/max distances in a second pass. The chosen approach improves space to O(1) by maintaining only the first critical index, the last critical index, and the running minimum distance between consecutive critical points.  

**Key insight:** The maximum distance is always between the first and last critical points; the minimum distance is the smallest gap between *adjacent* critical points. Both can be tracked online without storing all indices.

## Algorithm
1. Initialise `prev = head`, `curr = head.next`, `pos = 1` (1-indexed position of `curr`).
2. Initialise `first = -1`, `last = -1`, `min_dist = ∞`.
3. While `curr.next` exists (so `curr` has both neighbours):
   a. If `curr.val` is strictly greater than both `prev.val` and `curr.next.val` **or** strictly smaller than both, then `curr` is a critical point.
   b. If `first == -1`, set `first = pos` (first critical point found).
   c. Else, update `min_dist = min(min_dist, pos - last)` (distance from previous critical point).
   d. Set `last = pos` (update last seen critical point).
   e. Advance window: `prev = curr`, `curr = curr.next`, `pos += 1`.
4. After loop, if `first == last` (fewer than two critical points), return `[-1, -1]`.
5. Otherwise, `max_dist = last - first`; return `[min_dist, max_dist]`.

## Line-by-Line Explanation
- `prev = head; curr = head.next; pos = 1`: Set up the three-node window; `pos` tracks the index of `curr` (1-indexed because `head` is index 0).
- `first = -1; last = -1; min_dist = float('inf')`: Sentinels for first/last critical positions and running minimum gap.
- `while curr.next:`: Loop while `curr` has a next node, guaranteeing both neighbours exist for the critical-point test.
- `if ((curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val)):`: Checks the strict local maxima/minima condition.
- `if first == -1: first = pos`: Records the position of the very first critical point.
- `else: min_dist = min(min_dist, pos - last)`: Updates the minimum distance using the gap from the previous critical point (`last`).
- `last = pos`: Moves the `last` pointer to the current critical point.
- `prev = curr; curr = curr.next; pos += 1`: Slides the window forward by one node.
- `if first == last: return [-1, -1]`: Only one critical point found (or none), so no pair exists.
- `max_dist = last - first`: Maximum distance is simply the span from first to last critical point.
- `return [min_dist, max_dist]`: Returns the required pair.

## Dry Run
Example 2: `head = [5,3,1,2,5,1,2]` (indices 0–6)

| Step | pos | prev.val | curr.val | curr.next.val | Critical? | first | last | min_dist | Action |
|------|-----|----------|----------|---------------|-----------|-------|------|----------|--------|
| 1    | 1   | 5        | 3        | 1             | No        | -1    | -1   | ∞        | advance |
| 2    | 2   | 3        | 1        | 2             | Yes (min) | 2     | 2    | ∞        | first=2, last=2 |
| 3    | 3   | 1        | 2        | 5             | No        | 2     | 2    | ∞        | advance |
| 4    | 4   | 2        | 5        | 1             | Yes (max) | 2     | 4    | 2        | min_dist=4-2=2, last=4 |
| 5    | 5   | 5        | 1        | 2             | Yes (min) | 2     | 5    | 1        | min_dist=min(2,5-4)=1, last=5 |
| 6    | 6   | 1        | 2        | None          | loop ends | 2     | 5    | 1        | exit |

`first=2`, `last=5` → `max_dist = 3`. Return `[1, 3]`. Matches expected output.

## Complexity
- **Time:** O(n) — each node is visited exactly once; the loop runs n-2 times (n = list length).
- **Space:** O(1) — only a constant number of integer variables and pointers are used, independent of n.

## Edge Cases
- **Fewer than two critical points** (e.g., `[3,1]`, `[1,2,3]`, `[2,2,2]`): `first == last` triggers `[-1, -1]`. Correct.
- **Exactly two critical points**: `min_dist` and `max_dist` both equal `last - first`. Example 3 demonstrates this.
- **Multiple critical points with equal values adjacent** (e.g., `[1,3,2,2,3,2]`): Strict inequality prevents plateaus from being critical points; handled correctly.
- **Maximum list size (10⁵)**: Single pass with O(1) memory fits constraints.
- **Negative values**: Constraints specify `1 <= Node.val <= 10⁵`, so negatives are not possible; code would still work if they were.

## Possible Improvements
The solution is already optimal in both time (O(n)) and space (O(1)) for the given constraints. No algorithmic improvement is possible.  

A minor readability improvement: rename `pos` to `index` or `curr_idx` to clarify it is 1-indexed. The logic `if first == last` is correct but slightly subtle; an explicit `count` variable (incremented on each critical point) would make the "fewer than two" check more self-documenting (`if count < 2`). Neither change affects complexity.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
