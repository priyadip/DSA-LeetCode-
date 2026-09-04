# 5. Longest Palindromic Substring - Solution Analysis

## Problem Understanding
Given a string `s` of length 1 to 1000 containing only alphanumeric characters, return the longest contiguous substring that reads the same forwards and backwards. If multiple substrings share the maximum length, any one is acceptable. The constraints rule out exponential algorithms; an O(n²) or better solution is expected.

## Approach
The solution uses **Manacher's algorithm**, a linear-time algorithm for finding the longest palindromic substring. The brute-force approach checks all O(n²) substrings with O(n) palindrome verification each, yielding O(n³). Dynamic programming reduces verification to O(1) with an O(n²) table, still quadratic. Manacher's algorithm achieves O(n) by exploiting the symmetry of palindromes: when a palindrome centered at `center` extends to `right`, positions inside it have mirrors whose palindrome radii are already known, allowing us to skip redundant character comparisons. The key insight is that the radius at position `i` is at least the minimum of its mirror's radius and the distance to the current right boundary.

## Algorithm
1. Transform `s` into `t` by inserting `#` between every character and adding sentinels `^` at start and `$` at end. This makes every palindrome in `t` odd-length and eliminates bounds checks during expansion.
2. Initialize array `p` of length `n = len(t)` to store the radius (half-length) of the longest palindrome centered at each index.
3. Initialize `center = 0`, `right = 0` to track the rightmost palindrome found so far.
4. Initialize `max_len = 0`, `max_center = 0` to track the overall longest palindrome.
5. For each index `i` from 1 to `n-2` (skipping sentinels):
   a. Compute `mirror = 2 * center - i`, the reflection of `i` across `center`.
   b. If `i < right`, set `p[i] = min(right - i, p[mirror])` — the known safe radius.
   c. Expand around `i` while `t[i + 1 + p[i]] == t[i - 1 - p[i]]`, incrementing `p[i]`.
   d. If `i + p[i] > right`, update `center = i` and `right = i + p[i]`.
   e. If `p[i] > max_len`, update `max_len = p[i]` and `max_center = i`.
6. Convert back to original string: `start = (max_center - max_len) // 2`.
7. Return `s[start:start + max_len]`.

## Line-by-Line Explanation
- `t = "^#" + "#".join(s) + "#$"`: Builds transformed string with separators and sentinels. Example: `"babad"` → `"^#b#a#b#a#d#$"`.
- `n = len(t)`: Length of transformed string.
- `p = [0] * n`: Radius array; `p[i]` will hold how many characters to left/right of `i` match.
- `center = 0; right = 0`: Current rightmost palindrome's center and exclusive right boundary.
- `max_len = 0; max_center = 0`: Best palindrome seen so far.
- `for i in range(1, n - 1):`: Iterate over all real positions in `t`, skipping `^` and `$`.
- `mirror = 2 * center - i`: Mirror index of `i` with respect to `center`.
- `if i < right: p[i] = min(right - i, p[mirror])`: If `i` lies inside the current rightmost palindrome, inherit a lower bound on its radius from its mirror, clamped so we don't exceed `right`.
- `while t[i + 1 + p[i]] == t[i - 1 - p[i]]: p[i] += 1`: Expand outward as long as characters match. Sentinels guarantee termination.
- `if i + p[i] > right: center = i; right = i + p[i]`: New palindrome extends further right; update the reference palindrome.
- `if p[i] > max_len: max_len = p[i]; max_center = i`: Track the globally longest radius and its center.
- `start = (max_center - max_len) // 2`: Map transformed center and radius back to original string start index. Division by 2 accounts for inserted `#` characters.
- `return s[start:start + max_len]`: Slice the longest palindromic substring from `s`.

## Dry Run
Trace on `s = "babad"` → `t = "^#b#a#b#a#d#$"` (indices 0..12).

