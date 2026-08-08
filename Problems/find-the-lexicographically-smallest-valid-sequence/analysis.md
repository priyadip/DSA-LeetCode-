# 3302. Find the Lexicographically Smallest Valid Sequence - Solution Analysis

## Problem Understanding
We are given two strings `word1` (length `n`) and `word2` (length `m`, with `m < n`). We must select `m` indices from `word1` in strictly increasing order such that the characters at those indices form a string that differs from `word2` in **at most one position** (i.e., the strings are *almost equal*). Among all valid index sequences, we need the **lexicographically smallest** one (compare index arrays element by element). If no valid sequence exists, return an empty array. The constraints (`n ≤ 3·10⁵`) demand an O(n) or O(n log n) solution.

## Approach
The solution uses a **greedy algorithm with a suffix feasibility precomputation** (dynamic programming / two pointers).  
A brute-force approach would try all subsequences of length `m`, which is exponential.  
The key insight is: to obtain the lexicographically smallest sequence, we should pick the earliest possible index for each character of `word2`, but we have one allowed mismatch. We can decide to “spend” that mismatch at the earliest position where doing so still allows the rest of `word2` to be matched from the remaining part of `word1`.  

The suffix array `suf[i]` (defined as the smallest index `k` such that `word2[k:]` is a subsequence of `word1[i:]`) lets us check in O(1) whether the remainder of `word2` can be completed after a potential change at position `i`.  
- If `word1[i]` matches the current needed character `word2[j]`, we always take it (greedy for smallest index).  
- If it doesn’t match and we haven’t used our change yet, we check whether `word2[j+1:]` can be matched from `i+1` (i.e., `suf[i+1] ≤ j+1`). If yes, we use the change here, take index `i`, and move to the next character in `word2`.  
This greedy choice is safe because any valid sequence must match `word2[j]` at or after `i`; taking `i` (either by exact match or by using the single change) yields the smallest possible index for this position.

## Algorithm
1. Let `n = len(word1)`, `m = len(word2)`.
2. Create array `suf` of length `n+1`, initialized with `m`.
3. Set `j = m-1`. Iterate `i` from `n-1` down to `0`:
   - If `j ≥ 0` and `word1[i] == word2[j]`, decrement `j`.
   - Set `suf[i] = j + 1`.  
   (After this, `suf[i]` is the smallest index `k` such that `word2[k:]` is a subsequence of `word1[i:]`. `suf[n] = m`.)
4. Initialize `ans = []`, `j = 0`, `changed = False`.
5. Iterate `i` from `0` to `n-1`:
   - If `j == m`, break.
   - If `word1[i] == word2[j]`:
        - Append `i` to `ans`, increment `j`.
   - Else if `not changed` and `suf[i+1] ≤ j+1`:
        - Set `changed = True`, append `i` to `ans`, increment `j`.
6. Return `ans` if `j == m`, otherwise `[]`.

## Line-by-Line Explanation
```python
n = len(word1)
m = len(word2)
```
Store lengths for frequent access.

```python
suf = [m] * (n + 1)
```
Suffix feasibility array; `suf[i]` will hold the smallest index in `word2` whose suffix can be matched from `word1[i:]`. Initialized to `m` (empty suffix).

```python
j = m - 1
for i in range(n - 1, -1, -1):
    if j >= 0 and word1[i] == word2[j]:
        j -= 1
    suf[i] = j + 1
```
Backward pass: `j` tracks the next character of `word2` to match from the end. When a match is found, we move `j` left. `suf[i] = j+1` means characters `word2[j+1:]` are matched from `i` onward, so the earliest start index for a matchable suffix is `j+1`.

```python
ans = []
j = 0
changed = False
```
Forward pass: `ans` collects chosen indices, `j` now points to the next character of `word2` to match from the start, `changed` flags whether the single allowed mismatch has been used.

```python
for i in range(n):
    if j == m:
        break
```
Scan `word1` left to right; stop once all `m` characters are matched.

```python
    if word1[i] == word2[j]:
        ans.append(i)
        j += 1
```
Exact match – greedily take the earliest possible index for `word2[j]`.

```python
    elif not changed and suf[i + 1] <= j + 1:
        changed = True
        ans.append(i)
        j += 1
```
Mismatch but we can spend our one change here **iff** the rest of `word2` (starting at `j+1`) can be matched from `i+1`. `suf[i+1] ≤ j+1` exactly expresses this feasibility.

```python
return ans if j == m else []
```
If we matched all `m` characters, `ans` is the lexicographically smallest valid sequence; otherwise no valid sequence exists.

## Dry Run
Example 1: `word1 = "vbcca"`, `word2 = "abc"` (`n=5`, `m=3`).

**Backward pass (building `suf`):**
| i | word1[i] | j (before) | match? | j (after) | suf[i] = j+1 |
|---|----------|------------|--------|-----------|--------------|
| 4 | 'a'      | 2          | no     | 2         | 3            |
| 3 | 'c'      | 2          | yes    | 1         | 2            |
| 2 | 'c'      | 1          | no     | 1         | 2            |
| 1 | 'b'      | 1          | yes    | 0         | 1            |
| 0 | 'v'      | 0          | no     | 0         | 1            |
`suf = [1, 1, 2, 2, 3, 3]` (index 5 is the extra `m`).

**Forward pass:**
| i | word1[i] | j | word2[j] | changed | condition `suf[i+1] ≤ j+1` | Action |
|---|----------|---|----------|---------|----------------------------|--------|
| 0 | 'v'      | 0 | 'a'      | False   | `suf[1]=1 ≤ 1` true        | use change, ans=[0], j=1, changed=True |
| 1 | 'b'      | 1 | 'b'      | True    | –                          | exact match, ans=[0,1], j=2 |
| 2 | 'c'      | 2 | 'c'      | True    | –                          | exact match, ans=[0,1,2], j=3 |
| 3 | –        | 3 | –        | –       | –                          | `j==m` break |

Result: `[0,1,2]` ✓

## Complexity
- **Time:** O(n) – one backward pass and one forward pass over `word1`, each O(n). `m < n` so O(n) dominates.
- **Space:** O(n) – the `suf` array of size `n+1`.

## Edge Cases
- **`word2` length 1:** The algorithm correctly picks the first matching character or uses the change on the first character if no match exists (since `suf[i+1] ≤ 1` is always true for the last character).
- **No valid sequence:** The forward pass fails to reach `j == m`, returns `[]` (e.g., Example 3).
- **Multiple valid sequences:** Greedy choice of earliest index for each `word2` character, constrained by the single change, guarantees lexicographically smallest array.
- **Change used on last character:** Condition `suf[n] = m ≤ m` holds, so change can be spent on the final character if needed.
- **Maximum input size (3·10⁵):** O(n) time and space fit comfortably.

## Possible Improvements
The solution is already **optimal** for the given constraints: O(n) time and O(n) space are the best achievable (any algorithm must read the input). The code is concise, variable names are clear (`suf`, `ans`, `changed`), and there are no redundant passes or data structures. No further improvements are necessary.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
