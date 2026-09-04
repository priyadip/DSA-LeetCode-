# 647. Palindromic Substrings - Solution Analysis

## Problem Understanding
Given a string `s` of length up to 1000, count all contiguous substrings that read the same forward and backward. Substrings at different positions are counted separately even if they have identical content. The constraints allow O(n²) solutions, but the optimal solution achieves O(n) time.

## Approach
The solution uses **Manacher's algorithm**, a linear-time algorithm for finding all palindromic substrings. The brute-force approach checks all O(n²) substrings with O(n) verification each, yielding O(n³). Dynamic programming reduces verification to O(1) but still requires O(n²) time and space. Manacher's algorithm exploits symmetry: when a palindrome centered at `center` extends to `right`, any position `i` inside that range has a mirror `mirror = 2*center - i` whose palindrome radius provides a lower bound for `i`'s radius, avoiding redundant character comparisons. The key insight is that the rightmost palindrome's boundary lets us initialize radii for new centers in O(1) amortized time.

## Algorithm
1. Transform `s` by inserting `#` between characters and adding sentinels `^` and `$` to handle even/odd lengths uniformly and avoid bounds checks.
2. Create array `p` where `p[i]` will hold the radius of the longest palindrome centered at `i` in the transformed string.
3. Initialize `center = 0`, `right = 0` (boundary of the rightmost known palindrome), and `count = 0`.
4. For each position `i` from 1 to `n-2` (excluding sentinels):
   - Compute `mirror = 2*center - i`.
   - If `i < right`, set `p[i] = min(right - i, p[mirror])` to use the mirrored palindrome's radius, clamped by the current boundary.
   - Expand around `i` by comparing characters at `i + 1 + p[i]` and `i - 1 - p[i]`, incrementing `p[i]` while they match.
   - If the expanded palindrome extends past `right`, update `center = i` and `right = i + p[i]`.
   - Add `(p[i] + 1) // 2` to `count`; this converts the transformed-string radius to the number of original palindromic substrings centered at this position.
5. Return `count`.

## Line-by-Line Explanation
- `t = "^#" + "#".join(s) + "#$"`: Builds the transformed string with sentinels and separators; e.g., `"aba"` becomes `"^#a#b#a#$"`.
- `n = len(t)`: Length of transformed string.
- `p = [0] * n`: Array to store palindrome radii for each center in `t`.
- `center = 0; right = 0; count = 0`: Track the rightmost palindrome's center and right boundary, and the total count.
- `for i in range(1, n - 1):`: Iterate over all possible centers in `t`, skipping sentinels.
- `mirror = 2 * center - i`: Index of `i`'s mirror across `center`.
- `if i < right: p[i] = min(right - i, p[mirror])`: If `i` lies within the current rightmost palindrome, initialize its radius using the mirror's radius, limited by the distance to `right`.
- `while t[i + 1 + p[i]] == t[i - 1 - p[i]]: p[i] += 1`: Expand outward from the initialized radius while characters match.
- `if i + p[i] > right: center = i; right = i + p[i]`: If the new palindrome extends further right, update the rightmost boundary.
- `count += (p[i] + 1) // 2`: Each radius `p[i]` in the transformed string corresponds to `(p[i] + 1) // 2` palindromic substrings in the original string (odd and even lengths combined).
- `return count`: Total number of palindromic substrings.

## Dry Run
Trace for `s = "abc"` (Example 1). Transformed string `t = "^#a#b#c#$"` (indices 0..8).

| Step | i | mirror | i<right | p[i] (final) | center | right | count added | total | Action |
|------|---|--------|---------|--------------|--------|-------|-------------|-------|--------|
| 1 | 1 | -1 | False | 0 | 1 | 1 | 0 | 0 | No expansion (`a` != `^`) |
| 2 | 2 | 0 | False | 1 | 2 | 3 | 1 | 1 | Expand once (`#`==`#`), then `b`!=`^` |
| 3 | 3 | 1 | False | 0 | 2 | 3 | 0 | 1 | No expansion (`b`!=`a`) |
| 4 | 4 | 0 | False | 1 | 4 | 5 | 1 | 2 | Expand once (`#`==`#`), then `c`!=`a` |
| 5 | 5 | 3 | False | 0 | 4 | 5 | 0 | 2 | No expansion (`c`!=`b`) |
| 6 | 6 | 2 | False | 1 | 6 | 7 | 1 | 3 | Expand once (`#`==`#`), then `$`!=`b` |
| 7 | 7 | 5 | False | 0 | 6 | 7 | 0 | 3 | No expansion (`$`!=`c`) |

Final count = 3, matching the expected output.

## Complexity
- **Time:** O(n), where n = len(s). The transformed string has length 2n+3. The outer loop runs O(n) times. The inner `while` loop expands the right boundary `right`, which only moves forward and never exceeds the string length, so total expansions across all iterations are O(n).
- **Space:** O(n) for the transformed string `t` and the radius array `p`, both of length 2n+3.

## Edge Cases
- **Single character** (e.g., `"a"`): transformed to `"^#a#$"`, loop runs once, `p[2]=1`, count = (1+1)//2 = 1. Correct.
- **All identical characters** (e.g., `"aaa"`): algorithm correctly counts all n(n+1)/2 palindromic substrings (6 for n=3).
- **Maximum length (1000)**: O(n) time and space easily fit within limits.
- **Already a palindrome** (e.g., `"aba"`): handles overlapping centers correctly via the `mirror` optimization.
- **No valid answer**: impossible because every single character is a palindrome; constraint guarantees n ≥ 1.

## Possible Improvements
The solution is already optimal for the given constraints. Manacher's algorithm achieves O(n) time, which is the best possible asymptotic complexity for counting all palindromic substrings. The expand-around-center approach (O(n²)) would also pass for n ≤ 1000 but is slower asymptotically. No material improvements are needed; variable names (`center`, `right`, `p`, `count`) are clear and idiomatic for this algorithm.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
