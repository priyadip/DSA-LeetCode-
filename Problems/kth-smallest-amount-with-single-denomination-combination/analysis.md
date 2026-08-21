# 3116. Kth Smallest Amount With Single Denomination Combination - Solution Analysis

## Problem Understanding
We are given an array `coins` of distinct denominations (length ≤ 15, each ≤ 25) and an integer `k` (≤ 2·10⁹). We have infinitely many coins of each denomination but **cannot mix denominations**; thus the achievable amounts are exactly the multiples of each individual coin. The task is to find the k‑th smallest distinct amount in the union of these multiples. Duplicates across different coins (e.g., 6 is a multiple of both 3 and 6) count only once. The constraints rule out generating amounts explicitly; we need an efficient way to count how many distinct amounts are ≤ a given value `x`.

## Approach
The solution uses **binary search on the answer** combined with the **inclusion–exclusion principle** to count the number of distinct multiples ≤ `x`.

- **Binary search** works because the count of achievable amounts ≤ `x` is monotonic in `x`. The search space is `[1, min(coins)·k]` – the smallest coin alone produces at least `k` multiples by that value.
- **Inclusion–exclusion** counts the union of multiples: for each non‑empty subset of coins, compute the LCM of the subset. The number of multiples of that LCM up to `x` is `⌊x / LCM⌋`. Add this for odd‑sized subsets, subtract for even‑sized subsets. With `n ≤ 15`, there are at most 32 767 subsets, making each count call fast.
- **Key insight**: The union of arithmetic progressions (multiples of each coin) can be counted exactly via inclusion–exclusion on the LCMs of all subsets.

## Algorithm
1. **Pre‑define helpers**: `lcm(a, b) = a // gcd(a, b) * b`.
2. **Count function `count(x)`**:
   - Initialise `total = 0`.
   - Iterate `mask` from `1` to `(1 << n) - 1` (all non‑empty subsets).
   - For each `mask`, compute `L = LCM` of coins in the subset and `bits = popcount(mask)`.
   - `ways = x // L`.
   - If `bits` is odd, `total += ways`; else `total -= ways`.
   - Return `total`.
3. **Binary search**:
   - `left = 1`, `right = min(coins) * k`.
   - While `left < right`:
     - `mid = left + (right - left) // 2`.
     - If `count(mid) >= k`: `right = mid`.
     - Else: `left = mid + 1`.
   - Return `left`.

## Line-by-Line Explanation
- `n = len(coins)`: number of denominations.
- `def lcm(a, b): return a // gcd(a, b) * b`: computes least common multiple using GCD.
- `def count(x):`: closure that counts distinct multiples ≤ `x`.
- `total = 0`: accumulator for inclusion–exclusion sum.
- `for mask in range(1, 1 << n):`: loops over all non‑empty subsets via bitmask.
- `L = 1; bits = 0`: initialise LCM and subset size for this mask.
- `for i in range(n):`: iterates over coin indices.
- `if mask & (1 << i):`: checks if coin `i` is in the subset.
- `L = lcm(L, coins[i])`: updates LCM with the new coin.
- `bits += 1`: increments subset cardinality.
- `ways = x // L`: number of multiples of `L` not exceeding `x`.
- `if bits % 2 == 1: total += ways else: total -= ways`: inclusion–exclusion sign.
- `return total`: final count of distinct amounts ≤ `x`.
- `left = 1; right = min(coins) * k`: binary search bounds.
- `while left < right:`: standard lower‑bound binary search.
- `mid = left + (right - left) // 2`: midpoint avoiding overflow.
- `if count(mid) >= k: right = mid else: left = mid + 1`: narrows search to smallest `x` with count ≥ `k`.
- `return left`: the k‑th smallest amount.

## Dry Run
Example: `coins = [3, 6, 9]`, `k = 3`.  
`n = 3`, `min(coins) = 3`, `right = 9`.

| Step | left | right | mid | count(mid) | Action |
|------|------|-------|-----|------------|--------|
| 1    | 1    | 9     | 5   | 1          | 1 < 3 → left = 6 |
| 2    | 6    | 9     | 7   | 2          | 2 < 3 → left = 8 |
| 3    | 8    | 9     | 8   | 2          | 2 < 3 → left = 9 |
| 4    | 9    | 9     | –   | –          | loop ends, return 9 |

`count(5)` details: subsets {3}→1, {6}→0, {3,6}→0, {9}→0, {3,9}→0, {6,9}→0, {3,6,9}→0 → total 1.  
`count(7)`: {3}→2, {6}→1, {3,6}→1, others 0 → 2+1-1=2.  
`count(8)`: {3}→2, {6}→1, {3,6}→1 → 2.  
`count(9)`: {3}→3, {6}→1, {3,6}→1, {9}→1, {3,9}→1, {6,9}→0, {3,6,9}→0 → 3+1-1+1-1=3 ≥ 3.

## Complexity
- **Time**: O(2ⁿ · n · log(min(coins)·k)).  
  `n ≤ 15` → 2ⁿ = 32 768. Each `count` iterates all subsets and does O(n) work per subset (LCM updates). Binary search performs O(log(min(coins)·k)) ≤ 36 iterations. Total ≈ 1.2·10⁶ operations.
- **Space**: O(1) extra (only a few integer variables). The recursion depth is constant; no auxiliary arrays proportional to input size.

## Edge Cases
- **k = 1**: returns `min(coins)` (smallest multiple).
- **Coin value 1**: every positive integer is achievable; answer is `k`. Inclusion–exclusion handles this because LCM of any subset containing 1 is 1, and the formula correctly yields `x`.
- **Large k (2·10⁹)**: `right = min(coins)·k` fits easily in Python’s arbitrary‑precision integers; in fixed‑width languages 64‑bit is sufficient (max 25·2·10⁹ = 5·10¹⁰).
- **LCM overflow**: maximum LCM of numbers ≤ 25 is 26 771 144 400, well within 64‑bit.
- **All coins pairwise coprime**: inclusion–exclusion still works; no special handling needed.
- **Constraints guarantee non‑empty `coins` and `k ≥ 1`**, so empty input or zero `k` are not applicable.

## Possible Improvements
- **Pre‑compute subset LCMs and parities**: Since `coins` is fixed, compute an array `subset_lcm[mask]` and `subset_bits[mask]` once before binary search. This reduces each `count(x)` call from O(2ⁿ·n) to O(2ⁿ), a ~15× speedup for the inner loop.
- **Early exit in `count`**: If `L > x`, then `x // L == 0`; further LCM updates for supersets will only increase `L`, so we could break early. However, with pre‑computation this is less critical.
- **Tighter upper bound**: `right = min(coins) * k` is safe but sometimes loose; we could use `min(coins) * k` as is – it’s already logarithmic.
- **Variable naming**: `L` → `lcm_val`, `bits` → `popcount`, `ways` → `multiples` would improve readability without changing logic.

The solution is already asymptotically optimal for the given constraints (binary search + inclusion–exclusion is the standard approach). The suggested pre‑computation is a constant‑factor optimisation that would make it faster in practice.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
