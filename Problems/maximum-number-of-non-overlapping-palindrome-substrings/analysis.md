# 2472. Maximum Number of Non-overlapping Palindrome Substrings - Solution Analysis

## Problem Understanding
We are given a string `s` (length `n ≤ 2000`) and an integer `k ≥ 1`. We must select a set of non‑overlapping substrings such that each substring is a palindrome and has length **at least** `k`. The goal is to maximize the number of selected substrings. Substrings are contiguous and cannot share characters. The constraints rule out an O(n³) brute force (enumerate all substrings, check palindrome, then DP) but allow O(n²) or better. The key observation is that any palindrome of length ≥ `k+2` contains a palindrome of length exactly `k` or `k+1`, so an optimal solution never needs to use longer palindromes – we only need to consider those two lengths.

## Approach
The solution combines **Manacher’s algorithm** with **Dynamic Programming**.

1. **Manacher’s algorithm** computes for every center the maximum radius of odd‑length (`d1`) and even‑length (`d2`) palindromes in O(n) time. This gives O(1) palindrome queries for any substring.
2. **Dynamic Programming**: `dp[i]` = maximum number of valid substrings in the prefix `s[0..i-1]`.  
   Transition:  
   - Skip `s[i-1]`: `dp[i] = dp[i-1]`.  
   - If the last `k` characters form a palindrome, take it: `dp[i] = max(dp[i], dp[i-k] + 1)`.  
   - If the last `k+1` characters form a palindrome, take it: `dp[i] = max(dp[i], dp[i-k-1] + 1)`.  

The insight that only lengths `k` and `k+1` must be checked reduces the DP from O(n²) to O(n) while preserving optimality.

## Algorithm
1. **Manacher for odd lengths**  
   - Initialize `d1` array, `l=0`, `r=-1`.  
   - For each `i` from `0` to `n-1`:  
     - If `i > r`, start with radius `k1 = 1`; else use symmetry `k1 = min(d1[l+r-i], r-i+1)`.  
     - Expand while `s[i-k1] == s[i+k1]`.  
     - Store `d1[i] = k1` and update `l, r` if the palindrome extends further right.
2. **Manacher for even lengths**  
   - Initialize `d2`, `l=0`, `r=-1`.  
   - For each `i`:  
     - If `i > r`, `k2 = 0`; else `k2 = min(d2[l+r-i+1], r-i+1)`.  
     - Expand while `s[i-k2-1] == s[i+k2]`.  
     - Store `d2[i] = k2` and update `l, r`.
3. **Palindrome check helper**  
   - For substring `s[left..right]`, compute its length.  
   - If odd, center = `(left+right)//2`; check `d1[center] >= (length+1)//2`.  
   - If even, center = `(left+right+1)//2`; check `d2[center] >= length//2`.
4. **DP**  
   - `dp[0] = 0`.  
   - For `i = 1 .. n`:  
     - `dp[i] = dp[i-1]`.  
     - If `i ≥ k` and `s[i-k..i-1]` is palindrome: `dp[i] = max(dp[i], dp[i-k] + 1)`.  
     - If `i ≥ k+1` and `s[i-k-1..i-1]` is palindrome: `dp[i] = max(dp[i], dp[i-k-1] + 1)`.  
   - Return `dp[n]`.