| Step | i | t[i] | center | right | mirror | p[i] init | Expansion matches | p[i] final | max_len | max_center | Action |
|------|---|------|--------|-------|--------|-----------|-------------------|------------|---------|------------|--------|
| 1 | 1 | # | 0 | 0 | -1 | 0 | t[2]==t[0]? 'b' vs '^' no | 0 | 0 | 0 | no update |
| 2 | 2 | b | 0 | 0 | -2 | 0 | t[3]==t[1]? '#'=='#' yes; t[4]==t[0]? 'a' vs '^' no | 1 | 1 | 2 | center=2, right=3 |
| 3 | 3 | # | 2 | 3 | 1 | min(0,0)=0 | t[4]==t[2]? 'a' vs 'b' no | 0 | 1 | 2 | |
| 4 | 4 | a | 2 | 3 | 0 | 0 (i>=right) | t[5]==t[3]? '#'=='#' yes; t[6]==t[2]? 'b'=='b' yes; t[7]==t[1]? '#'=='#' yes; t[8]==t[0]? 'a' vs '^' no | 3 | 3 | 4 | center=4, right=7 |
| 5 | 5 | # | 4 | 7 | 3 | min(2,0)=0 | t[6]==t[4]? 'b' vs 'a' no | 0 | 3 | 4 | |
| 6 | 6 | b | 4 | 7 | 2 | min(1,1)=1 | t[8]==t[4]? 'a'=='a' yes; t[9]==t[3]? '#'=='#' yes; t[10]==t[2]? 'd' vs 'b' no | 3 | 3 | 4 | (tie, not >) |
| 7 | 7 | # | 4 | 7 | 1 | 0 (i>=right) | t[8]==t[6]? 'a' vs 'b' no | 0 | 3 | 4 | |
| 8 | 8 | a | 4 | 7 | 0 | 0 (i>=right) | t[9]==t[7]? '#'=='#' yes; t[10]==t[6]? 'd' vs 'b' no | 1 | 3 | 4 | |
| 9 | 9 | # | 4 | 7 | -1 | 0 (i>=right) | t[10]==t[8]? 'd' vs 'a' no | 0 | 3 | 4 | |
|10 |10 | d | 4 | 7 | -2 | 0 (i>=right) | t[11]==t[9]? '#'=='#' yes; t[12]==t[8]? '$' vs 'a' no | 1 | 3 | 4 | |
|11 |11 | # | 4 | 7 | -3 | 0 (i>=right) | t[12]==t[10]? '$' vs 'd' no | 0 | 3 | 4 | |

`max_center=4`, `max_len=3` → `start = (4-3)//2 = 0` → `s[0:3] = "bab"`. Correct.

## Complexity
- Time: O(n), where n = len(s). The loop runs O(n) times on the transformed string (length 2n+3). Each character comparison either increases `right` (which moves strictly forward at most 2n+3 steps) or terminates the while loop. Total comparisons are bounded by O(n).
- Space: O(n) for the transformed string `t` and the radius array `p`, both length 2n+3.

## Edge Cases
- Single character: `s = "a"` → `t = "^#a#$"`, `p[2]=1`, `start=0`, returns `"a"`. Works.
- All same characters: `s = "aaaa"` → transformed string yields a palindrome spanning the whole string; algorithm correctly expands to full length.
- Even-length palindrome: `s = "cbbd"` → `t` centers at `#` between the two `b`s, radius covers both; returns `"bb"`.
- Multiple valid answers: `s = "babad"` returns `"bab"` (first found); `"aba"` would also be correct. The code picks the first maximum because it uses `>` not `>=`.
- Constraints guarantee `len(s) >= 1`, so empty input is not a concern.

## Possible Improvements
The solution is already optimal in asymptotic complexity (O(n) time, O(n) space) for the given constraints. A minor clarity improvement: rename `p` to `radius` or `pal_radii` to make the array's purpose self-documenting. The sentinel characters `^` and `$` are clever but non-obvious; a comment explaining they prevent bounds checks during expansion would help future readers. No algorithmic improvement is needed.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
