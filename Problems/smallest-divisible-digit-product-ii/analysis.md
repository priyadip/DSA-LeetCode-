# 3348. Smallest Divisible Digit Product II - Solution Analysis

## Problem Understanding
We are given a decimal string `num` (no leading zeros) and an integer `t`.  
We must return the smallest **zero‑free** integer (no digit ‘0’) that is **≥ num** and whose digit product is a multiple of `t`. If no such integer exists we return “‑1”.  
Because `t` can be as large as 10¹⁴, the only relevant prime factors are 2, 3, 5, 7; any other factor makes the answer impossible.

## Approach
The solution uses a **BFS on a bounded state space (dynamic programming over exponent vectors)**.  
The brute‑force would try every zero‑free number ≥ num, which is exponential.  
Instead we pre‑compute, for every possible remaining exponent tuple `(e2,e3,e5,e7)` (bounded by the factorisation of `t`), the *shortest* multiset of digits (2‑9) that can supply at least those exponents. This is a classic shortest‑path/BFS on a small directed graph where each edge adds one digit and updates the exponent caps.  
The key insight: once we know the minimal suffix length and its lexicographically smallest composition for any required exponent vector, we can greedily try to increase a digit of `num` from right to left and fill the rest with that optimal suffix.

## Algorithm
1. **Factor `t`** into counts `max2, max3, max5, max7`. If any other prime remains, return “‑1”.  
2. **Build the BFS state space**  
   * State = `(c2,c3,c5,c7)` where each component is capped at its respective `max`.  
   * Initialise state `(0,0,0,0)` with length 0 and empty string.  
   * Repeatedly expand all frontier states by appending each digit `d∈{2…9}`; update the exponent caps (clamp to the maxima).  
   * For each newly reached state store  
     - `min_digits[state]` = minimal number of digits needed,  
     - `best_str[state]` = the smallest (lexicographically) sorted string of those digits.  
   * Keep only the best (longer‑digit‑count‑or‑lexicographically‑larger) candidate for a state.  
3. **Pre‑compute prefix exponent sums of `num`** and a flag `valid_pref[i]` indicating that the prefix `num[:i]` contains no zero.  
4. **Check if `num` itself is valid** (zero‑free and its prefix exponents already meet or exceed the required maxima). If so, return `num`.  
5. **Greedy suffix construction**  
   * Scan positions `i` from right to left. Skip any `i` where the prefix contains a zero.  
   * Let `p2…p7` be the exponent sums of the prefix `num[:i]`.  
   * For each digit `d` larger than `num[i]` (and `d≠0`), compute the *remaining* exponents needed after placing `d`.  
   * Encode this remaining vector to an index `nidx`.  
   * If `min_digits[nidx]` fits into the remaining length (`L‑1‑i`), build the answer as  
     `num[:i] + d + ('1' * (rem‑min_digits[nidx])) + best_str[nidx]` and return it.  
6. **If no position works**, we must lengthen the number.  
   * Encode the full required vector `(max2,max3,max5,max7)` → `total_need`.  
   * Let `total_min = min_digits[total_need]`.  
   * The answer length is `max(L+1, total_min)`.  
   * Pad with leading ‘1’s to reach that length and append `best_str[total_need]`.  

## Line‑by‑Line Explanation
- `class Solution:` – defines the LeetCode solution class.  
- `def smallestNumber(self, num: str, t: int) -> str:` – entry point.  

**Factorisation**
- `temp = t` – copy of `t` for division.  
- `max2 = max3 = max5 = max7 = 0` – initialise exponent counters.  
- `while temp % 2 == 0: …` – count factor 2, divide it out.  
- `while temp % 3 == 0: …` – count factor 3.  
- `while temp % 5 == 0: …` – count factor 5.  
- `while temp % 7 == 0: …` – count factor 7.  
- `if temp != 1: return "-1"` – any remaining prime makes the task impossible.  

**State‑space dimensions**
- `size2 = max2 + 1` … `size7 = max7 + 1` – number of possible values for each exponent (including 0).  
- `stride2 = size3 * size5 * size7` … `stride7 = 1` – pre‑computed multipliers to flatten a 4‑D index into a 1‑D array.  
- `N = size2 * size3 * size5 * size7` – total number of states.  

**Digit factor table**
- `dig_factors = [...]` – for each digit 2‑9 store how many 2/3/5/7 factors it contributes.  
- `dig_strs = ['2', …, '9']` – string representation of each digit, same order as `dig_factors`.  
- `dig_to_idx = {d: i for i, d in enumerate([2,3,4,5,6,7,8,9])}` – map digit → index in the count tuple.  

