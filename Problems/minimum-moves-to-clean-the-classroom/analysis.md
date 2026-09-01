# 3568. Minimum Moves to Clean the Classroom - Solution Analysis

## Problem Understanding
The problem asks for the minimum number of moves to collect all litter ('L') in an m x n grid starting from 'S' with a given maximum energy. Each move to an adjacent cell costs 1 energy; energy can be reset to maximum by stepping on 'R' cells. Obstacles 'X' are impassable. The grid size is up to 20x20, energy up to 50, and at most 10 litter pieces, making a state-space search with bitmask feasible.

## Approach
The solution uses Breadth-First Search (BFS) over a state space defined by (row, column, collected-litter bitmask, remaining energy). BFS is suitable because each move has uniform cost (1) and we need the shortest path that collects all litter. The key insight is that for a given position and set of collected litter, a state with higher remaining energy dominates one with lower energy, so we only need to keep the maximum energy seen for each (position, mask) pair. This pruning drastically reduces the number of states compared to a naive BFS that also tracks energy as a separate dimension.

## Algorithm
1. Parse the grid to locate the start 'S' and assign each litter 'L' a unique bit index.
2. If there is no litter, return 0 immediately.
3. Initialize a queue with the start state: (start_row, start_col, mask=0, energy=initial_energy, moves=0).
4. Maintain a dictionary `best` mapping (row, col, mask) to the highest remaining energy seen for that state.
5. While the queue is not empty:
   a. Pop the front state (r, c, mask, e, moves).
   b. For each of the four directions:
      i. Compute neighbor (nr, nc); skip if out of bounds or an obstacle 'X'.
      ii. Skip if current energy e is 0 (cannot move).
      iii. Compute new energy ne = e - 1.
      iv. Update mask if neighbor is 'L' by setting the corresponding bit.
      v. If neighbor is 'R', reset ne to the maximum energy.
      vi. If the new mask equals the full mask (all litter collected), return moves + 1.
      vii. If this (nr, nc, new_mask) has not been seen or ne > best[(nr, nc, new_mask)], update best and enqueue (nr, nc, new_mask, ne, moves+1).
6. If the queue empties without collecting all litter, return -1.

## Line-by-Line Explanation
- `m = len(classroom); n = len(classroom[0])`: Grid dimensions.
- `start = None; litter = {}`: Variables to store start coordinates and a mapping from litter positions to bit indices.
- `for i in range(m): for j in range(n): ...`: Scan grid to find 'S' and assign each 'L' an index (0, 1, ...).
- `total_litter = len(litter)`: Number of litter pieces.
- `if total_litter == 0: return 0`: Edge case: no litter to collect.
- `full_mask = (1 << total_litter) - 1`: Bitmask with all litter bits set.
- `q = deque(); q.append((start[0], start[1], 0, energy, 0))`: Initialize BFS queue with start state (position, empty mask, full energy, 0 moves).
- `best = {}; best[(start[0], start[1], 0)] = energy`: Dictionary to record the best (maximum) energy for each (row, col, mask); seed with start state.
- `directions = [(1,0), (-1,0), (0,1), (0,-1)]`: Four possible moves.
- `while q:`: Main BFS loop.
- `r, c, mask, e, moves = q.popleft()`: Dequeue the next state.
- `for dr, dc in directions:`: Try each direction.
- `nr = r + dr; nc = c + dc`: Neighbor coordinates.
- `if not (0 <= nr < m and 0 <= nc < n): continue`: Skip if neighbor is outside grid.
- `if classroom[nr][nc] == 'X': continue`: Skip obstacles.
- `if e == 0: continue`: Cannot move if energy is already 0.
- `ne = e - 1`: Moving costs 1 energy.
- `new_mask = mask`: Start with current collected litter mask.
- `if classroom[nr][nc] == 'L': idx = litter[(nr, nc)]; new_mask |= (1 << idx)`: If neighbor has litter, set its bit in the mask.
- `if classroom[nr][nc] == 'R': ne = energy`: Stepping on a reset area restores energy to maximum.
- `if new_mask == full_mask: return moves + 1`: All litter collected; current move completes the task.
- `state = (nr, nc, new_mask)`: Key for the visited dictionary.
- `if state not in best or ne > best[state]: best[state] = ne; q.append((nr, nc, new_mask, ne, moves + 1))`: Only enqueue if this state offers strictly more energy than any previous visit to the same position with the same mask.

## Dry Run
Trace of Example 1: `classroom = ["S.", "XL"]`, `energy = 2`.

Grid:
- (0,0) = 'S'
- (0,1) = '.'
- (1,0) = 'X'
- (1,1) = 'L' (index 0)

`total_litter = 1`, `full_mask = 1`.

| Step | r | c | mask | e | moves | Action |
|------|---|---|------|---|-------|--------|
| 1 | 0 | 0 | 0 | 2 | 0 | Pop start. Down (1,0) is 'X' → skip. Right (0,1) is '.' → ne=1, new_mask=0. State (0,1,0) not in best → best[(0,1,0)]=1, push (0,1,0,1,1). |
| 2 | 0 | 1 | 0 | 1 | 1 | Pop. Down (1,1) is 'L' → ne=0, new_mask = 0 \| (1<<0) = 1. new_mask == full_mask → return moves+1 = 2. |

## Complexity
- **Time:** O(m · n · 2^L) where m = rows (≤20), n = cols (≤20), L = number of litter cells (≤10). Each state (r, c, mask) is inserted into the queue at most once per distinct energy improvement; energy ≤ 50 is a constant factor. Each pop examines 4 directions.
- **Space:** O(m · n · 2^L) for the `best` dictionary and the BFS queue, storing at most one entry per (r, c, mask) with the highest energy seen.

## Edge Cases
- **No litter (`total_litter == 0`):** returns 0 immediately (handled).
- **Unreachable litter:** obstacles or energy constraints prevent collecting all litter → returns -1 (queue empties).
- **Reset areas ('R') used multiple times:** entering 'R' sets `ne = energy`; the state is re‑queued with full energy, allowing further moves.
- **Energy = 1:** moving onto 'R' with the last unit of energy resets to full; moving onto 'L' with the last unit collects it and finishes if it was the last litter.
- **Maximum constraints (20×20 grid, 10 litter, energy 50):** state space ≈ 400 × 1024 = 409,600, well within limits.
- **Single litter adjacent to start:** returns 1 (one move).

## Possible Improvements
- **Replace `best` dictionary with a 3D list** `best = [[[-1] * (1 << total_litter) for _ in range(n)] for _ in range(m)]` for O(1) array access and lower overhead.
- **Precompute a litter-index grid** `litter_idx[r][c] = index or -1` to avoid dictionary lookup for 'L' cells.
- The algorithm is already asymptotically optimal for the given constraints; the above are constant‑factor optimisations only.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
