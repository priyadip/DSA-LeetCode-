# 22. Generate Parentheses - Solution Analysis

## Problem Understanding
Given an integer `n` (1 ≤ n ≤ 8), generate all distinct strings of length `2n` consisting of `'('` and `')'` that are well‑formed (every opening parenthesis has a matching closing parenthesis and they are properly nested). The order of the output list does not matter. The Catalan number `C_n` gives the exact count of such strings, which is small enough for `n ≤ 8` to allow exhaustive generation.

## Approach
The solution uses **backtracking** (depth‑first search) to build strings incrementally. At each step we decide whether to append `'('` or `')'`, subject to two constraints:
1. The total number of `'('` cannot exceed `n`.
2. A `')'` can only be added if there are more `'('` than `')'` so far (i.e., `close_count < open_count`).

This prunes invalid prefixes early. A brute‑force approach would generate all `2^(2n)` strings and filter the valid ones, which is far less efficient. The key insight is that **any prefix with `open_count ≥ close_count` and `open_count ≤ n` can be extended to a valid full string**, so we only explore those prefixes.

## Algorithm
1. Initialize an empty list `result` to collect valid strings and an empty list `current` to build the current string efficiently.
2. Define a recursive function `backtrack(open_count, close_count)`:
   - If `len(current) == 2 * n`, join `current` into a string, append to `result`, and return.
   - If `open_count < n`: append `'('`, recurse with `open_count + 1`, then pop.
   - If `close_count < open_count`: append `')'`, recurse with `close_count + 1`, then pop.
3. Call `backtrack(0, 0)`.
4. Return `result`.

## Line-by-Line Explanation
- `result = []` – stores the final valid combinations.
- `current = []` – mutable list representing the current prefix; using a list avoids string concatenation overhead.
- `def backtrack(open_count, close_count):` – recursive helper; parameters track how many opening and closing parentheses have been placed.
- `if len(current) == 2 * n:` – base case: a complete string of length `2n` is formed.
- `result.append("".join(current))` – convert the list of characters to a string and save it.
- `return` – stop further recursion from this leaf.
- `if open_count < n:` – we can still add an opening parenthesis.
- `current.append("(")` – choose `'('`.
- `backtrack(open_count + 1, close_count)` – explore deeper with one more open.
- `current.pop()` – undo the choice (backtrack).
- `if close_count < open_count:` – we can add a closing parenthesis only if there are unmatched opens.
- `current.append(")")` – choose `')'`.
- `backtrack(open_count, close_count + 1)` – explore deeper with one more close.
- `current.pop()` – undo the choice.
- `backtrack(0, 0)` – start the recursion with zero parentheses placed.
- `return result` – return all generated combinations.

## Dry Run
Trace for `n = 3` (first example). The recursion is depth‑first; the table shows the sequence of calls that lead to the first result `"((()))"` and the subsequent backtracking steps that produce the remaining results. Only the `current` string, `open_count`, `close_count`, and the action are shown.

| Step | Call | open_count | close_count | current | Action |
|------|------|------------|-------------|---------|--------|
| 1 | backtrack(0,0) | 0 | 0 | [] | enter |
| 2 | backtrack(1,0) | 1 | 0 | ['('] | add '(' |
| 3 | backtrack(2,0) | 2 | 0 | ['(', '('] | add '(' |
| 4 | backtrack(3,0) | 3 | 0 | ['(', '(', '('] | add '(' |
| 5 | backtrack(3,1) | 3 | 1 | ['(', '(', '(', ')'] | add ')' (close<open) |
| 6 | backtrack(3,2) | 3 | 2 | ['(', '(', '(', ')', ')'] | add ')' |
| 7 | backtrack(3,3) | 3 | 3 | ['(', '(', '(', ')', ')', ')'] | add ')' → len=6 → save `"((()))"` |
| 8 | return to step 6 | 3 | 2 | ['(', '(', '(', ')', ')'] | pop last ')' |
| 9 | return to step 5 | 3 | 1 | ['(', '(', '(', ')'] | pop last ')' |
| 10 | return to step 4 | 3 | 0 | ['(', '(', '('] | pop last '(' (no more opens) |
| 11 | backtrack(2,1) | 2 | 1 | ['(', '(', ')'] | from step 3: add ')' (close<open) |
| 12 | backtrack(3,1) | 3 | 1 | ['(', '(', ')', '('] | add '(' |
| 13 | backtrack(3,2) | 3 | 2 | ['(', '(', ')', '(', ')'] | add ')' |
| 14 | backtrack(3,3) | 3 | 3 | ['(', '(', ')', '(', ')', ')'] | save `"(()())"` |
| … | … | … | … | … | continues similarly for `"(())()"`, `"()(())"`, `"()()()"` |

The full recursion tree yields the five expected strings in the order shown.

## Complexity
- **Time:** O(C_n * n), where C_n is the nth Catalan number (number of valid combinations). Each valid string of length `2n` is built once, and each recursive step does O(1) work (append/pop). The total work is proportional to the total length of all output strings.
- **Space:** O(n) for the recursion stack (maximum depth `2n`) and the `current` list (max length `2n`). Output space is not counted in auxiliary space.

## Edge Cases
- **n = 1:** Returns `["()"]` – the only valid pair.
- **n = 8 (maximum):** Produces 1430 strings; recursion depth 16, well within Python limits.
- **Duplicates:** The constraints `open_count < n` and `close_count < open_count` guarantee each combination is generated exactly once.
- **Empty input:** Not possible per constraints (`n ≥ 1`). If `n = 0` were allowed, the code would return `[""]` (since `len(current) == 0` immediately), which is correct for zero pairs.

## Possible Improvements
The solution is already optimal for the given constraints. Backtracking with pruning is the standard approach; it achieves the optimal time complexity (output‑sensitive) and uses minimal auxiliary space. Variable names (`open_count`, `close_count`, `current`, `result`) are clear and idiomatic. No redundant passes or data structures exist. An iterative or DP approach would not improve asymptotic complexity and would complicate the code.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
