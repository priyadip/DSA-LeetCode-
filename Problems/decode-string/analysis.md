# 394. Decode String - Solution Analysis

## Problem Understanding
The input is an encoded string where patterns `k[encoded_string]` indicate that the substring inside the brackets should be repeated `k` times. The string may contain nested patterns. The output is the fully decoded string. Constraints: `1 <= s.length <= 30`, digits only appear as repeat counts (1–300), brackets are well‑formed, and the final decoded length never exceeds `10^5`. Order matters, duplicates are allowed, and there are no negative numbers or empty input.

## Approach
The solution uses **recursive depth‑first parsing** (DFS). The string is scanned left‑to‑right; when an opening bracket `[` is encountered, the parser recursively decodes the substring until the matching closing bracket `]`, then multiplies the result by the preceding number. This mirrors the nested structure of the encoding. A brute‑force approach would be to repeatedly search for innermost brackets and expand them, costing O(n²) in the worst case. The recursive approach processes each character of the input once and builds the output in a single pass, achieving linear time in the output size.  
**Key insight:** The grammar is naturally recursive – a decoded string is a sequence of either plain letters or a number followed by a recursively decoded substring in brackets.

## Algorithm
1. Store the current parsing index in `self.i` (initially 0).
2. Define a recursive function `dfs()` that returns the decoded string starting at `self.i` and stops at the matching `]` or end of string.
3. Inside `dfs()`:
   - Initialize `ans = ''` (accumulator for this level) and `num = 0` (current repeat count).
   - While `self.i < len(s)`:
     - `ch = s[self.i]`
     - If `ch` is a digit: update `num = num * 10 + int(ch)`.
     - Else if `ch == '['`: increment `self.i` to skip `[`, recursively call `dfs()` to get the inner decoded string, append `inner * num` to `ans`, reset `num = 0`.
     - Else if `ch == ']'`: return `ans` (end of this recursive level).
     - Else (letter): append `ch` to `ans`.
     - Increment `self.i`.
   - Return `ans`.
4. Call `dfs()` and return its result.

## Line-by-Line Explanation
- `self.i = 0`: index pointer shared across recursive calls, tracks current position in `s`.
- `def dfs():`: recursive parser for one level of brackets.
- `ans = ''`: builds the decoded string for the current level.
- `num = 0`: accumulates the repeat count preceding a `[`.
- `while self.i < len(s):`: loop until end of string or a closing bracket returns.
- `ch = s[self.i]`: current character.
- `if ch.isdigit(): num = num*10 + int(ch)`: builds multi‑digit numbers.
- `elif ch == '[':`: enters a nested level.
  - `self.i += 1`: moves past `[` so the recursive call starts at the first inner character.
  - `ans += dfs() * num`: recursively decodes the inner substring, repeats it `num` times, appends to current level.
  - `num = 0`: resets repeat count for the next segment.
- `elif ch == ']': return ans`: closing bracket ends the current recursive level; return the decoded string built so far.
- `else: ans += ch`: plain letter, append directly.
- `self.i += 1`: advance index after processing the character.
- `return ans`: returns the fully decoded string for this level (used when the loop finishes at the top level).
- `return dfs()`: starts parsing from index 0 and returns the final result.

## Dry Run
Example: `s = "3[a2[c]]"`

| Step | self.i | ch   | num | ans (current level) | Action |
|------|--------|------|-----|---------------------|--------|
| 1    | 0      | '3'  | 3   | ''                  | digit → num=3 |
| 2    | 1      | '['  | 3   | ''                  | '[' → i=2, call dfs() (level 2) |
| 2.1  | 2      | 'a'  | 0   | 'a'                 | letter → ans='a' |
| 2.2  | 3      | '2'  | 2   | 'a'                 | digit → num=2 |
| 2.3  | 4      | '['  | 2   | 'a'                 | '[' → i=5, call dfs() (level 3) |
| 2.3.1| 5      | 'c'  | 0   | 'c'                 | letter → ans='c' |
| 2.3.2| 6      | ']'  | 0   | 'c'                 | ']' → return 'c' to level 2 |
| 2.4  | 7      | (after return) | 0 | 'a' + 'c'*2 = 'acc' | level 2: ans='acc', num=0 |
| 2.5  | 7      | ']'  | 0   | 'acc'               | ']' → return 'acc' to level 1 |
| 3    | 8      | (after return) | 0 | '' + 'acc'*3 = 'accaccacc' | level 1: ans='accaccacc' |
| 4    | 8      | end  | 0   | 'accaccacc'         | loop ends, return final result |

Output: `"accaccacc"`

## Complexity
- **Time:** O(L) where L is the length of the decoded output (≤ 10⁵). Each character of the input is examined once, and each character of the output is appended once.
- **Space:** O(L) for the output string plus O(D) for the recursion depth, where D is the maximum nesting level. With `s.length ≤ 30`, D ≤ 15, so the call stack is negligible.

## Edge Cases
- **Single letter / no brackets:** e.g., `"abc"` – the loop never sees `[` or `]`, simply accumulates letters and returns them.
- **Multiple top‑level groups:** e.g., `"2[ab]3[cd]ef"` – after the first `]` returns, the top‑level loop continues and processes the next group.
- **Deep nesting:** maximum depth limited by input length (≤ 30), well within Python’s recursion limit.
- **Large repeat counts:** up to 300, but output length capped at 10⁵, so no overflow issues.
- **Empty input:** not possible per constraints (`s.length ≥ 1`).

## Possible Improvements
The solution is already optimal for the given constraints. The recursive approach is clean and matches the problem’s recursive structure. The commented iterative stack version avoids recursion entirely and would be preferable if nesting depth could be large (e.g., 10⁴), but here it is unnecessary. A minor readability improvement would be to use a closure with a mutable index (e.g., `i = [0]`) instead of `self.i` to avoid an instance variable, but this is purely stylistic.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
