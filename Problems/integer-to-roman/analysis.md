# 12. Integer to Roman - Solution Analysis

## Problem Understanding
Convert an integer (1 ≤ num ≤ 3999) to its Roman numeral representation. Roman numerals use seven symbols (I, V, X, L, C, D, M) with specific additive and subtractive rules: symbols are written largest-to-smallest, but 4/9/40/90/400/900 use subtractive pairs (IV, IX, XL, XC, CD, CM). The input range guarantees the output fits in standard Roman numerals without overline notation. Order matters (descending value), duplicates are allowed for powers of ten up to three times, and the algorithm must handle all values in the range.

## Approach
**Greedy with precomputed value-symbol pairs.** The solution encodes every Roman "digit" — both additive (1000, 500, 100, 50, 10, 5, 1) and subtractive (900, 400, 90, 40, 9, 4) — into a single list sorted descending by value. At each step it takes the largest symbol that fits into the remaining number, appends it, and subtracts its value. This works because Roman numerals are essentially a mixed-radix system where each decimal place is independent, and the subtractive forms are just the "digits" for 4 and 9 in each place. Brute force would try all combinations or simulate place-by-place division; the greedy list reduces that to a single linear pass over 13 fixed entries.

**Key insight:** By baking the six subtractive forms into the value list alongside the seven base symbols, the algorithm never needs special-case logic for 4/9 — the greedy choice naturally picks CM before D, CD before C, etc.

## Algorithm
1. Define a constant list of (value, symbol) pairs ordered from largest to smallest, including all subtractive forms.
2. Initialise an empty result string.
3. For each (value, symbol) in the list:
   a. While the remaining `num` ≥ `value`:
      i. Append `symbol` to `result`.
      ii. Subtract `value` from `num`.
4. Return `result`.

## Line-by-Line Explanation
- `roman_tuples = [...]`: Lookup table mapping every Roman "digit" (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000) to its symbol(s), ordered so the greedy loop always picks the largest possible chunk.
- `result = ''`: Accumulator for the output string.
- `for value, roman in roman_tuples:`: Iterate over the 13 pairs once, high to low.
- `while num >= value:`: Repeatedly consume the current value as many times as it fits (0–3 times for base symbols, 0–1 for subtractive forms).
- `result += roman`: Append the corresponding symbol(s).
- `num -= value`: Reduce the remaining number.
- `return result`: Finished when `num` reaches 0.

## Dry Run
Trace `num = 1994` (Example 3):

| Step | value | roman | num before | num ≥ value? | Action | result after | num after |
|------|-------|-------|------------|--------------|--------|--------------|-----------|
| 1 | 1000 | M | 1994 | yes | append M, subtract 1000 | M | 994 |
| 2 | 1000 | M | 994 | no | skip | M | 994 |
| 3 | 900 | CM | 994 | yes | append CM, subtract 900 | MCM | 94 |
| 4 | 500 | D | 94 | no | skip | MCM | 94 |
| 5 | 400 | CD | 94 | no | skip | MCM | 94 |
| 6 | 100 | C | 94 | no | skip | MCM | 94 |
| 7 | 90 | XC | 94 | yes | append XC, subtract 90 | MCMXC | 4 |
| 8 | 50 | L | 4 | no | skip | MCMXC | 4 |
| 9 | 40 | XL | 4 | no | skip | MCMXC | 4 |
| 10 | 10 | X | 4 | no | skip | MCMXC | 4 |
| 11 | 9 | IX | 4 | no | skip | MCMXC | 4 |
| 12 | 5 | V | 4 | no | skip | MCMXC | 4 |
| 13 | 4 | IV | 4 | yes | append IV, subtract 4 | MCMXCIV | 0 |
| 14 | 1 | I | 0 | no | skip | MCMXCIV | 0 |

Output: `"MCMXCIV"`.

## Complexity
- Time: O(1) — the outer loop runs exactly 13 iterations (fixed table size), and the inner `while` executes at most 3 times per base symbol (since 4× would trigger a subtractive form earlier). Total appends ≤ 15 for the maximum input 3999 (MMMCMXCIX). With the constraint `num ≤ 3999`, this is constant time.
- Space: O(1) — only the fixed 13-entry table and the output string (max length 15) are stored. No auxiliary structures scale with input.

## Edge Cases
- **Minimum input (1):** Loop reaches the last pair (1, 'I'), appends once, returns "I".
- **Maximum input (3999):** Produces "MMMCMXCIX" — three M, then CM, XC, IX. The table order ensures CM is chosen before D, etc.
- **Values exactly on subtractive boundaries (4, 9, 40, 90, 400, 900):** The subtractive pair appears earlier in the list than the additive alternative, so it is picked (e.g., 900 triggers CM, not D + CCCC).
- **Values requiring three repeats (3, 30, 300, 3000):** The `while` loop appends the base symbol up to three times before moving to the next lower value.
- **No valid answer / empty input:** Impossible per constraints (`num ≥ 1`).

## Possible Improvements
The solution is already optimal for the given constraints. The 13-entry table is minimal (covers all distinct Roman "digits"), the greedy pass is a single loop with no backtracking, and both time and space are O(1) with tiny constants. A micro-optimisation would be to replace the `while` with integer division and string multiplication (`count = num // value; result += roman * count; num %= value`), reducing Python bytecode overhead, but the asymptotic complexity remains identical and the current code is clearer.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
