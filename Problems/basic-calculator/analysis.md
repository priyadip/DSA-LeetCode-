# 224. Basic Calculator - Solution Analysis

## Problem Understanding

The problem requires evaluating a mathematical expression string `s` containing non-negative integers, addition (`+`), subtraction (`-`), parentheses (`(` and `)`), and spaces. Subtraction can act as a unary operator (e.g., `"-1"` or `"-(2 + 3)"`), but addition is strictly binary.

The key constraints are:
- Expression length $n \le 3 \times 10^5$.
- Expressions are guaranteed to be valid, but may contain nested parentheses and unary minuses.
- No multiplication or division is involved, meaning all operators (`+` and `-`) have equal precedence and can be evaluated left-to-right, subject to parenthetical grouping.

## Approach

The solution uses a **Stack with Iterative Evaluation** pattern.

Since `+` and `-` share equal precedence, we can maintain a running `result` and a `sign` variable ($+1$ or $-1$). Parentheses temporarily override left-to-right evaluation. When an opening parenthesis `(` is encountered, the current context—the running `result` and the incoming `sign` multiplying the parenthesized sub-expression—is saved onto a stack. The state variables are then reset to evaluate the isolated sub-expression. When the matching closing parenthesis `)` is hit, the inner result is finalized, popped off the stack, and combined with the outer calculation.

## Algorithm

1. Initialize `stack = []`, `operand = 0`, `result = 0`, and `sign = 1`.
2. Iterate through each character `char` in string `s`:
   - If `char` is a digit, accumulate it into `operand` (`operand = operand * 10 + digit`).
   - If `char` is `+` or `-`:
     - Flush the completed `operand` into `result`: `result += sign * operand`.
     - Reset `operand` to `0`.
     - Update `sign` to `1` (for `+`) or `-1` (for `-`).
   - If `char` is `(`:
     - Push the current tuple `(result, sign)` onto `stack`.
     - Reset `result` to `0` and `sign` to `1` to evaluate the inner scope independently.
   - If `char` is `)`:
     - Flush the remaining `operand` inside the parentheses into `result`.
     - Reset `operand` to `0`.
     - Pop `(prev_result, prev_sign)` from `stack`.
     - Update `result = prev_result + prev_sign * result`.
3. After the loop, flush the final accumulated `operand`: return `result + sign * operand`.

## Line-by-Line Explanation

```python
stack = []
operand = 0
result = 0  # Final result
sign = 1  # Sign of the current operand
```
Initializes the tracking state. `stack` stores deferred contexts `(result, sign)` for outer scopes. `operand` builds multi-digit integers digit-by-digit. `sign` holds $+1$ or $-1$ for the next incoming value or sub-expression.

```python
for char in s:
```
Iterates through each character in the input string once.

```python
    if char.isdigit():
        operand = operand * 10 + int(char)
```
Handles multi-digit numbers by shifting previous digits left by a factor of 10 and adding the current digit.

```python
    elif char == '+':
        result += sign * operand
        operand = 0
        sign = 1
    elif char == '-':
        result += sign * operand
        operand = 0
        sign = -1
```
When encountering `+` or `-`, the current `operand` is multiplied by its `sign` and added to `result`. `operand` is reset to `0`, and `sign` is updated for the next term. Note that if `char == '-'` appears at the start of a scope (e.g., `"-2"` or `"(-3)"`), `operand` is `0`, so `result += sign * 0` effectively leaves `result` unchanged while setting `sign = -1` to handle unary minus.

```python
    elif char == '(':
        stack.append((result, sign))
        result = 0
        sign = 1
```
Saves the outer evaluation context `(result, sign)` onto `stack`. It then resets `result = 0` and `sign = 1` so that the sub-expression inside `()` is evaluated as an isolated fresh scope.

```python
    elif char == ')':
        result += sign * operand
        operand = 0
        prev_result, prev_sign = stack.pop()
        result = prev_result + prev_sign * result
```
Completes the current scope: flushes any remaining `operand` into `result`, pops the outer context `(prev_result, prev_sign)`, and combines the inner result with the outer context.

```python
return result + sign * operand
```
Flushes the final `operand` remaining after the loop terminates and returns the total computed value.

## Dry Run

Trace for input `s = "2 - (1 + 2)"`:

| Char | `operand` | `sign` | `result` | `stack` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Initial | `0` | `1` | `0` | `[]` | Setup |
| `'2'` | `2` | `1` | `0` | `[]` | `operand = 2` |
| `' '` | `2` | `1` | `0` | `[]` | Ignored |
| `'-'` | `0` | `-1` | `2` | `[]` | `result += 1 * 2 = 2`, `sign = -1` |
| `' '` | `0` | `-1` | `2` | `[]` | Ignored |
| `'('` | `0` | `1` | `0` | `[(2, -1)]` | Push `(2, -1)`, reset `result = 0, sign = 1` |
| `'1'` | `1` | `1` | `0` | `[(2, -1)]` | `operand = 1` |
| `' '` | `1` | `1` | `0` | `[(2, -1)]` | Ignored |
| `'+'` | `0` | `1` | `1` | `[(2, -1)]` | `result += 1 * 1 = 1`, `sign = 1` |
| `' '` | `0` | `1` | `1` | `[(2, -1)]` | Ignored |
| `'2'` | `2` | `1` | `1` | `[(2, -1)]` | `operand = 2` |
| `')'` | `0` | `1` | `2 - 1 * 3 = -1` | `[]` | Inner `result = 1 + 1*2 = 3`. Pop `(2, -1)`, `result = 2 + (-1)*3 = -1` |

**Final Return:** `result + sign * operand` = `-1 + 1 * 0 = -1`.

## Complexity

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of string `s`. The algorithm processes each character of the string exactly once in a single pass.
- **Space Complexity:** $\mathcal{O}(n)$ in the worst case. The stack depth depends on the maximum depth of nested parentheses. For a string like `(((((1)))))`, the stack stores $\mathcal{O}(n)$ tuples.

## Edge Cases

- **Unary Minus at Start or Scope Boundary:** In expressions like `"-2 + 1"` or `"(-2 + 1)"`, the initial `operand` is `0`. The operator `-` executes `result += sign * 0` (no-op) and sets `sign = -1`, correctly attributing a negative sign to the following number.
- **Spaces:** Ignored automatically since whitespace characters fall through all `if/elif` branches without altering state.
- **Deep Nesting:** Correctly handled by appending to and popping from `stack` in LIFO order.
- **Multi-digit Integers:** Constructed correctly via `operand = operand * 10 + int(char)`.

## Possible Improvements

The solution is already optimal in terms of time ($\mathcal{O}(n)$) and space ($\mathcal{O}(n)$) complexity. 

Minor Python-specific implementation notes:
- **Python 2/3 Compatibility:** The class uses `class Solution(object):` (Python 2 style), which is redundant in Python 3, though LeetCode accepts both.
- **Whitespace handling:** The current code checks `char.isdigit()`, then specific operators, letting spaces fall through. An explicit `elif char == ' ': continue` is not strictly necessary but makes the non-action on spaces explicit.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
