# 994. Rotting Oranges - Solution Analysis

## Problem Understanding
We are given an m×n grid where each cell is 0 (empty), 1 (fresh orange), or 2 (rotten orange). Every minute, any fresh orange that shares an edge (up/down/left/right) with a rotten orange becomes rotten. We must return the minimum minutes until no fresh oranges remain, or -1 if some fresh orange can never be reached. The grid dimensions are at most 10×10, so an O(mn) algorithm is easily fast enough. The key constraints are the 4-directional spread and the simultaneous rotting from all rotten oranges each minute.

## Approach
The solution uses **multi-source Breadth-First Search (BFS)**. The brute-force approach would simulate minute-by-minute by scanning the whole grid each time, costing O(mn × minutes). BFS improves this by starting from all initially rotten oranges at once (multiple sources in the queue) and expanding level by level; each BFS level corresponds to one minute. The key insight is that the first time a fresh orange is reached by BFS is exactly the minute it rots, because BFS explores in increasing distance from the sources. We maintain a count of fresh oranges and decrement it when we rot one; when the queue empties or fresh hits zero we stop.

## Algorithm
1. Scan the grid once to count fresh oranges and enqueue coordinates of every rotten orange.
2. Initialize `minutes = 0` and the four direction vectors.
3. While the queue is not empty **and** fresh oranges remain:
   a. Process the current level: repeat `len(queue)` times, popping a rotten orange.
   b. For each of its four neighbours, if the neighbour is in bounds and fresh (value 1), mark it rotten (value 2), decrement `fresh`, and enqueue the neighbour.
   c. After the level finishes, increment `minutes`.
4. Return `minutes` if `fresh == 0`, otherwise `-1`.

## Line-by-Line Explanation
- `rows, cols = len(grid), len(grid[0])`: store grid dimensions for bounds checks.
- `queue = deque()`: queue for BFS, holds (row, col) of rotten oranges.
- `fresh = 0`: counter of fresh oranges not yet rotted.
- The nested `for` loops: iterate every cell; if value is 2, append to queue; if 1, increment `fresh`.
- `minutes = 0`: minutes elapsed so far.
- `directions = [(1,0), (-1,0), (0,1), (0,-1)]`: four 4-directional moves.
- `while queue and fresh:`: continue while there are rotten oranges to spread from and fresh oranges left to rot.
- `for _ in range(len(queue)):`: process exactly the oranges that were rotten at the start of this minute (current BFS level).
- `r, c = queue.popleft()`: take one rotten orange.
- The inner `for dr, dc in directions:`: try each neighbour.
- `nr, nc = r + dr, c + dc`: neighbour coordinates.
- `if 0 <= nr < rows and 0 <= nc < cols:`: bounds check.
- `if grid[nr][nc] == 1:`: neighbour is fresh.
- `grid[nr][nc] = 2`: rot it in-place so it won't be processed again.
- `fresh -= 1`: one less fresh orange.
- `queue.append((nr, nc))`: this newly rotten orange will spread in the next minute.
- `minutes += 1`: one full minute (level) completed.
- `return minutes if fresh == 0 else -1`: all fresh rotted → answer; otherwise some unreachable fresh remain.

## Dry Run
Example 1: `grid = [[2,1,1],[1,1,0],[0,1,1]]`

Initial scan: queue = [(0,0)], fresh = 6, minutes = 0.

| Step | Level size | Popped (r,c) | Fresh neighbour rotted | fresh after level | minutes after level |
|------|------------|--------------|------------------------|-------------------|---------------------|
| 1    | 1          | (0,0)        | (0,1), (1,0)           | 4                 | 1                   |
| 2    | 2          | (0,1)        | (0,2), (1,1)           | 2                 | 2                   |
|      |            | (1,0)        | (none new)             |                   |                     |
| 3    | 2          | (0,2)        | (none)                 | 1                 | 3                   |
|      |            | (1,1)        | (2,1)                  |                   |                     |
| 4    | 1          | (2,1)        | (2,2)                  | 0                 | 4                   |

Queue empties, fresh = 0 → return 4.

## Complexity
- Time: O(m × n), because each cell is enqueued and dequeued at most once, and each edge (neighbour check) is examined at most once.
- Space: O(m × n) for the queue in the worst case (e.g., all oranges rotten initially).

Here m = rows, n = cols, both ≤ 10 per constraints.

## Edge Cases
- **No fresh oranges initially** (e.g., `[[0,2]]`): `fresh = 0`, the while loop never runs, `minutes` stays 0, returns 0. Correct.
- **Fresh oranges but no rotten oranges**: queue empty initially, while loop skipped, `fresh > 0` → returns -1. Correct.
- **Unreachable fresh orange** (Example 2): BFS cannot reach it, `fresh > 0` at end → returns -1. Correct.
- **Single cell grid**: handled by the same logic; bounds checks work for 1×1.
- **All cells empty (0)**: `fresh = 0`, queue empty → returns 0. Correct.

## Possible Improvements
The solution is already optimal in time and space for the given constraints. A minor clarity improvement: rename `minutes` to `elapsed` or `time` to emphasise it counts completed levels. The in-place mutation of `grid` is acceptable here but could be noted as a side effect if the grid were needed later. No algorithmic improvement is possible; multi-source BFS is the standard optimal approach.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
