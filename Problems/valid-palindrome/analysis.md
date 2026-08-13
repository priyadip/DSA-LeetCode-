# 125. Valid Palindrome - Solution Analysis

## Problem Understanding
The task asks whether a given string `s` reads the same forwards and backwards after stripping all non-alphanumeric characters and converting all remaining letters to lowercase. Empty strings or strings with no alphanumeric characters are valid palindromes. With $s.\text{length} \le 2 \times 10^5$, an optimal solution must run in $O(N)$ time and should ideally avoid allocating additional memory for filtered copies of the string.

## Approach
This solution uses the **two pointers** pattern (converging from opposite ends). 

A baseline approach creates a new filtered, lowercased string via regular expressions or list comprehensions and checks if it equals its reverse, which requires $O(N)$ auxiliary space. The two-pointer approach avoids this allocation by traversing the string in-place: one pointer advances from the left and another retreats from the right, skipping non-alphanumeric characters on the fly. 

**Key Insight:** Symmetric character equality can be validated directly on the original string in $O(1)$ space by skipping non-alphanumeric characters dynamically until the pointers meet.

## Algorithm
1. Initialize two pointers: `l` at the beginning (`0`) and `r` at the end (`len(s) - 1`).
2. While `l < r`:
   1. Increment `l` while `l < r` and `s[l]` is not alphanumeric.
   2. Decrement `r` while `l < r` and `s[r]` is not alphanumeric.
   3. Compare `s[l].lower()` and `s[r].lower()`. If they differ, return `False`.
   4. Advance `l` by 1 and `r` by -1 to move to the next inner pair of characters.
3. If the loop completes without finding a mismatch, return `True`.

## Line-by-Line Explanation
- `l, r = 0, len(s) - 1`: Sets up two pointers at the outer boundaries of the string.
- `while l < r:`: Drives the inward scan, terminating when the pointers meet or cross.
- `while l < r and not s[l].isalnum():`: Scans forward to find the next valid alphanumeric character from the left, bound-checked against `r` to prevent overshooting.
- `l += 1`: Moves the left pointer forward past non-alphanumeric characters.
- `while l < r and not s[r].isalnum():`: Scans backward to find the next valid alphanumeric character from the right, bound-checked against `l`.
- `r -= 1`: Moves the right pointer backward past non-alphanumeric characters.
- `if s[l].lower() != s[r].lower():`: Normalizes both characters to lowercase and checks for a mismatch.
- `return False`: Immediately exits with a negative result upon encountering the first asymmetric character pair.
- `l += 1`: Advances the left pointer inward after a successful character match.
- `r -= 1`: Advances the right pointer inward after a successful character match.
- `return True`: Returns success once all symmetric alphanumeric pairs have been validated.

## Dry Run

Trace of `s = "race a car"` (length = 10):

| Step | `l` | `s[l]` | `r` | `s[r]` | Inner While Advances | `s[l].lower() == s[r].lower()` | Action |
|---|---|---|---|---|---|---|---|
| 1 | 0 | `'r'` | 9 | `'r'` | None (both alphanumeric) | `'r' == 'r'` (True) | `l += 1`, `r -= 1` |
| 2 | 1 | `'a'` | 8 | `'a'` | None (both alphanumeric) | `'a' == 'a'` (True) | `l += 1`, `r -= 1` |
| 3 | 2 | `'c'` | 7 | `'c'` | None (both alphanumeric) | `'c' == 'c'` (True) | `l += 1`, `r -= 1` |
| 4 | 3 | `'e'` | 6 | `' '` | `r` decrements to 5 (`s[5] = 'a'`) | `'e' == 'a'` (False) | Return `False` |

---

## Complexity

- **Time:** $O(n)$, where $n$ is the length of `s` ($1 \le n \le 2 \times 10^5$). Each character is evaluated by `isalnum()` at most once by `l` and once by `r`. The pointers move inward monotonically and meet in at most $n$ total pointer increments/decrements.
- **Space:** $O(1)$. Pointers are updated in-place on the input string without allocating auxiliary strings or filtered arrays.

---

## Edge Cases

- **No alphanumeric characters (e.g., `s = ".,:;"`):** The inner `while` conditions `l < r` ensure neither pointer goes out of bounds. The pointers cross each other, the check compares equal characters or exits the outer loop, correctly returning `True`.
- **Single character (e.g., `s = "a"` or `s = " "`):** The outer loop condition `l < r` is immediately `0 < 0` (False), skipping the loop and returning `True`.
- **Mixed case and numeric characters (e.g., `s = "0P"`):** `s[l].lower()` and `s[r].lower()` properly handle ASCII digits without error, returning `False` when comparing `'0'` to `'p'`.

---

## Possible Improvements

The solution is already optimal in both time ($O(n)$) and space ($O(1)$).

A minor observation in the loop structure: if the inner loops skip non-alphanumeric characters until `l == r`, the code still executes the `s[l].lower() != s[r].lower()` check on the same character index before `l` and `r` cross. Because `s[i].lower() == s[i].lower()` is always true, correctness is preserved, but adding an explicit `if l >= r: break` right after the inner skipping loops would avoid an unnecessary character read and comparison on strings composed entirely of non-alphanumerics.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
