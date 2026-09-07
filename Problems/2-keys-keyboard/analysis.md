# 650. 2 Keys Keyboard - Solution Analysis

## Problem Understanding
We start with one 'A' on screen and an empty clipboard. Allowed operations: **Copy All** (copies the entire current screen content to clipboard, overwriting it) and **Paste** (appends the clipboard content to the screen). Given `n` (1 ≤ n ≤ 1000), find the minimum number of operations to obtain exactly `n` 'A's on screen. The order of operations matters; the clipboard can only hold a full copy of the screen at the moment of copying. The constraints are small enough for an O(n²) dynamic programming solution.

## Approach
The solution uses **Dynamic Programming** on a state space defined by two variables: `curr` (number of 'A's currently on screen) and `clip` (number of 'A's in the clipboard). This is a shortest-path problem on a directed acyclic graph where each state transitions via Copy All or Paste. Because `curr` never decreases and `clip` never exceeds `curr` (after a copy, `clip = curr`; paste only increases `curr`), the graph has no cycles. The DP is filled bottom‑up from the target `n` down to the start state `(1, 0)`.  

**Brute‑force** would explore all sequences of operations (exponential). The DP reduces this to O(n²) by memoising the minimum steps from each state.  

**Key insight:** The state `(curr, clip)` only moves to states with larger `curr` or same `curr` but larger `clip`, so processing `curr` from `n` down to `1` and `clip` from `n` down to `0` guarantees that all dependencies are already computed.

## Algorithm
1. Create a 2D array `dp` of size `(n+1) × (n+1)` initialized to infinity.
2. **Base case:** For every `clip` in `0..n`, set `dp[n][clip] = 0` (already reached `n` 'A's).
3. For `curr` from `n-1` down to `1`:
   For `clip` from `n` down to `0`:
   - `ans = INF`
   - **Copy All:** If `curr != clip` (copying when clipboard already equals screen is useless), consider `1 + dp[curr][curr]`.
   - **Paste:** If `clip > 0` and `curr + clip ≤ n`, consider `1 + dp[curr + clip][clip]`.
   - `dp[curr][clip] = ans`.
4. Return `dp[1][0]` (start with one 'A' on screen, empty clipboard).

## Line-by-Line Explanation
- `INF = float('inf')`: Sentinel for unreachable states.
- `dp = [[INF] * (n + 1) for _ in range(n + 1)]`: Allocates the DP table; `dp[curr][clip]` will hold the minimum steps from that state.
- `for clip in range(n + 1): dp[n][clip] = 0`: Base case – if we already have `n` 'A's, zero further steps are needed regardless of clipboard content.
- `for curr in range(n - 1, 0, -1):`: Iterate current screen count downward from `n-1` to `1`.
- `for clip in range(n, -1, -1):`: Iterate clipboard count downward from `n` to `0`.
- `ans = INF`: Temporary variable to accumulate the minimum.
- `if curr != clip: ans = min(ans, 1 + dp[curr][curr])`: Copy All operation – allowed only when clipboard differs from screen; new state is `(curr, curr)`.
- `if clip and curr + clip <= n: ans = min(ans, 1 + dp[curr + clip][clip])`: Paste operation – allowed only when clipboard non‑empty and pasting doesn't exceed `n`; new state is `(curr+clip, clip)`.
- `dp[curr][clip] = ans`: Store the computed minimum.
- `return dp[1][0]`: Answer for the initial state (1 'A' on screen, empty clipboard).

## Dry Run
Trace for `n = 3`. The table is filled for `curr = 2, 1` and `clip = 3, 2, 1, 0`. Only reachable states are shown.

| Step | curr | clip | Copy allowed? | Paste allowed? | dp[curr][clip] | Action |
|------|------|------|---------------|----------------|----------------|--------|
| Base | 3    | any  | –             | –              | 0              | base case |
| 1    | 2    | 3    | no (2≠3)      | no (2+3>3)     | INF            | unreachable |
| 2    | 2    | 2    | no (2=2)      | yes (2+2>3)    | INF            | unreachable |
| 3    | 2    | 1    | yes (2≠1)     | yes (2+1=3)    | min(1+dp[2][2], 1+dp[3][1]) = min(1+INF, 1+0) = 1 | Paste to reach 3 |
| 4    | 2    | 0    | yes (2≠0)     | no (clip=0)    | 1+dp[2][2] = INF | Copy leads to dead end |
| 5    | 1    | 3    | yes (1≠3)     | no (1+3>3)     | 1+dp[1][1] = INF | Copy leads to dead end |
| 6    | 1    | 2    | yes (1≠2)     | no (1+2=3≤3)   | min(1+dp[1][1], 1+dp[3][2]) = min(INF, 1) = 1 | Paste to reach 3 |
| 7    | 1    | 1    | no (1=1)      | yes (1+1=2)    | 1+dp[2][1] = 1+1 = 2 | Paste to (2,1) |
| 8    | 1    | 0    | yes (1≠0)     | no (clip=0)    | 1+dp[1][1] = 1+2 = 3 | Copy then follow (1,1) path |

Result: `dp[1][0] = 3`, matching the example.

## Complexity
- **Time:** O(n²) – two nested loops each run up to `n` times, constant work inside.
- **Space:** O(n²) – the `(n+1) × (n+1)` DP table.  
Here `n ≤ 1000`, so the table has ~1,000,000 entries, which fits comfortably in memory and time limits for Python.

## Edge Cases
- **n = 1:** The outer loop `range(n-1, 0, -1)` is empty; base case sets `dp[1][0] = 0`, correctly returning 0.
- **n = 1000:** Maximum input; DP table size ~1e6, runs within typical limits.
- **All states where `clip > curr`** are never reached because clipboard can never exceed screen content (copy sets `clip = curr`, paste only increases `curr`). The loops still iterate over them but they stay `INF` and do not affect the answer.
- The condition `curr != clip` for Copy All correctly avoids a useless self‑copy that would waste a step.

## Possible Improvements
The solution is correct but not asymptotically optimal. The problem has a well‑known mathematical solution: the minimum steps equal the **sum of prime factors of `n`** (e.g., for `n = 12 = 2·2·3`, answer = 2+2+3 = 7). That approach runs in O(√n) time and O(1) space. For the given constraint `n ≤ 1000` the O(n²) DP is acceptable, but if `n` were larger (e.g., 10⁹) the prime‑factor method would be necessary. No other material improvements (variable names, redundant passes) are needed for the current constraints.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
