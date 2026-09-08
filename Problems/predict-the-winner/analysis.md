# 486. Predict the Winner - Solution Analysis

## Problem Understanding
Two players alternately pick numbers from either end of an array, adding them to their own score. Player 1 starts. Both play optimally. Return `true` if Player 1's final score is at least Player 2's (ties count as a win for Player 1). The array length is at most 20, values up to 10^7. The small length allows O(n²) DP; the zero-sum nature means we only need to track the score difference the current player can secure.

## Approach
**Pattern:** Dynamic Programming (interval DP) with space optimization to 1D.  
**Why it fits:** The game state is fully defined by the remaining subarray `nums[i..j]`. The optimal score difference for the current player on that interval depends only on the two smaller intervals after taking the left or right end. This is a classic minimax/zero-sum game on an interval.  
**Brute force:** Recursion exploring both choices at every turn gives O(2ⁿ) time.  
**Chosen approach:** Bottom-up DP computes the maximum net score difference `dp[i][j]` the current player can achieve over the opponent on subarray `i..j`. The recurrence is `dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])`. The 1D optimization overwrites `dp[j]` in place because row `i` only needs row `i+1` (old `dp[j]`) and the current row's left neighbour (new `dp[j-1]`).  
**Key insight:** In a zero-sum game with perfect play, the current player's best net advantage equals the chosen end value minus the opponent's best net advantage on the remaining interval.

## Algorithm
1. Let `n = len(nums)`. Initialise a 1D array `dp` as a copy of `nums`; `dp[i]` represents the net score difference for the single-element interval `[i, i]`.
2. Iterate `i` from `n-2` down to `0` (expanding intervals leftward).
3. For each `i`, iterate `j` from `i+1` to `n-1` (expanding intervals rightward).
4. Update `dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])`:
   - `nums[i] - dp[j]`: take left end; `dp[j]` still holds the value for interval `[i+1, j]` from the previous outer iteration.
   - `nums[j] - dp[j-1]`: take right end; `dp[j-1]` was just updated in this inner loop and now holds the value for interval `[i, j-1]`.
5. After all loops, `dp[n-1]` holds the net score difference for the full array `[0, n-1]`. Return `true` if it is ≥ 0.

## Line-by-Line Explanation
- `n = len(nums)`: length of the array.
- `dp = nums[:]`: initialise DP with base cases `dp[i] = nums[i]` (interval of length 1, current player takes the only element).
- `for i in range(n - 2, -1, -1):`: outer loop moves the left boundary leftwards, building longer intervals.
- `for j in range(i + 1, n):`: inner loop moves the right boundary rightwards for the current left boundary.
- `dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])`: core recurrence. `dp[j]` (old) is `dp[i+1][j]`; `dp[j-1]` (new) is `dp[i][j-1]`. The current player picks the end that maximises their net advantage.
- `return dp[-1] >= 0`: `dp[n-1]` now holds the net advantage for the whole array; non-negative means Player 1 wins or ties.

## Dry Run
Example: `nums = [1, 5, 2]`

Initial: `dp = [1, 5, 2]`

| Step | i | j | nums[i] | nums[j] | old dp[j] (dp[i+1][j]) | new dp[j-1] (dp[i][j-1]) | left pick | right pick | new dp[j] | dp array after |
|------|---|---|---------|---------|------------------------|--------------------------|-----------|------------|-----------|----------------|
| 1    | 1 | 2 | 5       | 2       | 2                      | 5                        | 5-2=3     | 2-5=-3     | 3         | [1, 5, 3]      |
| 2    | 0 | 1 | 1       | 5       | 5                      | 1                        | 1-5=-4    | 5-1=4      | 4         | [1, 4, 3]      |
| 3    | 0 | 2 | 1       | 2       | 3                      | 4                        | 1-3=-2    | 2-4=-2     | -2        | [1, 4, -2]     |

Final `dp[-1] = -2 < 0` → return `False`. Matches example.

## Complexity
- **Time:** O(n²) — two nested loops over `n ≤ 20`, each iteration O(1).
- **Space:** O(n) — single array of length `n` replaces the 2D table.

## Edge Cases
- **Single element (`n=1`):** Outer loop doesn't run; `dp[-1] = nums[0] ≥ 0` → `True`. Correct: Player 1 takes the only number and wins.
- **All equal values:** e.g., `[5,5,5]`. DP computes net difference 5 (Player 1 gets two 5s, Player 2 gets one) → `True`.
- **Large values up to 10⁷:** Python integers handle sums up to 20·10⁷ easily; no overflow.
- **Already sorted / reverse sorted:** Order doesn't matter; DP examines all intervals.
- **No valid answer:** Not applicable — game always terminates with a winner/tie.

## Possible Improvements
The solution is already optimal for the given constraints (n ≤ 20). The 1D DP achieves O(n²) time and O(n) space, which is the best asymptotic complexity for this problem. The commented-out recursive and 2D versions are functionally equivalent but use more space or recursion overhead. No material improvement is needed; variable names (`dp`, `i`, `j`) are standard for this pattern.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
