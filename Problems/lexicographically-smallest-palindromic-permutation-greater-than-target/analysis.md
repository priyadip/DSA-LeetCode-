# 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target - Solution Analysis

## Problem Understanding
We are given two strings `s` and `target` of equal length `n` (1 ≤ n ≤ 300) consisting of lowercase letters. We must return the lexicographically smallest string that is both a palindromic permutation of `s` and strictly greater than `target`. If no such permutation exists, return an empty string. The palindrome condition restricts the character counts: at most one character may have an odd frequency. The lexicographic order forces us to construct the answer by building the first half of the palindrome, because the second half is forced by mirroring.

## Approach
The solution uses a **greedy construction with a "next permutation" style search on the first half**.  
Brute force would enumerate all palindromic permutations (exponential), but a palindrome is uniquely determined by its first half (and a fixed middle character for odd `n`). The key insight: to be strictly greater than `target`, the first half must be lexicographically ≥ `target`'s first half; if equal, the middle character decides, otherwise any larger first half works. The algorithm first checks if the exact first half of `target` can be formed; if the resulting palindrome is > `target`, it is the answer. Otherwise, it scans from right to left to find the first position where the character can be increased, then fills the remainder with the smallest available characters.

## Algorithm
1. Count characters in `s`. If more than one character has an odd count, return `""` (no palindrome possible).
2. Compute `half_cnt = {c: cnt[c] // 2}`. Let `m = n // 2`, `t = target[:m]`. Determine `mid` as the character with odd count (or `""` if none).
3. Define helper `make(left) = left + mid + left[::-1]`.
4. Check if `t` can be formed from `half_cnt`: copy `half_cnt`, consume each char of `t`. If possible, form `ans = make(t)`. If `ans > target`, return `ans`.
5. For `i` from `m-1` down to `0`:
   - Take `prefix = t[:i]`. Copy `half_cnt` and consume `prefix`; if not possible, continue.
   - For each character `c` in sorted `rem` where `c > t[i]` and `rem[c] > 0`:
       - Decrement `rem[c]`, build `left = prefix + c + all remaining chars in sorted order`.
       - Return `make(left)`.
6. If no such `i` found, return `""`.

## Line-by-Line Explanation
- `n = len(s)`: length of the strings.
- `cnt = Counter(s)`: frequency of each character in `s`.
- `if sum(v % 2 for v in cnt.values()) > 1: return ""`: palindrome impossible if >1 odd count.
- `half_cnt = Counter({c: v // 2 for c, v in cnt.items()})`: counts for the first half.
- `m = n // 2`: length of the first half.
- `t = target[:m]`: target's first half.
- `mid = next((c for c in cnt if cnt[c] % 2), "")`: the middle character (empty if even length).
- `def make(left): return left + mid + left[::-1]`: builds full palindrome from first half.
- `rem = half_cnt.copy(); possible = True`: prepare to test if `t` can be the first half.
- `for c in t: ...`: try to consume `t` from `rem`; if any char missing, `possible = False`.
- `if possible: ans = make(t); if ans > target: return ans`: exact first half works and yields a valid answer.
- `for i in range(m - 1, -1, -1):`: scan positions from right to left to increase.
- `prefix = t[:i]; rem = half_cnt.copy()`: fresh copy for each attempt.
- `ok = True; for c in prefix: ...`: consume `prefix`; if impossible, skip this `i`.
- `if not ok: continue`: prefix cannot be formed.
- `for c in sorted(rem): if c > t[i] and rem[c] > 0:`: find smallest available char greater than `t[i]`.
- `rem[c] -= 1`: use that character.
- `left = prefix + c; left += "".join(x * rem[x] for x in sorted(rem))`: append remaining chars in sorted order to get smallest suffix.
- `return make(left)`: construct and return the palindrome.
- `return ""`: no valid permutation found.

## Dry Run
Example 1: `s = "baba"`, `target = "abba"`.
- `n=4`, `cnt={'b':2,'a':2}`, `half_cnt={'b':1,'a':1}`, `m=2`, `t="ab"`, `mid=""`.
- `make(left) = left + left[::-1]`.
- Check `t="ab"`: `rem` becomes `{'a':0,'b':0}`, `possible=True`. `ans="abba"`, not > `"abba"`.
- Loop `i=1`: `prefix="a"`, `rem={'a':0,'b':1}`. Need `c > 'b'` → none.
- Loop `i=0`: `prefix=""`, `rem={'a':1,'b':1}`. Sorted `rem`: `['a','b']`. `c='a'` not > `'a'`. `c='b'` > `'a'` and available. `rem['b']` becomes 0. `left = "b" + "a" = "ba"`. `make("ba") = "baab"`. Return `"baab"`.

| Step | i | prefix | rem before choice | t[i] | chosen c | left | make(left) |
|------|---|--------|-------------------|------|----------|------|------------|
| 1    | 1 | "a"    | a:0, b:1          | 'b'  | none     | -    | -          |
| 2    | 0 | ""     | a:1, b:1          | 'a'  | 'b'      | "ba" | "baab"     |

## Complexity
- **Time**: O(n · 26) = O(n). The outer loop runs at most `m ≤ n` times. Inside, we iterate over at most 26 characters (sorted keys of `rem`). All other operations are O(1) or O(n) for string building. With `n ≤ 300`, this is easily fast enough.
- **Space**: O(n) for the strings and O(26) for the counters.

## Edge Cases
- **No palindromic permutation** (e.g., `s="abc"`): caught by the odd-count check, returns `""`.
- **Target is the largest palindrome** (e.g., `s="baba"`, `target="bbaa"`): exact half fails, loop finds no valid increase, returns `""`.
- **Odd length with middle character** (e.g., `s="aac"`, `target="abb"`): `mid='c'`, exact half `"a"` yields `"aca"` > `"abb"`, returned immediately.
- **All characters identical** (e.g., `s="aaa"`, `target="aaa"`): exact half yields `"aaa"` not > target; loop finds no larger character, returns `""`.
- **Target's first half not formable** (e.g., `s="aabb"`, `target="cccc"`): `possible=False`, loop tries to build a larger half from available chars.

## Possible Improvements
The solution is already optimal for the given constraints (n ≤ 300). Using a fixed-size array of length 26 instead of `Counter` would reduce constant factors but is not necessary. The code is clear, handles all edge cases, and achieves the best possible asymptotic complexity.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
