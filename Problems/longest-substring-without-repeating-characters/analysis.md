# 3. Longest Substring Without Repeating Characters - Solution Analysis

## Problem Understanding
Given a string `s` of length up to 10^5 containing ASCII characters, find the length of the longest contiguous substring with all unique characters. The substring must be contiguous (not a subsequence). Empty string returns 0. The constraint on length rules out O(n^2) substring enumeration; an O(n) single-pass solution is required.

## Approach
The solution uses the **sliding window** pattern with a hash map tracking the most recent index of each character. The window `[l, r]` always contains unique characters. When the right pointer encounters a character already inside the window, the left pointer jumps to one position after that character's previous occurrence, preserving uniqueness. This avoids the O(n^2) brute force of checking all substrings by ensuring each character is processed at most twice (once entering, once leaving the window). The key insight: storing the *latest* index of each character lets us skip the left pointer forward in O(1) time instead of incrementing it one by one.

## Algorithm
1. Initialize left pointer `l = 0`, answer `ans = 0`, and empty dictionary `store` mapping character → latest index.
2. Iterate right pointer `r` and character `ch` over the string with `enumerate`.
3. If `ch` exists in `store` and its stored index is ≥ `l` (i.e., the duplicate lies inside the current window), move `l` to `store[ch] + 1` to exclude the previous occurrence.
4. Update `store[ch] = r` to record the current position.
5. Update `ans = max(ans, r - l + 1)` with the current window length.
6. After the loop, return `ans`.

## Line-by-Line Explanation
- `l = 0`: Left boundary of the sliding window, starts at the first character.
- `ans = 0`: Tracks the maximum window length seen so far.
- `store = {}`: Dictionary mapping each character to its most recent index in the string.
- `for r, ch in enumerate(s):`: Right pointer `r` expands the window one character at a time.
- `if store.get(ch, -1) >= l:`: Checks whether `ch` has appeared inside the current window (index ≥ `l`). `get` with default `-1` handles unseen characters.
- `l = store[ch] + 1`: Jumps left pointer past the previous occurrence of `ch`, restoring uniqueness.
- `store[ch] = r`: Records the current index of `ch` for future duplicate checks.
- `ans = max(ans, r - l + 1)`: Updates the maximum length using the current window size.
- `return ans`: Returns the length of the longest valid substring found.

## Dry Run
Trace of Example 1: `s = "abcabcbb"`

| Step | r | ch | l | store (before) | store.get(ch, -1) | Condition | l (after) | store (after) | ans (after) | Action |
|------|---|-----|---|----------------|-------------------|-----------|-----------|---------------|-------------|--------|
| 1 | 0 | 'a' | 0 | {} | -1 | False | 0 | {'a': 0} | 1 | store 'a'→0, ans=1 |
| 2 | 1 | 'b' | 0 | {'a':0} | -1 | False | 0 | {'a':0, 'b':1} | 2 | store 'b'→1, ans=2 |
| 3 | 2 | 'c' | 0 | {'a':0, 'b':1} | -1 | False | 0 | {'a':0, 'b':1, 'c':2} | 3 | store 'c'→2, ans=3 |
| 4 | 3 | 'a' | 0 | {'a':0, 'b':1, 'c':2} | 0 | True (0≥0) | 1 | {'a':3, 'b':1, 'c':2} | 3 | move l to 1, store 'a'→3, ans=max(3,3)=3 |
| 5 | 4 | 'b' | 1 | {'a':3, 'b':1, 'c':2} | 1 | True (1≥1) | 2 | {'a':3, 'b':4, 'c':2} | 3 | move l to 2, store 'b'→4, ans=max(3,3)=3 |
| 6 | 5 | 'c' | 2 | {'a':3, 'b':4, 'c':2} | 2 | True (2≥2) | 3 | {'a':3, 'b':4, 'c':5} | 3 | move l to 3, store 'c'→5, ans=max(3,3)=3 |
| 7 | 6 | 'b' | 3 | {'a':3, 'b':4, 'c':5} | 4 | True (4≥3) | 5 | {'a':3, 'b':6, 'c':5} | 3 | move l to 5, store 'b'→6, ans=max(3,2)=3 |
| 8 | 7 | 'b' | 5 | {'a':3, 'b':6, 'c':5} | 6 | True (6≥5) | 7 | {'a':3, 'b':7, 'c':5} | 3 | move l to 7, store 'b'→7, ans=max(3,1)=3 |

Final `ans = 3`.

## Complexity
- **Time:** O(n), where n = len(s). The loop visits each character once; dictionary `get` and assignment are O(1) average.
- **Space:** O(min(n, Σ)), where Σ is the character set size. The dictionary holds at most one entry per distinct character in the current window. Since the input consists of English letters, digits, symbols and spaces (bounded ASCII subset), Σ ≤ 128, so space is effectively O(1) with a small constant.

## Edge Cases
- **Empty string** (`s = ""`): loop body never executes, returns initial `ans = 0`. Valid per constraints (0 ≤ s.length).
- **Single character** (`s = "a"`): one iteration, `ans = 1`.
- **All identical characters** (`s = "bbbbb"`): `l` jumps to `r` each step, window size stays 1, returns 1.
- **All unique characters** (`s = "abcdef"`): condition never true, `l` stays 0, `ans` grows to n.
- **Maximum length** (n = 10⁵): O(n) time and O(1) space easily fit limits.
- **Characters outside ASCII letters** (spaces, symbols): dictionary keys are raw characters, so handled uniformly.

## Possible Improvements
The solution is already optimal for the given constraints. Time complexity O(n) is the theoretical lower bound (must inspect each character). Space complexity O(min(n, Σ)) is optimal for a sliding-window approach. Variable names (`l`, `r`, `ans`, `store`) are concise and idiomatic for this pattern; renaming to `left`/`right` would add clarity but is not necessary. The use of `store.get(ch, -1) >= l` to detect a duplicate inside the current window is clean and avoids a separate `in` check. No material improvement exists without changing the algorithmic paradigm.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