## Line-by-Line Explanation
- `n = len(s)`: length of the string.
- `d1 = [0] * n`: array for odd‑length palindrome radii (half‑length rounded up).
- `l = 0; r = -1`: current rightmost palindrome boundary `[l, r]`.
- `for i in range(n):`: iterate over all centers for odd palindromes.
- `if i > r: k1 = 1`: outside current rightmost palindrome, start with radius 1 (the single character).
- `else: k1 = min(d1[l + r - i], r - i + 1)`: inside, use mirrored radius but clamp to stay within `[l, r]`.
- `while (i - k1 >= 0 and i + k1 < n and s[i - k1] == s[i + k1]): k1 += 1`: expand palindrome as far as possible.
- `d1[i] = k1`: store the final radius (palindrome spans `i-k1+1 .. i+k1-1`).
- `if i + k1 - 1 > r: l = i - k1 + 1; r = i + k1 - 1`: update the rightmost boundary if extended.
- `d2 = [0] * n`: array for even‑length palindrome radii (half‑length).
- `l = 0; r = -1`: reset boundaries for even centers.
- `for i in range(n):`: iterate over centers between `i-1` and `i`.
- `if i > r: k2 = 0`: outside, start with radius 0 (empty string).
- `else: k2 = min(d2[l + r - i + 1], r - i + 1)`: mirrored radius clamped.
- `while (i - k2 - 1 >= 0 and i + k2 < n and s[i - k2 - 1] == s[i + k2]): k2 += 1`: expand even palindrome.
- `d2[i] = k2`: store radius (palindrome spans `i-k2 .. i+k2-1`).
- `if i + k2 - 1 > r: l = i - k2; r = i + k2 - 1`: update boundary.
- `def is_palindrome(left, right):`: O(1) check using precomputed radii.
- `length = right - left + 1`: substring length.
- `if length & 1:`: odd length.
- `center = (left + right) // 2`: center index.
- `return d1[center] >= (length + 1) // 2`: required radius for odd palindrome.
- `else:`: even length.
- `center = (left + right + 1) // 2`: center between two characters.
- `return d2[center] >= length // 2`: required radius for even palindrome.
- `dp = [0] * (n + 1)`: DP array, `dp[i]` for prefix of length `i`.
- `for i in range(1, n + 1):`: process prefixes.
- `dp[i] = dp[i - 1]`: option to skip `s[i-1]`.
- `if i >= k:`: enough characters for length `k`.
- `if is_palindrome(i - k, i - 1):`: check suffix of length `k`.
- `dp[i] = max(dp[i], dp[i - k] + 1)`: take it, add 1 to best before it.
- `if i >= k + 1:`: enough for length `k+1`.
- `if is_palindrome(i - k - 1, i - 1):`: check suffix of length `k+1`.
- `dp[i] = max(dp[i], dp[i - k - 1] + 1)`: take it.
- `return dp[n]`: answer for whole string.

## Dry Run
Example: `s = "abaccdbbd"`, `k = 3`, `n = 9`.  
Palindromes of length ≥3: `"aba"` (0‑2), `"dbbd"` (5‑8).  
DP trace (only showing steps where `dp` changes):

| i | dp[i-1] | check len 3 (i-3..i-1) | check len 4 (i-4..i-1) | dp[i] | Action |
|---|---------|------------------------|------------------------|-------|--------|
| 1 | 0       | –                      | –                      | 0     | skip   |
| 2 | 0       | –                      | –                      | 0     | skip   |
| 3 | 0       | "aba" ✓                | –                      | 1     | take "aba" (dp[0]+1) |
| 4 | 1       | "bac" ✗                | "abac" ✗               | 1     | skip   |
| 5 | 1       | "acc" ✗                | "bacc" ✗               | 1     | skip   |
| 6 | 1       | "ccd" ✗                | "accd" ✗               | 1     | skip   |
| 7 | 1       | "cdb" ✗                | "ccdb" ✗               | 1     | skip   |
| 8 | 1       | "dbb" ✗                | "cdbb" ✗               | 1     | skip   |
| 9 | 1       | "bbd" ✗                | "dbbd" ✓               | 2     | take "dbbd" (dp[5]+1) |

Result: `dp[9] = 2`.

## Complexity
- **Time**: O(n)  
  - Manacher (odd + even) visits each character a constant number of times → O(n).  
  - DP loop runs `n` iterations, each does O(1) work → O(n).  
  - Total O(n).
- **Space**: O(n)  
  - Three arrays of length `n` (`d1`, `d2`, `dp`) → O(n).

## Edge Cases
- **k = 1**: Every single character is a valid palindrome. The DP will take a length‑1 palindrome at every step, yielding `dp[n] = n`. Correct.
- **k = n**: Only the whole string can be chosen, and only if it is a palindrome. The DP checks length `n` at `i = n` (via `k` or `k+1`); if it’s a palindrome, `dp[n] = 1`, else `0`. Correct.
- **No palindrome of length ≥ k**: All `is_palindrome` checks fail, `dp` stays `0`. Correct.
- **All characters identical** (e.g., `"aaaaa"`, `k=3`): The DP picks non‑overlapping blocks of length `k` or `k+1` greedily, which is optimal because longer blocks would only reduce the count. The algorithm returns the maximum possible (here `1` for `n=5, k=3`). Correct.
- **Maximum input size (n=2000)**: O(n) time and space easily fit within limits.

## Possible Improvements
The solution is already **optimal** for the given constraints: O(n) time and O(n) space are the best possible (any algorithm must read the input). The only minor cosmetic change would be renaming `d1`/`d2` to `odd_radii`/`even_radii` and `k1`/`k2` to `rad1`/`rad2` for clarity, but this does not affect correctness or performance.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
