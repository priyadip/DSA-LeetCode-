# 394. Decode String - Solution Analysis

## Problem Understanding
The problem asks us to expand an encoded string formatted with repetition rules of the form `k[encoded_string]`, where `encoded_string` is repeated `k` times. Encoding patterns can be deeply nested (e.g., `3[a2[c]]` expands to `accaccacc`).

The input constraints dictate:
- `1 <= s.length <= 30`
- `1 <= k <= 300`
- The output string length will not exceed $10^5$.
- Input is always well-formed with matching brackets and valid formatting.

The core challenge is processing nested expressions in inner-to-outer order (last-in, first-out pattern).

## Approach
This solution uses **Depth-First Search (DFS) / Recursion** combined with an instance-level index pointer (`self.i`).

Recursion fits hierarchical, nested structures like balanced brackets. Each pair of square brackets `[...]` introduces a subproblem that is structurally identical to the top-level string decoding. When a `'['` is encountered, the algorithm pauses current execution, spawns a child recursive context to decode the enclosed substring, multiplies the returned substring by $k$, and appends it to the parent scope's result.

## Algorithm
1. Store a global index pointer `self.i = 0` attached to the `Solution` instance to track reading position across recursive stack frames.
2. Define recursive function `dfs()`:
   a. Initialize an empty string accumulator `ans = ''` and integer `num = 0`.
   b. Iterate while `self.i < len(s)`:
      - If character is a digit: update `num = num * 10 + int(ch)` to accumulate multi-digit numbers.
      - If character is `'['`: advance `self.i += 1` to skip `'['`, make a recursive call `dfs()`, multiply its output string by `num`, append to `ans`, and reset `num = 0`.
      - If character is `']'`: return `ans` immediately to the caller frame.
      - If character is a lowercase letter: append it directly to `ans`.
      - Increment `self.i += 1`.
3. Invoke `dfs()` and return the final decoded string.

## Line-by-Line Explanation
```python3
class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0 
```
Initializes `self.i` to `0`. Making `i` an attribute allows all recursive function calls to share and advance a single read pointer across string `s`.

```python3
        def dfs():
            ans = ''
            num = 0 
```
Defines `dfs()` to process a single structural scope. `ans` accumulates decoded characters for this scope, and `num` parses the repetition count `k`.

```python3
            while self.i < len(s):
                ch = s[self.i]
```
Loops through characters of `s` using the instance pointer `self.i`.

```python3
                if ch.isdigit():
                    num = num*10 + int(ch)
```
Parses digits into `num`. Multiplying the running total by 10 accounts for multi-digit numbers like `12`.

```python3
                elif ch == '[':
                    self.i += 1
                    ans += dfs()*num
                    num = 0
```
When encountering `'['`:
1. `self.i += 1` moves the pointer past `'['`.
2. `dfs()` processes the nested substring until it encounters the matching `']'`.
3. `dfs() * num` repeats the inner decoded string `num` times and appends it to `ans`.
4. `num = 0` resets the multiplier for subsequent tokens.

```python3
                elif ch == ']':
                    return ans
```
When encountering `']'`, the current scope has finished parsing its bracketed content. It returns `ans` to its parent call frame. Note that `self.i` remains pointing at `']'` at the exact moment of return.

```python3
                else:
                    ans += ch
```
Appends regular lowercase characters directly to `ans`.

```python3
                self.i += 1
```
Advances `self.i` to the next character. Crucially, when returning from an inner `dfs()` call back to the `elif ch == '['` block, this line executes afterwards, which consumes the matching `']'` that caused the inner `dfs()` to terminate.

```python3
            return ans
        return dfs()
```
Returns `ans` when reaching the end of the input string, and initiates the root `dfs()` call.

## Dry Run
Tracing `s = "3[a2[c]]"` (length = 8, indices 0 to 7):

