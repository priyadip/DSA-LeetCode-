# 3320. Count The Number of Winning Sequences - Solution Analysis

## Problem Understanding
The problem asks: given Alice's fixed sequence of moves (F, W, E) of length n, count the number of valid Bob sequences (no two consecutive moves identical) such that Bob's total points strictly exceed Alice's. Points are awarded per round in a rock-paper-scissors cycle: F beats E, W beats F, E beats W; ties give 0. The answer is modulo 1e9+7. Constraints: n ≤ 1000, so an O(n^2) dynamic programming solution is feasible, while brute force (3·2^{n-1}) is impossible.

## Approach
The solution uses **dynamic programming** with state compression (rolling array). The DP state is `dp[last_move][diff]` where `last_move ∈ {0,1,2}` represents Bob's move in the current round (F, W, E) and `diff = BobScore - AliceScore` after the processed rounds. The key insight is that the score difference updates additively each round and the only restriction linking rounds is that Bob cannot repeat the same move consecutively. This allows a transition that only depends on the previous move and the current score difference. The brute-force approach would enumerate all 3·2^{n-1} sequences, which is exponential; the DP reduces this to O(n^2) by aggregating sequences that share the same last move and score difference.

## Algorithm
1. Set `MOD = 10^9+7`, `n = len(s)`, `OFFSET = n` (to index negative differences).
2. Precompute a dictionary `score` mapping `(alice_char, bob_move)` to the change in `BobScore - AliceScore` for that round. The mapping follows the cyclic rules: Bob wins → +1, Alice wins → -1, tie → 0.
3. Initialize `cur[3][2n+1]` to all zeros. For the first round (i=0), for each `move ∈ {0,1,2}`, compute `d = score[(s[0], move)]` and set `cur[move][OFFSET + d] = 1`.
4. For each round `i` from 1 to n-1:
   - Create `nxt[3][2n+1]` zeros.
   - For each `last ∈ {0,1,2}` and each `diff` from `-i` to `i` (the reachable range after i rounds):
        - `ways = cur[last][OFFSET + diff]`; if zero, continue.
        - For each `move ∈ {0,1,2}` with `move != last`:
            - `ndiff = diff + score[(s[i], move)]`
            - `nxt[move][OFFSET + ndiff] = (nxt[move][OFFSET + ndiff] + ways) % MOD`
   - Set `cur = nxt`.
5. After the loop, sum `cur[last][OFFSET + diff]` for all `last ∈ {0,1,2}` and `diff ∈ [1, n]` (strictly positive difference) modulo `MOD`.
6. Return the sum.

## Line-by-Line Explanation
- `MOD = 10 ** 9 + 7`: Modulo constant.
- `n = len(s)`: Length of Alice's sequence.
- `OFFSET = n`: Shift to make negative differences non-negative indices.
- `score = { ... }`: Lookup table for the score delta (Bob - Alice) for each pair of Alice's character and Bob's move (0=F,1=W,2=E). The values encode the rock-paper-scissors outcomes.
- `cur = [[0] * (2 * n + 1) for _ in range(3)]`: DP table for the current round; `cur[last][diff+OFFSET]` holds the number of sequences ending with `last` and having score difference `diff`.
- First-round initialization loop: `for move in range(3): d = score[(s[0], move)]; cur[move][OFFSET + d] = 1`. Each possible first move gets one way with its corresponding score difference.
- Main loop `for i in range(1, n):` processes rounds 1 to n-1.
- `nxt = [[0] * (2 * n + 1) for _ in range(3)]`: Next-round DP table.
- `for last in range(3):` iterates over Bob's previous move.
- `for diff in range(-i, i + 1):` iterates over all possible score differences after i rounds (max absolute difference is i).
- `ways = cur[last][OFFSET + diff]; if ways == 0: continue`: Skip unreachable states.
- `for move in range(3): if move == last: continue`: Enforce no consecutive same moves.
- `ndiff = diff + score[(s[i], move)]`: Update score difference with the outcome of round i.
- `nxt[move][OFFSET + ndiff] = (nxt[move][OFFSET + ndiff] + ways) % MOD`: Accumulate ways into the next state.
- `cur = nxt`: Roll the DP array forward.
- Final summation: `ans = 0; for last in range(3): for diff in range(1, n + 1): ans = (ans + cur[last][OFFSET + diff]) % MOD`. Sum all sequences where Bob's total score exceeds Alice's (diff > 0).
- `return ans`: Return the count modulo MOD.

## Dry Run
Trace `s = "FFF"` (n=3). Moves: 0=F,1=W,2=E. Score table for Alice 'F': (F,0)=0, (F,1)=1, (F,2)=-1.

**Initialization (i=0, Alice 'F'):**
| move | d | cur[move][OFFSET+d] |
|------|---|---------------------|
| 0 (F) | 0 | 1 |
| 1 (W) | 1 | 1 |
| 2 (E) | -1 | 1 |

