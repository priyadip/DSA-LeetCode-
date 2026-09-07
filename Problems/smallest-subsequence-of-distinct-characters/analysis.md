# 1081. Smallest Subsequence of Distinct Characters - Solution Analysis

## Problem Understanding
Given a string `s` of lowercase letters, return the lexicographically smallest subsequence that contains every distinct character of `s` exactly once. The subsequence must preserve the relative order of characters from `s`. The length of `s` is up to 1000, and the alphabet size is fixed at 26, so an O(n) solution with O(1) auxiliary space is expected.

## Approach
The solution uses a **monotonic stack** with a greedy strategy. A brute-force approach would enumerate all valid subsequences, which is exponential. The monotonic stack builds the answer in a single left-to-right pass, maintaining the invariant that the stack is the lexicographically smallest prefix achievable with the characters processed so far, provided the remaining characters can still complete the set. The key insight: a character at the top of the stack can be safely removed if it is larger than the current character and appears again later in the string, because we can always add it back when we encounter its later occurrence.

## Algorithm
1. Compute `last`, a dictionary mapping each character to its last occurrence index in `s`.
2. Initialize an empty list `stack` to hold the result characters and a set `seen` to track characters currently in `stack`.
3. Iterate over `s` with index `i` and character `c`:
   - If `c` is already in `seen`, skip it (we only need each distinct character once).
   - While `stack` is not empty, the top character `stack[-1]` is lexicographically greater than `c`, and `last[stack[-1]] > i` (the top character appears again later):
     - Pop the top character from `stack` and remove it from `seen`.
   - Append `c` to `stack` and add it to `seen`.
4. Join `stack` into a string and return it.

## Line-by-Line Explanation
- `last = {c: i for i,c in enumerate(s)}`: Records the last index of each character; used to decide if a stacked character can be popped and re-added later.
- `stack = []`: Accumulates the output characters in order; maintained as a monotonic increasing sequence where possible.
- `seen = set()`: Provides O(1) check for whether a character is already in `stack`.
- `for i, c in enumerate(s):`: Processes each character with its position.
- `if c in seen: continue`: Skips duplicates; we only need the first occurrence that fits the greedy construction.
- `while stack and stack[-1] > c and last[stack[-1]] > i:`: Pops larger characters that can still be found later, improving lexicographical order.
- `seen.remove(stack.pop())`: Removes the popped character from both `stack` and `seen`.
- `stack.append(c)`: Adds the current (smaller or necessary) character to the result prefix.
- `seen.add(c)`: Marks the character as included.
- `return "".join(stack)`: Converts the list of characters into the final string.

## Dry Run

| Step | i | c | stack (after) | seen (after) | Action |
|------|---|---|---------------|--------------|--------|
| 1 | 0 | b | ['b'] | {'b'} | push 'b' |
| 2 | 1 | c | ['b', 'c'] | {'b', 'c'} | push 'c' |
| 3 | 2 | a | ['a'] | {'a'} | pop 'c', pop 'b', push 'a' |
| 4 | 3 | b | ['a', 'b'] | {'a', 'b'} | push 'b' |
| 5 | 4 | c | ['a', 'b', 'c'] | {'a', 'b', 'c'} | push 'c' |

## Complexity

- Time: O(n), where n = len(s). Each character is pushed onto the stack at most once and popped at most once. The outer loop runs n times, and the total number of inner while iterations across the whole run is bounded by n because each pop corresponds to a previous push.
- Space: O(1) (or O(26) = O(1)). The `last` dictionary, `stack`, and `seen` set each hold at most 26 entries because the input consists only of lowercase English letters. Even though n can be up to 1000, the distinct character count is bounded by 26.

## Edge Cases

- **All characters distinct** (e.g., "abcdef"): The algorithm never pops because `last[stack[-1]] > i` is false for any earlier character (its last occurrence is its only occurrence, which is before the current index). The output is the original string, the only valid subsequence.
- **All characters identical** (e.g., "aaaa"): The first 'a' is pushed; subsequent 'a's are skipped because `c in seen`. Output is "a".
- **String already lexicographically smallest** (e.g., "abc"): No pops occur, output equals input.
- **String with duplicates where a smaller character appears after larger ones** (e.g., "bcabc"): The algorithm correctly pops larger characters that have later occurrences, yielding the smallest subsequence.
- **Maximum distinct characters (26)**: The stack and set never exceed 26 elements, so space remains constant.
- **Single character** (e.g., "z"): Returns "z".

The constraints guarantee non-empty input and only lowercase letters, so empty string and non-lowercase cases are not applicable.

## Possible Improvements

The solution is already optimal for the given constraints. It achieves O(n) time and O(1) space (alphabet size 26). The variable names (`last`, `stack`, `seen`) are clear and idiomatic. No redundant passes or structures exist. A micro-optimisation could replace the `set` with a fixed-size boolean array of length 26 for slightly faster membership checks, but the asymptotic complexity remains the same and the current code is perfectly acceptable.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