**BFS containers**
- `min_digits = [-1] * N` – length of the shortest digit multiset reaching each state (`-1` = unreached).  
- `best_str = [None] * N` – the lexicographically smallest sorted digit string for each state.  
- `start_counts = (0,0,0,0,0,0,0,0)` – tuple of digit counts for the empty multiset.  
- `queue = [(0,0,0,0,start_counts)]` – frontier list containing the initial state.  
- `min_digits[0] = 0` – empty state has length 0.  
- `best_str[0] = ""` – empty string for the empty state.  
- `level = 0` – current BFS depth (number of digits used).  

**BFS loop**
- `while queue:` – iterate until no new states appear.  
- `next_cand = {}` – temporary map for the next depth, ensuring we keep only the best candidate per state.  
- `for c2, c3, c5, c7, cnts in queue:` – expand each frontier state.  
- `for d, (a2, a3, a5, a7) in dig_factors:` – try appending each digit.  
- `n2 = c2 + a2; if n2 > max2: n2 = max2` – update exponent, clamp to the required maximum. (Same for `n3,n5,n7`).  
- `nidx = n2 * stride2 + n3 * stride3 + n5 * stride5 + n7` – flatten the new exponent vector.  
- `if min_digits[nidx] != -1: continue` – skip if the state was already reached in an earlier (shorter) level.  
- `d_idx = dig_to_idx[d]` – locate the position of `d` in the count tuple.  
- `new_cnts = list(cnts); new_cnts[d_idx] += 1; new_cnts = tuple(new_cnts)` – increment the count of digit `d`.  
- `if nidx not in next_cand: … else: …` – keep the candidate with the *larger* digit‑count tuple (lexicographically larger) because later we will reconstruct the smallest string by sorting digits; a larger count of a larger digit can only improve the sorted string.  
- After processing all expansions, `if not next_cand: break` – no new states, stop BFS.  
- `next_queue = []` – prepare the frontier for the next level.  
- `for nidx, (n2, n3, n5, n7, ncnts) in next_cand.items():` – finalize each newly discovered state.  
- `min_digits[nidx] = level + 1` – record the length (current depth + 1).  
- `s = ''` … `for d_idx, cnt in enumerate(ncnts): if cnt: s += dig_strs[d_idx] * cnt` – build the sorted digit string for this state.  
- `best_str[nidx] = s` – store it.  
- `next_queue.append((n2, n3, n5, n7, ncnts))` – add to next frontier.  
- `queue = next_queue; level += 1` – advance BFS.  

**Helper to encode a vector**
- `def encode(c2, c3, c5, c7): return c2 * stride2 + c3 * stride3 + c5 * stride5 + c7` – same flattening logic used later.  

**Digit‑to‑factor map for later use**
- `dig_factor_map = {1:(0,0,0,0), 2:(1,0,0,0), …, 9:(0,2,0,0)}` – quick lookup of exponent contribution for any digit 1‑9.  

**Prefix preprocessing**
- `L = len(num)` – length of the input string.  
- `pref2 = [0]*(L+1)` … `pref7 = [0]*(L+1)` – prefix sums of each prime exponent.  
- `valid_pref = [True]*(L+1)` – whether the prefix contains a zero.  
- `r2 = r3 = r5 = r7 = 0; v = True` – running totals and validity flag.  
- `for i, ch in enumerate(num):` – scan the input once.  
  - `if ch == '0': v = False` – any zero invalidates the prefix.  
  - `else: f = dig_factor_map[int(ch)]; r2 += f[0]; …` – add the digit’s contributions.  
  - `pref2[i+1] = r2; …; valid_pref[i+1] = v` – store cumulative data.  

**Whole‑string check**
- `if valid_pref[L] and pref2[L] >= max2 and …:` – if `num` is zero‑free and already supplies enough of each prime, return it.  

**Greedy suffix search**
- `for i in range(L-1, -1, -1):` – iterate positions from rightmost to leftmost.  
  - `if not valid_pref[i]: continue` – cannot keep a prefix that already has a zero.  
  - `p2, p3, p5, p7 = pref2[i], pref3[i], pref5[i], pref7[i]` – exponents of the current prefix.  
  - `curr_d = int(num[i])` – original digit at position `i`.  
  - `for d in range(curr_d + 1, 10):` – try every larger digit (including 0? range stops at 9, but 0 is excluded because start is `curr_d+1`).  
    - `f = dig_factor_map[d]` – factor contribution of candidate digit.  
    - `need2 = max2 - p2 - f[0]; if need2 < 0: need2 = 0` – remaining exponent needed after placing `d` (clamped to 0). (Same for `need3, need5, need7`).  
    - `nidx = encode(need2, need3, need5, need7)` – encode the remaining requirement.  
    - `if min_digits[nidx] <= L - 1 - i:` – can we fit the minimal suffix into the remaining positions?  
      - `rem = L - 1 - i` – number of slots after position `i`.  
      - `m = min_digits[nidx]` – minimal length needed for the required exponents.  
      - `suffix = '1' * (rem - m) + best_str[nidx]` – fill unused slots with ‘1’s (the smallest digit) and then the optimal sorted suffix.  
      - `return num[:i] + str(d) + suffix` – construct and return the answer.  

