# 1520. Maximum Number of Non-Overlapping Substrings - Solution Analysis

## Problem Understanding
Given a string `s` of lowercase letters, we must select a set of non-overlapping substrings such that:
1. No two substrings overlap.
2. If a substring contains a character `c`, it must contain **all** occurrences of `c` in `s`.

We need to maximize the number of substrings. If multiple solutions have the same maximum count, we must choose the one with the smallest total length (it is guaranteed unique). The string length is up to 10⁵, so an O(n) or O(n log n) solution is required.

## Approach
The solution uses **greedy interval scheduling** after constructing all *minimal valid substrings*.

**Key insight:** Any valid substring must start at the first occurrence of some character. For each character `c`, we can try to build the minimal valid substring that starts at `first[c]` by expanding its right boundary to include the last occurrence of every character encountered. If during this expansion we meet a character whose first occurrence lies *before* the current left boundary, the interval cannot be a minimal valid substring (it would force the left boundary leftward, contradicting the start at `first[c]`). The intervals that survive this check are exactly the minimal valid substrings. These intervals are either nested or disjoint. To maximize the count (and minimize total length), we sort them by ending index and greedily pick non-overlapping ones – the classic interval scheduling algorithm.

**Brute force** would enumerate all O(n²) substrings, check the condition, and then search for a maximum non-overlapping subset – far too slow.

## Algorithm
1. **Record first/last positions** – Create arrays `first[26]` (initialized to `len(s)`) and `last[26]` (initialized to `-1`). Scan `s` once to fill them.
2. **Build candidate intervals** – For each character `c` that appears:
   - Set `l = first[c]`, `r = last[c]`.
   - Scan `i` from `l` to `r`:
     - Let `x = s[i]`. If `first[x] < l`, the interval is invalid → `break`.
     - Otherwise, extend `r = max(r, last[x])`.
   - If the scan finishes without `break`, the interval `[l, r]` is a minimal valid substring. Store it as `(r, l)`.
3. **Sort intervals** by their right endpoint `r` (ascending).
4. **Greedy selection** – Iterate the sorted intervals, maintaining `end = -1` (the rightmost index of the last chosen substring). If `l > end`, select `s[l:r+1]` and update `end = r`.
5. Return the list of selected substrings.

## Line-by-Line Explanation
```python
first = [len(s)] * 26
last = [-1] * 26
```
Initialize arrays for first and last occurrence of each letter.

```python
for i, c in enumerate(s):
    x = ord(c) - 97
    first[x] = min(first[x], i)
    last[x] = i
```
Single pass to populate `first` and `last`.

```python
a = []
for c in range(26):
    l, r = first[c], last[c]
    if r < 0:
        continue
```
`a` will hold valid intervals as `(right, left)`. Skip characters that never appear.

```python
    i = l
    while i <= r:
        x = ord(s[i]) - 97
        if first[x] < l:
            break
        r = max(r, last[x])
        i += 1
    else:
        a.append((r, l))
```
Expand the interval starting at `l`. If any character inside has its first occurrence before `l`, the interval is invalid (`break`). Otherwise, keep extending `r` to the furthest last occurrence seen. The `else` clause (executed only if the loop wasn't broken) adds the valid interval.

```python
a.sort()
ans, end = [], -1
```
Sort by right endpoint (tuple sort uses first element `r`). `end` tracks the last index of the previously chosen substring.

```python
for r, l in a:
    if l > end:
        ans.append(s[l:r + 1])
        end = r
```
Classic greedy interval scheduling: pick the interval with the earliest end that starts after the previous end.

```python
return ans
```

## Dry Run
Example: `s = "adefaddaccc"` (indices 0‑10)

| char | first | last |
|------|-------|------|
| a    | 0     | 7    |
| d    | 1     | 6    |
| e    | 2     | 2    |
| f    | 3     | 3    |
| c    | 8     | 10   |

**Building intervals:**
- `a`: l=0, r=7. Scan 0..7: all chars have first ≥ 0, r stays 7 → add (7,0).
- `d`: l=1, r=6. Scan 1..6: at i=4 (a) first[a]=0 < 1 → break, invalid.
- `e`: l=2, r=2. Scan 2..2: ok → add (2,2).
- `f`: l=3, r=3. Scan 3..3: ok → add (3,3).
- `c`: l=8, r=10. Scan 8..10: ok → add (10,8).

`a = [(7,0), (2,2), (3,3), (10,8)]` → after sort: `[(2,2), (3,3), (7,0), (10,8)]`.

**Greedy selection:**
| Step | (r, l) | l > end? | Action          | end |
|------|--------|----------|-----------------|-----|
| 1    | (2,2)  | 2 > -1   | take "e"        | 2   |
| 2    | (3,3)  | 3 > 2    | take "f"        | 3   |
| 3    | (7,0)  | 0 > 3? no| skip            | 3   |
| 4    | (10,8) | 8 > 3    | take "ccc"      | 10  |

Result: `["e","f","ccc"]`.

## Complexity
- **Time:** O(n). The first scan is O(n). The interval expansion runs at most 26 times, each scanning a segment of `s`; because each character’s interval is processed once and the total scanned indices across all 26 letters is bounded by 26·n = O(n). Sorting ≤26 intervals is O(1). Greedy pass is O(1).
- **Space:** O(1) extra (fixed-size arrays of length 26, list of ≤26 intervals, output list).

## Edge Cases
- **Single character / all same character:** e.g., `"aaaa"` → only one valid interval covering the whole string, correctly returned.
- **Characters appearing once:** Each forms a length‑1 valid interval; greedy picks all of them (they are disjoint).
- **Nested intervals:** The algorithm generates the outermost interval for a character (e.g., `"adefadda"` for `a`) but the greedy pass prefers the shorter inner intervals (`"e"`, `"f"`) because they end earlier, yielding a higher count and smaller total length.
- **No valid answer?** Impossible – every character that appears at least once yields at least its own minimal interval (if it appears once) or a larger one; the greedy pass always selects a non‑empty set.

## Possible Improvements
The solution is already optimal in both time (O(n)) and space (O(1)) for the given constraints. Variable names are concise but clear (`first`, `last`, `a` for intervals, `end` for the greedy boundary). No material improvement is needed.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