**Round i=1 (Alice 'F'):**
We build nxt from cur. Reachable diffs after 1 round: -1,0,1.
- From last=0 (F), diff=0, ways=1:
    - move=1 (W): ndiff = 0 + 1 = 1 → nxt[1][OFFSET+1] +=1
    - move=2 (E): ndiff = 0 + (-1) = -1 → nxt[2][OFFSET-1] +=1
- From last=1 (W), diff=1, ways=1:
    - move=0 (F): ndiff = 1 + 0 = 1 → nxt[0][OFFSET+1] +=1
    - move=2 (E): ndiff = 1 + (-1) = 0 → nxt[2][OFFSET+0] +=1
- From last=2 (E), diff=-1, ways=1:
    - move=0 (F): ndiff = -1 + 0 = -1 → nxt[0][OFFSET-1] +=1
    - move=1 (W): ndiff = -1 + 1 = 0 → nxt[1][OFFSET+0] +=1

Resulting nxt (non-zero entries):
| last | diff | count |
|------|------|-------|
| 0    | 1    | 1 |
| 0    | -1   | 1 |
| 1    | 1    | 1 |
| 1    | 0    | 1 |
| 2    | -1   | 1 |
| 2    | 0    | 1 |

**Round i=2 (Alice 'F'):**
Process each state from previous round (i=1, max |diff|=1). We'll compute nxt for i=2.
We'll only track states that eventually lead to diff>0 at the end, but let's compute all.

From last=0, diff=1, ways=1:
- move=1: ndiff=1+1=2 → nxt[1][2]+=1
- move=2: ndiff=1-1=0 → nxt[2][0]+=1
From last=0, diff=-1, ways=1:
- move=1: ndiff=-1+1=0 → nxt[1][0]+=1
- move=2: ndiff=-1-1=-2 → nxt[2][-2]+=1
From last=1, diff=1, ways=1:
- move=0: ndiff=1+0=1 → nxt[0][1]+=1
- move=2: ndiff=1-1=0 → nxt[2][0]+=1
From last=1, diff=0, ways=1:
- move=0: ndiff=0+0=0 → nxt[0][0]+=1
- move=2: ndiff=0-1=-1 → nxt[2][-1]+=1
From last=2, diff=-1, ways=1:
- move=0: ndiff=-1+0=-1 → nxt[0][-1]+=1
- move=1: ndiff=-1+1=0 → nxt[1][0]+=1
From last=2, diff=0, ways=1:
- move=0: ndiff=0+0=0 → nxt[0][0]+=1
- move=1: ndiff=0+1=1 → nxt[1][1]+=1

Final cur after i=2 (non-zero):
| last | diff | count |
|------|------|-------|
| 0    | 1    | 1 |
| 0    | 0    | 2 |
| 0    | -1   | 1 |
| 1    | 2    | 1 |
| 1    | 1    | 1 |
| 1    | 0    | 2 |
| 2    | 0    | 2 |
| 2    | -1   | 1 |
| 2    | -2   | 1 |

Sum over diff>0: last=0 diff=1 →1; last=1 diff=2→1, diff=1→1; last=2 none. Total = 3. Matches example output.

## Complexity
- Time: O(n^2). The outer loop runs n-1 times. The inner loops iterate over 3 last moves, at most 2i+1 differences, and 2 next moves (since one is excluded). Total operations ≈ Σ_{i=1}^{n-1} 3·(2i+1)·2 = 12 Σ i + O(n) = 6n^2 + O(n). With n ≤ 1000, this is well within limits.
- Space: O(n). Two 3×(2n+1) arrays are used, each of size O(n). The `score` dictionary is constant size.

## Edge Cases
- **n = 1**: The main loop is skipped. The initialization sets `cur` for the single round. The final sum counts moves where Bob's score > Alice's (diff > 0). For example, if s="F", Bob can play W (diff=1) → 1 way; F (diff=0) and E (diff=-1) are not counted. Correct.
- **All moves identical (e.g., "FFF")**: Handled as in the dry run.
- **Maximum n = 1000**: The DP array size is 3×2001 ≈ 6000 integers, and the loops perform ~6 million iterations, easily fitting in time and memory.
- **Negative differences**: The `OFFSET` shift handles them correctly; the loop bounds `range(-i, i+1)` ensure we only visit reachable indices.
- **Multiple valid answers**: The DP aggregates all sequences, so the sum correctly counts all distinct Bob sequences.

## Possible Improvements
The solution is already optimal in asymptotic complexity for the given constraints (O(n^2) time, O(n) space). A constant-factor improvement could be made by replacing the dictionary `score` with a 3×3 list for faster lookups, but the difference is negligible. The variable names are clear and the rolling array minimizes space. No further algorithmic improvement is needed unless the constraints were larger (e.g., n up to 10^5), which would require a different approach (e.g., matrix exponentiation or generating functions). For n ≤ 1000, this implementation is ideal.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
