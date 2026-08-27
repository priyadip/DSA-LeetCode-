# 3720. Lexicographically Smallest Permutation Greater Than Target - Solution Analysis

## Problem Understanding
Given two equal-length strings `s` and `target` (length ≤ 300, lowercase letters), we must return the lexicographically smallest permutation of `s` that is strictly greater than `target`. If no such permutation exists, return an empty string. Lexicographic order compares characters left to right; the first differing character decides. Duplicates in `s` are allowed and must be respected in the permutation.

## Approach
The solution uses a **greedy construction with backtracking** (often called "next permutation" on a multiset). It maintains a frequency count of characters in `s`. It first tries to match `target` from left to right as long as the required characters are available. When matching becomes impossible (either the needed character is exhausted or we deliberately choose a larger one), it attempts to place the smallest available character strictly greater than `target[i]` at that position, then fills the remaining positions with the smallest possible characters (sorted ascending). If no larger character exists at the current position, it backtracks to the most recent matched position, returns that character to the pool, and tries to increase there. This yields the minimal lexicographic permutation greater than `target` because we keep the prefix as small as possible and only increase at the rightmost feasible position.

## Algorithm
1. Count frequencies of each letter in `s` into array `cnt[26]`.
2. Initialize `i = 0`. While `i < n` and `cnt[target[i]] > 0`: consume `target[i]` (decrement count) and increment `i`. This builds the longest prefix identical to `target`.
3. If `i < n` (we stopped before the end):
   - Let `x = target[i]`. For each `y` from `x+1` to `'z'`: if `cnt[y] > 0`, consume `y`, build the suffix by concatenating all remaining letters in ascending order, and return `target[:i] + y + suffix`.
4. If no larger character at position `i`, backtrack:
   - For `j` from `i-1` down to `0`:
     - Return `target[j]` to `cnt` (increment its count).
     - For each `y` from `target[j]+1` to `'z'`: if `cnt[y] > 0`, consume `y`, build the suffix from remaining counts, and return `target[:j] + y + suffix`.
5. If the loop finishes without returning, no valid permutation exists; return `""`.

## Line-by-Line Explanation
- `cnt = [0] * 26`: frequency array for 'a'..'z'.
- `for c in s: cnt[ord(c) - 97] += 1`: populate counts from `s`.
- `n = len(s)`: store length.
- `i = 0`: start index for prefix matching.
- `while i < n:`: attempt to match `target` greedily.
  - `x = ord(target[i]) - 97`: index of current target character.
  - `if cnt[x] == 0: break`: cannot match further; stop.
  - `cnt[x] -= 1`: use this character for the prefix.
  - `i += 1`: advance.
- `if i < n:`: we stopped early, so position `i` is the first where we can try to exceed `target`.
  - `x = ord(target[i]) - 97`: target character at the mismatch.
  - `for y in range(x + 1, 26):`: search for smallest available character > `target[i]`.
    - `if cnt[y]:`: found a candidate.
    - `cnt[y] -= 1`: reserve it.
    - `suffix = ''.join(chr(k + 97) * cnt[k] for k in range(26))`: build minimal suffix from remaining letters.
    - `return target[:i] + chr(y + 97) + suffix`: construct answer: matched prefix + chosen larger char + minimal suffix.
- `for j in range(i - 1, -1, -1):`: backtrack over matched positions.
  - `x = ord(target[j]) - 97`: character at backtrack position.
  - `cnt[x] += 1`: return it to the pool (we will replace it).
  - `for y in range(x + 1, 26):`: try to place a larger character here.
    - `if cnt[y]:`: found.
    - `cnt[y] -= 1`: reserve.
    - `suffix = ''.join(chr(k + 97) * cnt[k] for k in range(26))`: minimal suffix from updated counts.
    - `return target[:j] + chr(y + 97) + suffix`: answer with increased character at `j`.
- `return ""`: no valid permutation found.

## Dry Run
Trace of Example 1: `s = "abc"`, `target = "bba"`.

Initial `cnt = [1,1,1]` (a,b,c).

**While loop – match target as far as possible:**

| Step | i | target[i] | x | cnt[x] before | cnt after | Action |
|------|---|-----------|---|---------------|-----------|--------|
| 1 | 0 | 'b' | 1 | 1 | 0 | match, i=1 |
| 2 | 1 | 'b' | 1 | 0 | – | break (cnt[x]==0) |

After loop: `i = 1`, `cnt = [1,0,1]` (a:1, c:1).

**First if block (i < n):**  
`x = 1` (target[1] = 'b'). Loop `y` from 2 to 25:  
- `y = 2` ('c'), `cnt[2] = 1` → use it. `cnt[2]` becomes 0.  
Build suffix from remaining `cnt`: `cnt[0]=1` → `'a'`, others 0 → suffix = `"a"`.  
Return `target[:1] + 'c' + "a"` = `"bca"`.

## Complexity
- **Time:** O(n), where n = len(s) = len(target) ≤ 300.  
  Counting frequencies: O(n).  
  While loop: at most n iterations.  
  First y-loop: at most 26 iterations.  
  Backtrack loop: at most n iterations, each with an inner loop of at most 26 iterations.  
  All operations inside loops are O(1). Since 26 is a constant, total time is O(n).
- **Space:** O(n) for the output string. The frequency array uses O(26) = O(1) extra space.

## Edge Cases
- **Exact match (i == n):** The while loop consumes all characters matching target exactly. The first if block is skipped; the backtrack loop tries to increase an earlier position. If target is already the largest permutation, returns `""`.
- **No match at first character (i == 0):** While loop breaks immediately. Algorithm places the smallest available character > target[0] at position 0, then appends the remaining characters in sorted order.
- **All characters identical:** e.g., `s = "aaa"`, `target = "aaa"`. While loop matches all, backtrack finds no larger character, returns `""`.
- **Duplicates in s:** Handled correctly by frequency counts.
- **Multiple valid answers:** Greedy choice of the smallest possible increase at the rightmost feasible position guarantees the lexicographically smallest result.
- **Maximum input size (n = 300):** O(n) time and space easily fit within limits.

## Possible Improvements
The solution is already optimal for the given constraints. Time complexity is O(n) with a small constant (26), and space is O(n) for the output. The code is concise and clear. A minor readability improvement would be to extract the suffix construction into a helper function to avoid duplication, but this does not affect correctness or asymptotic performance. No algorithmic improvement is needed.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
