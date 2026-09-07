# 3517. Smallest Palindromic Rearrangement I - Solution Analysis

## Problem Understanding
Given a palindromic string `s` of lowercase letters (length up to 10^5), we must return the lexicographically smallest palindrome that is a permutation of `s`. Because `s` is already a palindrome, its character counts contain at most one odd frequency. Lexicographic order is determined by the left half of the palindrome; the right half is forced to be its mirror. Therefore, the problem reduces to arranging the available characters so that the left half is as small as possible.

## Approach
The solution uses **counting sort** (frequency array) combined with **greedy construction**. It counts each character's frequency, then builds the left half by taking `freq[i] // 2` copies of each character in alphabetical order (`'a'` to `'z'`). The middle character (if any) is the one with an odd count. The final palindrome is `left + mid + reverse(left)`.  

Brute force would enumerate all permutations, which is infeasible. Counting sort exploits the fixed alphabet size (26) to achieve O(n) time and O(1) extra space. The key insight is that the lexicographically smallest palindrome is obtained by sorting the first half of the characters in ascending order.

## Algorithm
1. Count the frequency of each lowercase letter in `s` using a fixed-size array of length 26.
2. Initialise an empty list `left` for the left half of the result and an empty string `mid` for the centre character.
3. Iterate `i` from 0 to 25 (i.e. 'a' to 'z'):
   - Append `chr(i+97)` repeated `freq[i] // 2` times to `left`. This places the maximum possible pairs of the current smallest character at the end of the left half, keeping the left half lexicographically minimal.
   - If `freq[i]` is odd, record `chr(i+97)` in `mid`. Because the input is guaranteed palindromic, at most one character has an odd count, so this assignment happens at most once.
4. Join `left` into a single string.
5. Return the concatenation `left + mid + left[::-1]`, which mirrors the left half around the optional centre character to form the smallest palindrome.

## Line-by-Line Explanation
`freq = [0]*26`: Allocates a counting array for 'a'–'z'.

`for ch in s:` / `freq[ord(ch)-97] += 1`: Populates the frequency array in O(n) time.

`left = []` / `mid = ''`: Prepares containers for the left half (as a list of strings for efficient appends) and the middle character.

`for i in range(26):`: Processes characters in alphabetical order, which is the greedy choice for lexicographically smallest left half.

`if freq[i]:`: Skips characters that do not appear.

`left.append(chr(i+97)*(freq[i]//2))`: Adds half of the current character's count (the number of pairs) to the left half. Multiplying the character by the pair count produces the correct run of characters in one step.

`if freq[i] & 1:` / `mid = chr(i+97)`: Detects an odd frequency using a bitwise AND. Since the input is a palindrome, this branch executes at most once; the character stored becomes the centre of the final palindrome.

`left = ''.join(left)`: Flattens the list of runs into the complete left-half string.

`return left+mid+left[::-1]`: Constructs the full palindrome by mirroring the left half. The middle character (empty string if length is even) sits between the two halves. This yields the lexicographically smallest palindromic permutation because the left half is built from the smallest available characters first.

## Dry Run

**Example:** `s = "babab"`

### Frequency counting loop
| Step | ch | freq before (indices 0,1) | freq after (indices 0,1) | Action |
|------|----|---------------------------|--------------------------|--------|
| 1 | 'b' | [0, 0] | [0, 1] | `freq[1] += 1` |
| 2 | 'a' | [0, 1] | [1, 1] | `freq[0] += 1` |
| 3 | 'b' | [1, 1] | [1, 2] | `freq[1] += 1` |
| 4 | 'a' | [1, 2] | [2, 2] | `freq[0] += 1` |
| 5 | 'b' | [2, 2] | [2, 3] | `freq[1] += 1` |

### Construction loop (iterating `i = 0..25`)
| Step | i | char | freq[i] | left (list) | mid | Action |
|------|---|------|---------|-------------|-----|--------|
| 1 | 0 | 'a' | 2 | `['a']` | `''` | append `'a' * (2//2) = 'a'`; `freq[0] & 1 == 0` |
| 2 | 1 | 'b' | 3 | `['a', 'b']` | `'b'` | append `'b' * (3//2) = 'b'`; `freq[1] & 1 == 1` → `mid = 'b'` |
| 3 | 2–25 | – | 0 | unchanged | unchanged | `freq[i] == 0` → skip |

**Final assembly:**  
`left = ''.join(['a','b']) = "ab"`  
`return "ab" + "b" + "ba" = "abbba"`

## Complexity
- **Time:** O(n), where n = len(s). The first loop visits each character once (n iterations). The second loop runs a constant 26 times. String joining and reversal are linear in the length of `left` (≤ n/2).
- **Space:** O(n). The frequency array uses O(1) space (26 integers). The `left` list holds n/2 characters, and the final result string holds n characters.

## Edge Cases
- The solution assumes the input string `s` is palindromic, which guarantees at most one character has an odd frequency. The code sets `mid` to the last character with an odd count (since it iterates from 'a' to 'z'), but because there is at most one such character, this is correct. If the constraint were relaxed and `s` could have multiple odd counts, the algorithm would silently drop characters (by using `freq[i]//2` for each) and produce a string that is not a permutation of `s`.
- Single-character strings: `left` is empty, `mid` becomes that character, returns the character itself.
- Even-length palindromes: no character has an odd count, `mid` remains `''`, and the result is `left + left[::-1]`.
- Maximum input size (10^5): the algorithm runs in O(n) time with O(n) auxiliary space for the output and the `left` string, which is acceptable.

## Possible Improvements
The solution is already optimal for the given constraints. It uses counting sort (O(n + 26) time) and builds the lexicographically smallest left half directly by iterating from 'a' to 'z'. The space complexity is O(n) for the output, which is unavoidable. The alternative implementation commented out uses a pre-allocated list and two pointers, but it does not improve asymptotic complexity and is more verbose. No material improvement is needed.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
