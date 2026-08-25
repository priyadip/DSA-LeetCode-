# 150. Evaluate Reverse Polish Notation - Solution Analysis

## Problem Understanding
The input is an array of strings representing a valid Reverse Polish Notation (postfix) expression. Operands are integers in `[-200, 200]`; operators are `+`, `-`, `*`, `/`. Division must truncate toward zero. The expression is guaranteed valid with no division by zero, and all intermediate results fit in a 32-bit integer. The output is the single integer result of evaluating the expression.

## Approach
The solution uses a **stack** to evaluate the postfix expression. This is the canonical algorithm for RPN: operands are pushed onto the stack; when an operator appears, the top two operands are popped, the operation is applied (first popped is the right operand, second is the left), and the result is pushed back. The brute-force alternative would be to recursively parse the expression tree, which would require building the tree first and uses O(n) extra space for the tree nodes plus recursion overhead. The stack approach evaluates in a single left-to-right pass with O(n) time and O(n) space (worst-case stack depth). The key insight is that postfix notation eliminates the need for parentheses or precedence rules — the order of tokens alone dictates evaluation order, and a stack naturally captures the "most recent operands waiting for an operator" invariant.

## Algorithm
1. Initialise an empty stack.
2. Iterate through each token in `tokens`:
   a. If the token is an operand (not one of `+`, `-`, `*`, `/`), convert to `int` and push onto the stack.
   b. Otherwise (token is an operator):
      i. Pop the top value as `b` (right operand).
      ii. Pop the next value as `a` (left operand).
      iii. Apply the operator: `a + b`, `a - b`, `a * b`, or `int(a / b)` for division (truncates toward zero).
      iv. Push the result back onto the stack.
3. After processing all tokens, the stack contains exactly one value — the final result. Return it.

## Line-by-Line Explanation
- `stack = []`: Initialises the operand stack.
- `for token in tokens:`: Single left-to-right pass over the input.
- `if token not in "+-*/":`: Checks whether the token is an operand (any string not exactly one of the four operators).
- `stack.append(int(token))`: Converts the operand string to an integer and pushes it.
- `continue`: Skips the operator logic for this iteration.
- `b = stack.pop()`: Pops the right operand (most recently pushed).
- `a = stack.pop()`: Pops the left operand (pushed before `b`).
- `if token == "+": stack.append(a + b)`: Addition.
- `elif token == "-": stack.append(a - b)`: Subtraction (left minus right).
- `elif token == "*": stack.append(a * b)`: Multiplication.
- `else: stack.append(int(a / b))`: Division; `a / b` produces a float, `int()` truncates toward zero as required.
- `return stack[-1]`: The final result is the sole remaining stack element.

## Dry Run
Example 2: `tokens = ["4","13","5","/","+"]`

| Step | token | stack before | a | b | operation | stack after | Action |
|------|-------|--------------|---|---|-----------|-------------|--------|
| 1 | "4" | [] | - | - | - | [4] | push 4 |
| 2 | "13" | [4] | - | - | - | [4, 13] | push 13 |
| 3 | "5" | [4, 13] | - | - | - | [4, 13, 5] | push 5 |
| 4 | "/" | [4, 13, 5] | 13 | 5 | int(13/5)=2 | [4, 2] | pop 5, pop 13, push 2 |
| 5 | "+" | [4, 2] | 4 | 2 | 4+2=6 | [6] | pop 2, pop 4, push 6 |
| End | - | [6] | - | - | - | - | return 6 |

## Complexity
- Time: O(n), where n = `len(tokens)`. Each token is processed once; each stack operation is O(1).
- Space: O(n) in the worst case (e.g., all operands followed by all operators, stack grows to ~n/2). The constraints guarantee n ≤ 10⁴, so this is easily within limits.

## Edge Cases
- **Single operand**: `tokens = ["42"]` → stack becomes `[42]`, returns 42. Handled correctly (loop pushes, no operators, final return works).
- **Negative operands**: `tokens = ["-3","2","/"]` → `int(-3/2) = -1` (truncates toward zero). Python's `int(-1.5)` yields `-1`, matching spec.
- **Division truncation toward zero**: `tokens = ["7","-3","/"]` → `int(7/-3) = -2` (since 7/-3 ≈ -2.33, truncates to -2). Correct.
- **Large valid expression**: Up to 10⁴ tokens; stack depth ≤ 5000, well within Python recursion/stack limits (no recursion used).
- **All operators at end**: e.g., `["1","2","3","+","*"]` → stack grows to 3, then shrinks. Works.
- The constraints guarantee non-empty input, valid RPN, no division by zero, and 32-bit intermediate results, so no additional guards are needed.

## Possible Improvements
The solution is already optimal in time (O(n)) and space (O(n)) for the given constraints. A minor clarity improvement: replace `if token not in "+-*/":` with a set lookup `if token not in {"+", "-", "*", "/"}:` for O(1) membership (though the string scan is trivial for length 4). Alternatively, use a dictionary mapping operators to functions (`ops = {"+": lambda a,b: a+b, ...}`) to eliminate the if/elif chain, but the current explicit branches are perfectly readable and avoid lambda overhead. No material algorithmic improvement exists.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
