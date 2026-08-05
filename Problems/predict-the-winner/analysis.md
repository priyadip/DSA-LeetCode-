# 486. Predict the Winner - Solution Analysis

## Problem Understanding
The problem asks whether Player 1 can guarantee a score greater than or equal to Player 2 in a turn-based game played on an integer array `nums`. 

On each turn, the active player chooses a number from either the left or right end of the array, adds it to their score, and removes it from the array. Both players play optimally to maximize their final relative score margin (their score minus the opponent's score).

Constraints:
- $1 \le n \le 20$, where $n$ is `len(nums)`.
- $0 \le nums[i] \le 10^7$.

Because $n$ is small, subproblem results can be cached to evaluate game states without recalculating them.

---

## Approach
This solution uses **Minimax Dynamic Programming** space-optimized to a 1D array.

In a zero-sum game, a standard state definition is `dp[i][j]`: the maximum net score difference (`current_player_score - opponent_score`) the active player can achieve on the subarray `nums[i...j]`.

The recursive relation is:
$$\text{dp}[i][j] = \max(nums[i] - \text{dp}[i+1][j], \; nums[j] - \text{dp}[i][j-1])$$

Notice that computing row `i` only depends on:
1. `dp[i+1][j]` (the subproblem from the row below, i.e., index $i+1$).
2. `dp[i][j-1]` (the subproblem from the current row, i.e., index $j-1$).

By iterating the left boundary `i` backwards from $n-2$ down to $0$, and the right boundary `j` forwards from $i+1$ to $n-1$, we can overwrite a single 1D array `dp` of size $n$ in-place:
- `dp[j]` before modification stores $\text{dp}[i+1][j]$.
- `dp[j-1]` after modification stores $\text{dp}[i][j-1]$.

---

## Algorithm
1. Initialize a 1D array `dp` as a copy of `nums`. Initially, `dp[i]` represents subproblems of length 1 where $i = j$ ($\text{dp}[i][i] = nums[i]$).
2. Loop `i` backwards from `n - 2` down to `0` (left index of current subarray).
3. Loop `j` forwards from `i + 1` up to `n - 1` (right index of current subarray).
4. For each pair $(i, j)$, update `dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])`.
5. Return `True` if `dp[-1] >= 0` (the net score margin for the full range $0 \dots n-1$ is non-negative), otherwise `False`.

---

## Line-by-Line Explanation

```python3
n = len(nums)
dp = nums[:]          # dp[i] = dp[i][i]
```
`n` stores the size of the array. `dp` is initialized as a clone of `nums`. Initially, `dp[i]` holds the base case where subarray length is $1$ ($i = j$). Picking `nums[i]` leaves no elements for the opponent, so net score difference is `nums[i]`.

```python3
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
```
The outer loop moves the start index `i` backward from `n-2` to `0`. The inner loop moves the end index `j` forward from `i+1` to `n-1`. This guarantees that for any subproblem $(i, j)$, both necessary subproblems $(i+1, j)$ and $(i, j-1)$ have already been computed.

```python3
        dp[j] = max(
            nums[i] - dp[j],      # old dp[j] = dp[i+1][j]
            nums[j] - dp[j - 1]   # dp[j-1] = dp[i][j-1]
        )
```
Updates `dp[j]` for subarray `nums[i...j]`. 
- `nums[i] - dp[j]` calculates taking the left element `nums[i]` minus opponent's optimal margin on `nums[i+1...j]`.
- `nums[j] - dp[j - 1]` calculates taking the right element `nums[j]` minus opponent's optimal margin on `nums[i...j-1]`.

```python3
return dp[-1] >= 0
```
`dp[-1]` (which is `dp[n-1]`) holds the net score margin for the full array `nums[0...n-1]`. If it is $\ge 0$, Player 1 wins or ties, so return `True`.

---

## Dry Run

Trace for `nums = [1, 5, 2]` ($n = 3$):

Initial state: `dp = [1, 5, 2]`

| Step | `i` | `j` | Subarray | Decision Calculation | `dp` State |
|---|---|---|---|---|---|
| Start | - | - | - | Initial base cases | `[1, 5, 2]` |
| 1 | 1 | 2 | `[5, 2]` | `max(nums[1] - dp[2], nums[2] - dp[1])` = `max(5 - 2, 2 - 5) = 3` | `[1, 5, 3]` |
| 2 | 0 | 1 | `[1, 5]` | `max(nums[0] - dp[1], nums[1] - dp[0])` = `max(1 - 5, 5 - 1) = 4` | `[1, 4, 3]` |
| 3 | 0 | 2 | `[1, 5, 2]` | `max(nums[0] - dp[2], nums[2] - dp[1])` = `max(1 - 3, 2 - 4) = -2` | `[1, 4, -2]` |

Final check: `dp[-1] >= 0` $\rightarrow$ `-2 >= 0` $\rightarrow$ `False`.

---

## Complexity

- **Time Complexity:** $O(n^2)$ where $n$ is the length of `nums`. The double nested loop evaluates $\frac{n(n-1)}{2}$ subproblems, executing constant time operations $O(1)$ per state.
- **Space Complexity:** $O(n)$ where $n$ is the length of `nums`. The state was optimized from a full $O(n^2)$ 2D matrix down to a single 1D array of size $n$.

---

## Edge Cases

- **Single element ($n = 1$):** `range(n - 2, -1, -1)` evaluates to `range(-1, -1, -1)`, which is empty. The loops do not execute, and `dp[-1] >= 0` evaluates `nums[0] >= 0` which returns `True`.
- **All elements equal:** Player 1 can always control game progression to tie or win. Handled correctly.
- **Zeros in array ($nums[i] = 0$):** Zero elements add no score margin; handled natively by standard subtraction logic.

---

## Possible Improvements

For even-length arrays ($n \pmod 2 == 0$), Player 1 can **always** win or tie. 

Player 1 can partition the array indices into two sets: odd indices and even indices. Player 1 can force picking *all* even-indexed numbers or *all* odd-indexed numbers throughout the game. Since total score is fixed, picking the set with the larger or equal sum guarantees a score $\ge$ Player 2's score.

Adding an $O(1)$ parity check at the beginning avoids unnecessary dynamic programming loops for even lengths:

```python3
if len(nums) % 2 == 0:
    return True
```

---

_Generated by leetvault using gemini (gemini-flash-latest)_
