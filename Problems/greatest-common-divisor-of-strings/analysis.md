# 1071. Greatest Common Divisor of Strings - Solution Analysis

## Problem Understanding
Given two strings `str1` and `str2` (lengths 1–1000, uppercase letters), find the longest string `x` such that both `str1` and `str2` can be formed by concatenating `x` with itself one or more times. If no such string exists, return the empty string. The order of characters matters, and the divisor string must be a prefix of both inputs.

## Approach
The solution uses a **mathematical insight combined with the Euclidean algorithm on string lengths**. The key observation is that a common divisor string exists if and only if `str1 + str2 == str2 + str1`; this concatenation equality is both necessary and sufficient. When it holds, the length of the greatest common divisor string is exactly `gcd(len(str1), len(str2))`, and the string itself is the prefix of that length from either input. This reduces the problem to an integer GCD computation (O(log min(m,n))) plus a linear-time concatenation check (O(m+n)). The brute-force alternative would test every prefix length up to `min(m,n)` for divisibility, costing O(min(m,n)·(m+n)) time. The chosen approach exploits the algebraic property of string periods to achieve optimal linear time.

## Algorithm
1. Check if `str1 + str2` equals `str2 + str1`. If not, no string can divide both, so return `""`.
2. Compute `l = gcd(len(str1), len(str2))` using the Euclidean algorithm (via `math.gcd`).
3. Return the prefix `str1[:l]`, which is the longest string that can be repeated to form both inputs.

The concatenation check works because if a string `x` divides both `str1` and `str2`, then `str1 = x * a` and `str2 = x * b` for integers `a, b`. Then `str1 + str2 = x * (a + b) = str2 + str1`. Conversely, if the concatenations are equal, both strings are composed of repetitions of the same base pattern, and the longest such pattern has length equal to the GCD of the two lengths.

## Line-by-Line Explanation
- `if str1 + str2 != str2+str1:`: Verifies the necessary condition for a common divisor string to exist; if the two concatenation orders differ, the strings share no repeating base pattern.
- `return ''`: Early exit when the condition fails — no common divisor possible.
- `l = gcd(len(str1), len(str2))`: Computes the greatest common divisor of the two string lengths; this is the maximum possible length of a string that can tile both inputs.
- `return str1[:l]`: Returns the prefix of `str1` of length `l`, which is guaranteed to be the GCD string when the concatenation check passes.

## Dry Run
Trace Example 1: `str1 = "ABCABC"`, `str2 = "ABC"`.

| Step | Code | State / Result |
|------|------|----------------|
| 1 | `if str1 + str2 != str2 + str1:` | `"ABCABC" + "ABC" = "ABCABCABC"`; `"ABC" + "ABCABC" = "ABCABCABC"`; equal → condition false, continue |
| 2 | `l = gcd(len(str1), len(str2))` | `len(str1)=6`, `len(str2)=3`; `gcd(6,3)=3` → `l=3` |
| 3 | `return str1[:l]` | `str1[:3] = "ABC"` → returns `"ABC"` |

## Complexity
- Time: O(n + m), where n = len(str1), m = len(str2). Concatenating and comparing the two strings takes O(n + m); the Euclidean gcd runs in O(log min(n, m)), which is dominated.
- Space: O(n + m), because `str1 + str2` and `str2 + str1` each create a new string of length n + m.

## Edge Cases
- **Concatenation order mismatch**: The check `str1 + str2 != str2 + str1` correctly identifies when no common divisor exists (e.g., `"LEET" + "CODE" != "CODE" + "LEET"`). This single condition subsumes all cases where the strings are not composed of the same repeating unit.
- **Different lengths with common prefix but different periods**: e.g., `str1 = "ABABAB"`, `str2 = "ABAB"`. The concatenation check passes (`"ABABABABAB" == "ABABABABAB"`), `gcd(6,4)=2`, and `str1[:2]="AB"` is the correct largest divisor.
- **One string is a multiple of the other**: e.g., `str1 = "ABCABC"`, `str2 = "ABC"`. `gcd(6,3)=3`, returns `"ABC"`.
- **All characters identical**: e.g., `str1 = "AAAA"`, `str2 = "AA"`. `gcd(4,2)=2`, returns `"AA"`.
- **Maximum input size (1000 each)**: Concatenation creates a 2000-character string; well within Python's memory and time limits. The `gcd` computation is `O(log min(m,n))`.

The constraints guarantee non-empty strings, so empty-input handling is unnecessary.

## Possible Improvements
- **Missing import**: The code uses `gcd` without `from math import gcd`. This would raise `NameError` in a clean environment. Add the import.
- **Variable name `l`**: Use `gcd_len` (or `g`) to avoid confusion with the digit `1`.
- **Avoid allocation (optional)**: The concatenation check allocates two new strings of length `m+n`. For the given constraints this is trivial, but it can be made `O(1)` space by verifying `str1[i % len(str1)] == str2[i % len(str2)]` for `i` in `range(m+n)` (or by checking `str1 * n == str2 * m` which still allocates). The current approach is acceptable for `n ≤ 1000`.
- **Remove dead code**: The commented brute-force implementation adds noise and should be deleted.

The algorithmic complexity is already optimal: `O(m+n)` time and `O(m+n)` space (dominated by the concatenation), which is the best achievable for this problem under the given constraints.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