**Lengthening case**
- `total_need = encode(max2, max3, max5, max7)` – encode the full requirement.  
- `total_min = min_digits[total_need]` – minimal number of non‑‘1’ digits needed.  
- `ans_len = max(L + 1, total_min)` – the answer must be at least one digit longer than `num` (otherwise the previous loop would have succeeded) and at least as long as the minimal suffix.  
- `return '1' * (ans_len - total_min) + best_str[total_need]` – pad with leading ‘1’s and append the optimal suffix.  

**Overall correctness notes**
- The BFS guarantees `min_digits` holds the true shortest length for every exponent vector because each level adds exactly one digit and we never revisit a state with a longer path.  
- `best_str` is built by sorting digits in ascending order, which yields the lexicographically smallest suffix for a given multiset; prefixing with the maximal possible number of ‘1’s (the smallest digit) preserves overall minimality.  
- The greedy scan from right to left ensures the first feasible modification yields the smallest possible overall number, because any change at a more significant position would produce a larger prefix.  
- The algorithm runs in `O(Nstates * 8 + |num|)` time and `O(Nstates)` memory, where `Nstates =

## Dry Run
We trace the algorithm on the first example:

```
num = "1234",   t = 256   (256 = 2^8)
```

### 1. Factorisation of `t`
```
max2 = 8,  max3 = max5 = max7 = 0
```

### 2. DP construction (BFS)
The DP explores all reachable exponent‑tuples `(c2,c3,c5,c7)` up to the caps.
For the needed state `(8,0,0,0)` the BFS discovers the minimal multiset of digits
`{2:1, 8:2}` → string `"288"` (3 digits).  
`min_digits[encode(8,0,0,0)] = 3`, `best_str[encode(8,0,0,0)] = "288"`.

### 3. Prefix information of `num`
| i (0‑based) | digit | pref2 | pref3 | pref5 | pref7 | valid_pref |
|------------|-------|-------|-------|-------|-------|------------|
| 0          | 1     | 0     | 0     | 0     | 0     | True |
| 1          | 2     | 1     | 0     | 0     | 0     | True |
| 2          | 3     | 1     | 0     | 0     | 0     | True |
| 3          | 4     | 3     | 0     | 0     | 0     | True |

`pref2[4] = 3 < max2`, so `num` itself is not a solution.

### 4. Trying to modify a suffix (loop `i = L‑1 … 0`)

| Step | i | p2,p3,p5,p7 (prefix) | curr_d | d tried | f(d) (2‑exponent) | need2 = max2‑p2‑f(d) | encode(need) | min_digits[encode] | remaining positions (L‑1‑i) | Action |
|------|---|----------------------|--------|---------|-------------------|----------------------|--------------|--------------------|-----------------------------|--------|
| 1    | 3 | (3,0,0,0)            | 4      | 5       | 0                 | 5                    | idx5         | 2                  | 0                           | `2 > 0` → continue |
|      |   |                      |        | 6       | 1                 | 4                    | idx4         | 2                  | 0                           | `2 > 0` → continue |
|      |   |                      |        | 7,8,9   | 0,3,0             | 5,2,5                | …            | ≥2                 | 0                           | none fits |
| 2    | 2 | (1,0,0,0)            | 3      | 4       | 2                 | 5                    | idx5         | 2                  | 1                           | `2 > 1` → continue |
|      |   |                      |        | 5       | 0                 | 7                    | idx7         | 3                  | 1                           | `3 > 1` |
|      |   |                      |        | 6       | 1                 | 6                    | idx6         | 2                  | 1                           | `2 > 1` |
|      |   |                      |        | 7,8,9   | 0,3,0             | 7,4,7                | …            | ≥2                 | 1                           | none fits |
| 3    | 1 | (0,0,0,0)            | 2      | 3       | 0                 | 8                    | idx8         | 3                  | 2                           | `3 > 2` |
|      |   |                      |        | 4       | 2                 | 6                    | idx6         | 2                  | 2                           | **fits** |
|      |   |                      |        | –       | –                 | –                    | –            | –                  | –                           | Build answer |
|      |   |                      |        |         |                   |                      |              |                    |                             | `rem = 2`, `m = 2`, `suffix = '' + best_str[encode(6)] = "88"` |
|      |   |                      |        |         |                   |                      |              |                    |                             | Return `"1" + "4" + "88" = "1488"` |

The algorithm stops at `i = 1` with digit `d = 4`, producing the required answer `"1488"`.

---

## Complexity
- **Let**  
  `e2 = max2`, `e3 = max3`, `e5 = max5`, `e7 = max7`.  
  `N = (e2+1)*(e3+1)*(e5+1)*(e7+1)` – number of exponent states.
- **Time**
  - Factorising `t`: `O(log t)` (at most 4 loops).
  - BFS DP: each state is processed once and expands to at most 8 digits → `O(8·N) = O(N)`.
  - Prefix scan of `num`: `O(L)`.
  - Suffix‑search loop: at most `L·9` iterations, each `O(1)` → `O(L)`.
  - **Total:** `O(N + L)`.  
    With the constraints (`t ≤ 10^14`) the worst‑case exponents are  
    `e2 ≤ 46, e3 ≤ 29, e5 ≤ 20, e7 ≤ 16`, giving `N ≤ 4.3·10^5`.
- **Space**
  - Arrays `min_digits` and `best_str` of size `N` → `O(N)`.
  - Queue for BFS holds at most one layer of states → `O(N)` in the worst case.
  - Prefix arrays `O(L)`.
  - **Total:** `O(N + L)`.

---

## Edge Cases
| Situation | How the code handles it |
|-----------|------------------------|
| `t` contains a prime factor other than 2,3,5,7 | Early return `"-1"` after the factorisation loop (`temp != 1`). |
| `num` already satisfies the condition | After building prefix arrays the check `valid_pref[L] and pref* >= max*` returns `num` unchanged. |
| `num` contains a `0` digit | `valid_pref[i]` becomes `False` for any prefix that includes a zero, so suffix modifications are only attempted on zero‑free prefixes. |
| No zero‑free number of the same length works, but a longer one does | After the suffix loop fails, the algorithm uses the pre‑computed DP to build the shortest possible suffix (`best_str[total_need]`) and pads the front with `'1'`s, possibly increasing the total length (`ans_len = max(L+1, total_min)`). |
| Very large `t` (close to `10^14`) | Exponent caps stay bounded (≤ 46 for 2, ≤ 29 for 3, ≤ 20 for 5, ≤ 16 for 7), so `N` stays below half a million; the BFS still finishes comfortably. |
| `num` length = 2 (minimum) | The same logic works; prefix arrays have size `L+1 = 3`, loops iterate correctly. |
| All digits of `num` are `9` and still insufficient | The suffix loop will eventually fall through and the “longer answer” branch will construct a new number with leading `'1'`s. |
| `t = 1` | All exponent caps are zero, DP size is `1`. The early prefix check succeeds because `pref* >= 0`, so the original `num` (if zero‑free) is returned. |
| `t` is a power of a single prime (e.g., `t = 3^10`) | Only the corresponding exponent (`max3`) is non‑zero; DP still explores the 4‑dimensional space but most dimensions are size 1, keeping `N` small. |

All listed cases respect the problem’s constraints; the solution would only fail if the constraints were relaxed (e.g., allowing digits `0` in the answer or primes beyond `{2,3,5,7}`).

---

## Possible Improvements
1. **Tie‑breaking simplification**  
   The inner loop that decides whether a newly discovered state is “better” manually compares digit counts. Because `cnts` is a tuple of counts ordered by increasing digit, a direct tuple comparison (`new_cnts > exist`) yields the same result and is clearer.

2. **Avoid rebuilding strings for every state**  
   `best_str[nidx]` is constructed by concatenating `dig_strs[d_idx] * cnt`. Storing the counts only (as the current `cnts` tuple) and generating the string lazily when needed (only for the final answer) would cut down on repeated string allocations during BFS, reducing constant factors.

3. **Early termination of BFS**  
   The BFS could stop once all states that are reachable within `L` additional digits have been visited, because any state requiring more than `L` digits can never be used for a same‑length solution. This would shrink the explored portion of the state space for very long inputs.

4. **Memory layout**  
   The two parallel arrays `min_digits` (int) and `best_str` (string) could be merged into a single array of a small custom object or a `namedtuple`. This would improve cache locality and slightly lower memory overhead.

5. **Pre‑compute digit factor map once**  
   `dig_factor_map` is built twice (once as a list of tuples, once as a dict). Keeping a single immutable mapping (e.g., a list indexed by digit) eliminates redundancy.

These changes are incremental; the algorithm already meets the optimal `O(N + L)` time and `O(N + L)` space for the given constraints.

---

_Generated by leetvault using groq (openai/gpt-oss-120b)_
