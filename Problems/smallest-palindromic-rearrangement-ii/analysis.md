# 3518. Smallest Palindromic Rearrangement II - Solution Analysis

## Problem Understanding
Given a palindromic string `s` (length ≤ 10⁴) and an integer `k` (≤ 10⁶), we must return the k‑th lexicographically smallest **distinct** palindromic permutation of `s`. Because `s` is already a palindrome, its character frequencies contain at most one odd count (the middle character). Every palindromic permutation is uniquely determined by the first half of the string (the second half is the mirror, the middle is fixed). Thus the problem reduces to finding the k‑th permutation of the multiset formed by half of each character’s frequency.

## Approach
The algorithm uses **combinatorial construction** (k‑th permutation of a multiset).  
Brute force would enumerate all permutations, but the number can be factorial. Instead we build the answer left‑to‑right: for each position try characters from `'a'` to `'z'`, compute how many completions exist if that character is placed here (using multinomial coefficients), and either fix the character (if the count ≥ k) or skip that block (subtract the count from k and try the next character).  

**Key insight:** The number of distinct palindromic permutations equals the number of distinct permutations of the half‑counts multiset. This count can be computed as a product of binomial coefficients, and we only need to know whether it reaches `k` (capped at 10⁶+1).

## Algorithm
1. Count frequencies of each character in `s`.
2. Identify the middle character (the one with odd frequency, if any) and store half of each frequency in an array `half[26]`.
3. If `count_perm(half) < k`, return `""` (fewer than `k` permutations exist).
4. Initialise an empty list `left`.
5. While `sum(half) > 0`:
   - For `c` from 0 to 25:
     - If `half[c] == 0`, continue.
     - Decrement `half[c]` (tentatively place this character).
     - Compute `ways = count_perm(half)` (number of completions with the remaining multiset).
     - If `ways >= k`: append `chr(c+97)` to `left`, break the inner loop.
     - Else: `k -= ways`, restore `half[c]`, continue.
6. Return `left + mid + left[::-1]`.

`count_perm(cnt)` computes the multinomial coefficient `total! / (f₁! f₂! …)` by iteratively multiplying `C(total, f)` and subtracting `f` from `total`. It caps the result at `MAX = 10⁶+1`.

`nCk(n, k)` computes the binomial coefficient with the multiplicative formula, stopping early if the value reaches `MAX`.

## Line-by-Line Explanation
- `MAX = 10 ** 6 + 1` – cap for combinatorial counts (k ≤ 10⁶).
- `cnt = Counter(s)` – frequency of each character.
- `half = [0] * 26; mid = ""` – storage for half‑counts and middle character.
- `for ch, f in cnt.items():` – if `f` is odd, `mid = ch`; `half[ord(ch)-97] = f // 2`.
- `if self.count_perm(half) < k: return ""` – not enough permutations.
- `left = []` – will hold the left half.
- `while sum(half):` – until all half characters are used.
- `for c in range(26):` – try characters in lexicographic order.
  - `if half[c] == 0: continue`
  - `half[c] -= 1` – use one occurrence.
  - `ways = self.count_perm(half)` – completions with this prefix.
  - `if ways >= k: left.append(chr(c+97)); break` – fix this character.
  - `k -= ways; half[c] += 1` – skip this block, restore count.
- `left = "".join(left); return left + mid + left[::-1]` – form the palindrome.
- `count_perm(self, cnt):` – computes permutations of multiset `cnt`.
  - `total = sum(cnt); res = 1`
  - `for f in cnt:` – for each frequency.
    - `if f == 0: continue`
    - `res *= self.nCk(total, f)` – choose positions for this character.
    - `if res >= self.MAX: return self.MAX` – early cap.
    - `total -= f`
  - `return res`
- `nCk(self, n, k):` – binomial coefficient with early exit.
  - `k = min(k, n-k)`
  - `ans = 1`
  - `for i in range(1, k+1):`
    - `ans = ans * (n - i + 1) // i`
    - `if ans >= self.MAX: return self.MAX`
  - `return ans`

## Dry Run
Example: `s = "abba"`, `k = 2`.

| Step | half (a,b) | mid | left (so far) | c tried | half after decrement | ways | k | Action |
|------|------------|-----|---------------|---------|----------------------|------|---|--------|
| start | [1,1] | "" | [] | – | – | – | 2 | total perm = 2 ≥ 2 |
| 1 | [1,1] | "" | [] | a (0) | [0,1] | 1 | 2 | 1 < 2 → k=1, restore a |
| 1 | [1,1] | "" | [] | b (1) | [1,0] | 1 | 1 | 1 ≥ 1 → fix 'b', left=['b'] |
| 2 | [1,0] | "" | ['b'] | a (0) | [0,0] | 1 | 1 | 1 ≥ 1 → fix 'a', left=['b','a'] |
| end | [0,0] | "" | "ba" | – | – | – | – | return "ba" + "" + "ab" = "baab" |

## Complexity
- **Time:** O(n) where n = len(s). The outer loop runs `n/2` times. Each iteration tries at most 26 characters; `count_perm` loops over 26 frequencies and calls `nCk`, which runs at most ~11 iterations before hitting `MAX` (since C(23,11) > 10⁶). All operations are O(1) per step.
- **Space:** O(1) – fixed-size arrays (26), a few integers, and the output string.

## Edge Cases
- **Single character** (`s = "a"`): `half` empty, `mid = "a"`, `count_perm` returns 1. k=1 → "a"; k>1 → "".
- **All characters identical** (`s = "aaaa"`): only one permutation; handled correctly.
- **k equals total permutations**: algorithm selects the lexicographically last permutation (e.g., "abba" with k=2 gives "baab").
- **Large k (10⁶) with huge permutation count**: `MAX` cap ensures we never compute massive numbers; `count_perm` returns `MAX` (≥ k) so construction proceeds.
- **Multiple odd frequencies**: impossible by problem guarantee (s is palindromic).

## Possible Improvements
The solution is already optimal for the given constraints (O(n) time, O(1) space). Minor cosmetic improvements could include:
- Maintaining a running `remaining` count instead of `sum(half)` in the while condition (avoids summing 26 elements each iteration, though 26 is constant).
- Using more descriptive variable names (e.g., `freqs` instead of `cnt` in `count_perm`), but current names are clear enough.
- The combinatorial counting is already capped and early‑exited; no further algorithmic speedup is needed.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