| Frame Depth | `self.i` (start) | `ch` | Action | `ans` state | `num` state | `self.i` (end of step) |
|---|---|---|---|---|---|---|
| Depth 0 | 0 | `'3'` | `num = 0*10 + 3` | `""` | 3 | 1 |
| Depth 0 | 1 | `'['` | `self.i += 1` (becomes 2), invoke `dfs()` Depth 1 | `""` | 3 | 2 |
| Depth 1 | 2 | `'a'` | Append `'a'` to `ans` | `"a"` | 0 | 3 |
| Depth 1 | 3 | `'2'` | `num = 0*10 + 2` | `"a"` | 2 | 4 |
| Depth 1 | 4 | `'['` | `self.i += 1` (becomes 5), invoke `dfs()` Depth 2 | `"a"` | 2 | 5 |
| Depth 2 | 5 | `'c'` | Append `'c'` to `ans` | `"c"` | 0 | 6 |
| Depth 2 | 6 | `']'` | Match `']'`, `return "c"` | `"c"` | 0 | 6 |
| Depth 1 | 4 | - | Resume from call: `ans += "c"*2` -> `"acc"`, `num=0` | `"acc"` | 0 | 7 (via `self.i += 1`) |
| Depth 1 | 7 | `']'` | Match `']'`, `return "acc"` | `"acc"` | 0 | 7 |
| Depth 0 | 1 | - | Resume from call: `ans += "acc"*3` -> `"accaccacc"`, `num=0` | `"accaccacc"` | 0 | 8 (via `self.i += 1`) |
| Depth 0 | 8 | - | Loop condition `8 < 8` False | `"accaccacc"` | 0 | 8 |

Output: `"accaccacc"`

## Complexity
- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the total length of the generated output string. Each character of the input string is parsed once, and string construction operations scale linearly with the final decoded output size (bounded by $10^5$).
- **Space Complexity:** $\mathcal{O}(D + N)$, where $D$ is the maximum nesting depth of brackets and $N$ is the length of the generated output string. $D$ accounts for the recursion call stack frames ($\le 30$), and $N$ accounts for holding intermediate string buffers during concatenation.

## Edge Cases
- **Multi-digit multipliers:** Correctly handled by `num = num*10 + int(ch)`.
- **Nested patterns:** Handled through recursive `dfs()` call execution stack.
- **Unbracketed trailing/leading characters:** Handled by the `else` branch in the main loop body.
- **Fragility under relaxed constraints:**
  - If maximum nesting depth $D$ were thousands of levels deep, recursion would raise a `RecursionError` due to Python's call stack limit ($\sim 1000$).
  - String concatenation `ans += ...` creates intermediate string objects. In languages without string mutable builders or Python instances with extreme string lengths, list appending (`[].append(...)` followed by `''.join(...)`) is safer.

## Possible Improvements
1. **Iterative Stack Approach:** The commented-out stack approach in your submission file avoids recursion limits entirely by keeping state (`curr_str`, `num`) explicitly on a Python `list` stack:
   ```python3
   class Solution:
       def decodeString(self, s: str) -> str:
           stack = []
           curr_str = ''
           num = 0
           for ch in s:
               if ch.isdigit():
                   num = num * 10 + int(ch)
               elif ch == '[':
                   stack.append((curr_str, num))
                   curr_str, num = '', 0
               elif ch == ']':
                   prev_str, repeat_count = stack.pop()
                   curr_str = prev_str + curr_str * repeat_count
               else:
                   curr_str += ch
           return curr_str
   ```
   This iterative stack pattern is cleaner than mutating shared instance state (`self.i`) across recursive stack frames.

2. **Decouple state mutation:** In the active solution, `self.i` is incremented in two separate places (`self.i += 1` inside `elif ch == '['` and at the end of the loop). While correct, this implicit contract—where the inner recursive call leaves `self.i` pointing at `']'` and the outer call increments past it—is subtle and easy to break during refactoring.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
