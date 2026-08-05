# 3. Longest Substring Without Repeating Characters - Solution Analysis

## Problem Understanding
The task is to find the length of the longest contiguous substring within a given string `s` such that no character appears more than once in that substring.

Constraints that shape the design:
* `0 <= s.length <= 10^5`: An $O(N^2)$ brute-force check of all substrings will result in a Time Limit Exceeded (TLE). An $O(N)$ algorithm is required.
* `s` contains English letters, digits, symbols, and spaces: The set of possible characters is bounded by the character encoding set (e.g., standard ASCII or extended ASCII), meaning the maximum number of unique characters in memory is small and constant.

## Approach
This solution uses the **Sliding Window** pattern optimized with a **Hash Map** (index mapping).

Instead of maintaining a set of characters and shrinking the left boundary `l` one step at a time via a `while` loop when a duplicate is found, the hash map records the most recent 0-based index of each character. When a duplicate character is encountered inside the current window (i.e., `store[ch] >= l`), the left boundary `l` immediately jumps past the duplicate's previous index (`store[ch] + 1`). This keeps window expansion and contraction at $O(1)$ per character.

## Algorithm
1. Initialize the window's left pointer `l = 0`, the maximum length `res = 0`, and an empty dictionary `store`.
2. Iterate through the string `s` using index `r` and character `ch`.
3. Check if `ch` is present in `store` and its saved index is greater than or equal to `l` (confirming it resides inside the active window).
4. If true, set `l = store[ch] + 1` to skip past the last occurrence of `ch`.
5. Record or update `store[ch] = r`.
6. Calculate the current window length `r - l + 1` and update `res = max(res, r - l + 1)`.
7. After the loop terminates, return `res`.

## Line-by-Line Explanation
```python3
l = 0
res = 0
store = {}
```
Initializes the window's left boundary `l` at 0, the maximum valid substring length `res` at 0, and the lookup table `store` to track each character's last seen index.

```python3
for r, ch in enumerate(s):
```
Loops through string `s`, providing the current right boundary index `r` and the character `ch`.

```python3
    if ch in store and store[ch]>=l:
        l = store[ch]+1
```
Checks if `ch` was seen previously **and** if its recorded position lies within the active window `[l, r]`. The check `store[ch] >= l` is critical: without it, encountering a character whose previous instance was before `l` would incorrectly shift `l` backward. If the condition holds, `l` jumps to `store[ch] + 1`.

```python3
    store[ch] = r
```
Updates `store` so `ch` maps to its newest index `r`.

```python3
    res = max(res, r-l+1)
```
Calculates the current valid substring size (`r - l + 1`) and keeps the maximum length encountered so far.

```python3
return res
```
Returns the length of the longest duplicate-free substring.

## Dry Run
Tracing `s = "pwwkew"`:

| Step (`r`, `ch`) | `ch in store and store[ch] >= l` | `l` (before $\rightarrow$ after) | `store` state after step | Window `s[l..r]` | `r - l + 1` | `res` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `0, 'p'` | False (`'p'` not in store) | $0 \rightarrow 0$ | `{'p': 0}` | `"p"` | $1$ | $1$ |
| `1, 'w'` | False (`'w'` not in store) | $0 \rightarrow 0$ | `{'p': 0, 'w': 1}` | `"pw"` | $2$ | $2$ |
| `2, 'w'` | True (`1 >= 0`) | $0 \rightarrow 2$ | `{'p': 0, 'w': 2}` | `"w"` | $1$ | $2$ |
| `3, 'k'` | False (`'k'` not in store) | $2 \rightarrow 2$ | `{'p': 0, 'w': 2, 'k': 3}` | `"wk"` | $2$ | $2$ |
| `4, 'e'` | False (`'e'` not in store) | $2 \rightarrow 2$ | `{'p': 0, 'w': 2, 'k': 3, 'e': 4}` | `"wke"` | $3$ | $3$ |
| `5, 'w'` | True (`2 >= 2`) | $2 \rightarrow 3$ | `{'p': 0, 'w': 5, 'k': 3, 'e': 4}` | `"kew"` | $3$ | $3$ |

Final returned result: `3`.

## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the length of string `s`. The string is traversed once using the `r` pointer. Each character lookup, insertion, and update operation in the Python `dict` takes average $O(1)$ time.
- **Space Complexity:** $O(\min(n, \Sigma))$, where $\Sigma$ is the size of the character set (charset). The hash map `store` will hold at most $\Sigma$ unique entries (e.g., 128 for standard ASCII).

## Edge Cases
- **Empty String (`s = ""`):** The `for` loop does not execute; `res = 0` is returned.
- **Single Character (`s = "a"`):** Loop runs once for `r = 0`; `res` becomes `max(0, 0 - 0 + 1) = 1`.
- **All Identical Characters (`s = "bbbbb"`):** On every index $r > 0$, `store[ch] >= l` evaluates to `True`, forcing `l = r`. The length stays $1$ throughout, returning `1`.
- **Out-of-Window Duplicates (e.g., `s = "abba"`):**
  - At `r = 0 ('a')`: `store['a'] = 0`, `l = 0`
  - At `r = 1 ('b')`: `store['b'] = 1`, `l = 0`
  - At `r = 2 ('b')`: `store['b'] = 2`, `l` jumps to $1 + 1 = 2$
  - At `r = 3 ('a')`: `store['a']` is `0`, but `store['a'] >= l` ($0 \ge 2$) evaluates to `False`. `l` correctly remains at $2$ rather than regressing back to $1$.

## Possible Improvements
The code is optimal in both time ($O(n)$) and space ($O(\min(n, \Sigma))$) complexities. 

A minor syntactical simplification is to use `dict.get()` with a default value of `-1` to combine the membership check and boundary condition:

```python3
if store.get(ch, -1) >= l:
    l = store[ch] + 1
```

This reduces dictionary lookups from two to one per iteration step when `ch` is in `store`, though the asymptotic complexity remains unchanged.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
