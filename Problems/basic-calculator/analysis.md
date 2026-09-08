# 224. Basic Calculator - Solution Analysis

## Problem Understanding
The input is a string `s` containing digits, `'+'`, `'-'`, `'('`, `')'`, and spaces. It represents a valid arithmetic expression where `'+'` and `'-'` are binary operators (except `'-'` can be unary), parentheses group sub‑expressions, and spaces are insignificant. The task is to evaluate the expression and return the integer result. Constraints: length up to 3·10⁵, no two consecutive operators, every intermediate value fits in a signed 32‑bit integer. The key challenge is handling parentheses which require saving and restoring the evaluation state.

## Approach
**Pattern:** Stack‑based iterative parsing.  
The expression contains only addition and subtraction (same precedence) and parentheses. A single left‑to‑right pass can evaluate it if we maintain a running `result` and the `sign` of the next operand. When a `'('` appears, the current `result` and `sign` are pushed onto a stack and reset for the sub‑expression. When a `')'` appears, the sub‑expression result is combined with the saved state. This avoids recursion and processes each character once.

**Brute force:** A recursive descent parser would also be O(n) time but uses the call stack (O(n) space) and is more verbose. Converting to RPN (Shunting‑Yard) would be O(n) time and space but overkill for only two operators.

**Key insight:** Because `+` and `-` have equal precedence and are left‑associative, the expression can be evaluated by accumulating `sign * operand` into `result` whenever an operator or closing parenthesis is met; parentheses only require saving the current `result` and `sign` on a stack.

## Algorithm
1. Initialise `stack = []`, `operand = 0`, `result = 0`, `sign = 1`.
2. For each character `char` in `s`:
   - If `char` is a digit: `operand = operand * 10 + int(char)`.
   - If `char == '+'`: `result += sign * operand`; `operand = 0`; `sign = 1`.
   - If `char == '-'`: `result += sign * operand`; `operand = 0`; `sign = -1`.
   - If `char == '('`: push `(result, sign)` onto `stack`; `result = 0`; `sign = 1`.
   - If `char == ')'`: `result += sign * operand`; `operand = 0`; pop `(prev_result, prev_sign)`; `result = prev_result + prev_sign * result`.
   - Spaces are ignored (no branch matches them).
3. After the loop, return `result + sign * operand` (adds the last pending operand).

## Line-by-Line Explanation
- `stack = []`: Holds tuples `(result_before_parenthesis, sign_before_parenthesis)`.
- `operand = 0`: Accumulates the current number being read.
- `result = 0`: Running total of the current level (inside current parentheses).
- `sign = 1`: Sign (`+1` or `-1`) to apply to the next operand.
- `for char in s:`: Iterate over every character.
- `if char.isdigit(): operand = operand * 10 + int(char)`: Build multi‑digit numbers.
- `elif char == '+': result += sign * operand; operand = 0; sign = 1`: Finalise the previous operand with its sign, reset for next, set sign positive.
- `elif char == '-': result += sign * operand; operand = 0; sign = -1`: Same but sign negative (handles unary minus because `operand` is 0 at start or after `(`).
- `elif char == '(': stack.append((result, sign)); result = 0; sign = 1`: Save current state, start fresh for sub‑expression.
- `elif char == ')': result += sign * operand; operand = 0; prev_result, prev_sign = stack.pop(); result = prev_result + prev_sign * result`: Finish sub‑expression, combine with saved state.
- `return result + sign * operand`: Add the last operand (if any) after the loop ends.

## Dry Run
Example: `s = "(1+(4+5+2)-3)+(6+8)"` → expected 23.

| Step | char | operand | result | sign | stack (top at right) | Action |
|------|------|---------|--------|------|----------------------|--------|
| 1 | '(' | 0 | 0 | 1 | [(0, 1)] | push (0,1); reset result=0, sign=1 |
| 2 | '1' | 1 | 0 | 1 | [(0, 1)] | build operand |
| 3 | '+' | 0 | 1 | 1 | [(0, 1)] | result += 1*1=1; operand=0; sign=1 |
| 4 | '(' | 0 | 0 | 1 | [(0, 1), (1, 1)] | push (1,1); reset result=0, sign=1 |
| 5 | '4' | 4 | 0 | 1 | [(0, 1), (1, 1)] | build operand |
| 6 | '+' | 0 | 4 | 1 | [(0, 1), (1, 1)] | result += 1*4=4; operand=0; sign=1 |
| 7 | '5' | 5 | 4 | 1 | [(0, 1), (1, 1)] | build operand |
| 8 | '+' | 0 | 9 | 1 | [(0, 1), (1, 1)] | result += 1*5=9; operand=0; sign=1 |
| 9 | '2' | 2 | 9 | 1 | [(0, 1), (1, 1)] | build operand |
|10 | ')' | 0 | 11 | 1 | [(0, 1)] | result += 1*2=11; pop (1,1); result = 1 + 1*11 = 12 |
|11 | '-' | 0 | 12 | -1 | [(0, 1)] | result += 1*0=12; operand=0; sign=-1 |
|12 | '3' | 3 | 12 | -1 | [(0, 1)] | build operand |
|13 | ')' | 0 | 9 | 1 | [] | result += (-1)*3=9; pop (0,1); result = 0 + 1*9 = 9 |
|14 | '+' | 0 | 9 | 1 | [] | result += 1*0=9; operand=0; sign=1 |
|15 | '(' | 0 | 0 | 1 | [(9, 1)] | push (9,1); reset result=0, sign=1 |
|16 | '6' | 6 | 0 | 1 | [(9, 1)] | build operand |
|17 | '+' | 0 | 6 | 1 | [(9, 1)] | result += 1*6=6; operand=0; sign=1 |
|18 | '8' | 8 | 6 | 1 | [(9, 1)] | build operand |
|19 | ')' | 0 | 14 | 1 | [] | result += 1*8=14; pop (9,1); result = 9 + 1*14 = 23 |
|20 | end | 0 | 23 | 1 | [] | return 23 + 1*0 = 23 |

## Complexity
- **Time:** O(n) where n = len(s). Each character is examined once; all operations inside the loop are O(1).
- **Space:** O(n) worst‑case for the stack (e.g., `((((...)))`). The stack depth equals the maximum nesting level of parentheses, which can be Θ(n) in the worst case.

## Edge Cases
- **Unary minus at start:** `"-12"` → first `'-'` adds `sign*operand` (0) to result, sets `sign=-1`, then digits build operand=12, final return gives -12. Works.
- **Unary minus before parentheses:** `"-(3+2)"` → same logic, `sign=-1` saved on stack, sub‑expression evaluated, then combined with negative sign.
- **Multiple digits:** `"123"` → operand builds to 123, no operator triggers addition until end, final return adds it.
- **Spaces:** `" 2 - 1 "` → spaces match no branch, effectively skipped.
- **Single number:** `"42"` → loop only builds operand, final return returns 42.
- **Deep nesting:** Up to 3·10⁵ characters, stack may grow to ~1.5·10⁵; Python list handles it.
- **Empty string:** Not possible per constraints (length ≥ 1).

## Possible Improvements
The solution is already optimal for the given constraints: O(n) time and O(n) space (worst‑case stack depth) is the best achievable for this problem because parentheses require saving state proportional to nesting depth. Variable names (`operand`, `result`, `sign`, `stack`) are clear and conventional. No redundant passes or structures exist. The only minor stylistic addition could be an explicit `elif char == ' ': continue` for readability, but the current implicit ignore is fine and slightly faster.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
