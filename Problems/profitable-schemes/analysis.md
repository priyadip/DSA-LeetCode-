# 879. Profitable Schemes - Solution Analysis

## Problem Understanding
We have `n` members and a list of crimes; crime `i` requires `group[i]` members and yields `profit[i]` profit. A member can participate in at most one crime. We need to count the number of subsets of crimes (schemes) such that the total members used ≤ `n` and the total profit ≥ `minProfit`. The answer is returned modulo 10⁹+7. Constraints: `n ≤ 100`, `minProfit ≤ 100`, up to 100 crimes, each `group[i] ≤ 100`, `profit[i] ≤ 100`. These bounds make a three‑dimensional DP (crime index, members used, profit capped at `minProfit`) feasible.

## Approach
The solution uses **top‑down dynamic programming with memoization** (recursion + `@cache`). This is a 0/1 knapsack variant with two constraints (members and profit) where we count subsets instead of maximizing value.  
Brute force would enumerate all 2¹⁰⁰ subsets – impossible. The DP reduces the state space to `O(len(group) * n * minProfit)` ≈ 10⁶ states.  
**Key insight:** Profit beyond `minProfit` is irrelevant for the “at least” condition, so we can cap accumulated profit at `minProfit`, turning the profit dimension into a small bounded range.

## Algorithm
1. Define a recursive function `fn(i, p, minc)` returning the number of valid schemes considering crimes from index `i` onward, given that `p` members have already been used and the accumulated profit (capped at `minProfit`) is `minc`.
2. **Base case:** If `i == len(group)`, return `1` if `minc == minProfit` (i.e., target profit reached) else `0`.
3. **Skip crime `i`:** Add `fn(i+1, p, minc)` to the answer.
4. **Take crime `i` (if possible):** If `p + group[i] ≤ n`, compute `new_minc = min(minProfit, minc + profit[i])` and add `fn(i+1, p + group[i], new_minc)`.
5. Return the sum modulo `10⁹+7`.
6. The final answer is `fn(0, 0, 0)`.

## Line-by-Line Explanation
- `mod = 10**9 + 7`: Modulus for the result.
- `@cache`: Memoizes `fn` so each state `(i, p, minc)` is computed once.
- `def fn(i, p, minc):`: State parameters – crime index, members used, capped profit.
- `if i >= len(group): return 1 if minc == minProfit else 0`: Base case – no more crimes; count this scheme only if profit target met.
- `ways = fn(i+1, p, minc)`: Count schemes that skip the current crime.
- `if p + group[i] <= n:`: Check if we have enough members left to commit this crime.
- `new = min(minProfit, minc + profit[i])`: Update profit, capping at `minProfit`.
- `ways += fn(i+1, p + group[i], new)`: Add schemes that include this crime.
- `return ways % mod`: Apply modulus and return.
- `return fn(0, 0, 0)`: Start with no crimes considered, 0 members used, 0 profit.

## Dry Run
Example 1: `n = 5, minProfit = 3, group = [2,2], profit = [2,3]`.

We trace the memoized states in post‑order (base cases first, then `i=1`, then `i=0`). Only reachable states are shown.

| i | p | minc | Computation (ways) | Returned |
|---|---|------|---------------------|----------|
| 2 | 0 | 0    | base: minc≠3        | 0 |
| 2 | 0 | 2    | base: minc≠3        | 0 |
| 2 | 0 | 3    | base: minc==3       | 1 |
| 2 | 2 | 0    | base: minc≠3        | 0 |
| 2 | 2 | 2    | base: minc≠3        | 0 |
| 2 | 2 | 3    | base: minc==3       | 1 |
| 2 | 4 | 0    | base: minc≠3        | 0 |
| 2 | 4 | 2    | base: minc≠3        | 0 |
| 2 | 4 | 3    | base: minc==3       | 1 |
| 1 | 0 | 0    | fn(2,0,0) + fn(2,2,3) = 0+1 | 1 |
| 1 | 0 | 2    | fn(2,0,2) + fn(2,2,3) = 0+1 | 1 |
| 1 | 0 | 3    | fn(2,0,3) + fn(2,2,3) = 1+1 | 2 |
| 1 | 2 | 0    | fn(2,2,0) + fn(2,4,3) = 0+1 | 1 |
| 1 | 2 | 2    | fn(2,2,2) + fn(2,4,3) = 0+1 | 1 |
| 1 | 2 | 3    | fn(2,2,3) + fn(2,4,3) = 1+1 | 2 |
| 1 | 4 | 0    | fn(2,4,0) = 0 | 0 |
| 1 | 4 | 2    | fn(2,4,2) = 0 | 0 |
| 1 | 4 | 3    | fn(2,4,3) = 1 | 1 |
| 0 | 0 | 0    | fn(1,0,0) + fn(1,2,2) = 1+1 | **2** |

Final answer: 2.

## Complexity
- **Time:** `O(len(group) * n * minProfit)` – each of the at most `101 * 101 * 101 ≈ 10⁶` states is computed once with `O(1)` work.
- **Space:** `O(len(group) * n * minProfit)` for the memoization cache, plus `O(len(group))` recursion depth (≤ 100).

## Edge Cases
- **`minProfit = 0`:** Every subset with total members ≤ `n` is valid. The code works because `minc` starts at 0 and is capped at 0, so every base case returns 1.
- **`profit[i] = 0`:** Taking such a crime consumes members but does not increase profit; `new = minc` handles this correctly.
- **`group[i] > n`:** The crime can never be taken because the `if` condition fails; it is effectively skipped.
- **Large inputs (max constraints):** 100 crimes, `n=100`, `minProfit=100` – recursion depth 100 is well within Python’s default recursion limit (1000), so no stack overflow.
- **All crimes have profit 0 and `minProfit > 0`:** No scheme can reach the target; the code correctly returns 0 because base cases never satisfy `minc == minProfit`.

## Possible Improvements
The solution is already optimal in asymptotic complexity for the given constraints. Minor readability improvements:
- Rename `p` → `used` (members used) and `minc` → `cur_profit` (capped profit) for clarity.
- An iterative bottom‑up DP would avoid recursion overhead and any theoretical recursion‑limit concerns, but the current top‑down approach is concise and performs well within the limits.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
