# 7. Reverse Integer - Solution Analysis

## Problem Understanding

The problem requires reversing the decimal digits of a signed 32-bit integer $x$. If the resulting reversed integer falls outside the signed 32-bit range $[-2^{31}, 2^{31} - 1]$ (i.e., $[-2147483648, 2147483647]$), the function must return `0`.

A critical constraint stated in the description is:
> Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

This means solutions theoretically should detect potential overflow before performing operations that would exceed 32-bit limits.

---

## Approach

The code uses mathematical digit extraction and reconstruction (modulo and integer division):
- Modulo `% 10` extracts the rightmost (least significant) digit.
- Integer division `// 10` shifts all digits one position to the right, dropping the extracted digit.
- Accumulation via `reversed_x * 10 + digit` shifts existing digits left and appends the new digit.

To avoid handling negative modulo rules across different programming languages, the solution converts negative inputs to positive using `abs(x)`, tracks the original sign, and re-applies it after reversing. Finally, it uses a post-computation range check to detect overflow.

---

## Algorithm

1. Check if $x < 0$. If so, record `sign = -1` and replace $x$ with `abs(x)`. Otherwise, set `sign = 1`.
2. Initialize `reversed_x = 0`.
3. Loop while $x > 0$:
   a. Compute `digit = x % 10`.
   b. Update `reversed_x = reversed_x * 10 + digit`.
   c. Truncate $x$ using `x //= 10`.
4. Multiply `reversed_x` by `sign`.
5. Check if `reversed_x < -2**31` or `reversed_x > 2**31 - 1`.
   a. If out of bounds, return `0`.
   b. Otherwise, return `reversed_x`.

---

## Line-by-Line Explanation

```python
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
```
Determines if $x$ is negative. Storing `sign` allows processing $x$ strictly as a non-negative integer, avoiding Python's negative floor division and modulo behavior (`-123 % 10 = 7` in Python, which differs from C-style truncation towards zero).

```python
        reversed_x = 0
```
Initializes the accumulator variable that will hold the reversed magnitude.

```python
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
```
Standard loop for digit extraction and base-10 shifts:
- `digit = x % 10` isolates the current rightmost digit.
- `reversed_x = reversed_x * 10 + digit` pushes existing digits left by one position and adds the new digit.
- `x //= 10` removes the rightmost digit from $x$.

```python
        reversed_x *= sign
```
Restores the original sign of the integer.

```python
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        else:
            return reversed_x
```
Checks if the final value fits within signed 32-bit bounds (`[-2147483648, 2147483647]`). If it overflows, `0` is returned; otherwise, `reversed_x` is returned.

---

## Dry Run

Input: `x = -123`

| Step | `x` | `sign` | `x != 0` | `digit` | `reversed_x` (before) | `reversed_x` (after) |
|---|---|---|---|---|---|---|
| Init | `-123` -> `123` | `-1` | — | — | — | `0` |
| Loop 1 | `123` -> `12` | `-1` | `True` | `3` | `0` | `0 * 10 + 3 = 3` |
| Loop 2 | `12` -> `1` | `-1` | `True` | `2` | `3` | `3 * 10 + 2 = 32` |
| Loop 3 | `1` -> `0` | `-1` | `True` | `1` | `32` | `32 * 10 + 1 = 321` |
| Exit | `0` | `-1` | `False` | — | — | `321` |

Post-loop:
- `reversed_x *= sign` $\rightarrow$ `321 * -1 = -321`
- Range check: `-2147483648 <= -321 <= 2147483647` is `True`.
- Return `-321`.

---

## Complexity

- **Time Complexity:** $O(\log_{10} |x|)$. The loop processes one decimal digit per iteration. Since $x$ is a 32-bit integer, it has at most 10 decimal digits. Thus, runtime is bounded by at most 10 iterations, which is effectively $O(1)$.
- **Space Complexity:** $O(1)$. Only a fixed number of integer variables (`sign`, `reversed_x`, `digit`) are created.

---

## Edge Cases

- **`x = 0`:** The loop condition `x != 0` is false immediately; returns `0` correctly.
- **Trailing zeroes (`x = 120`):** `120 % 10` gives `0`, setting `reversed_x = 0`. Next iteration adds `2`, yielding `21`. Correctly drops leading zeroes in output.
- **Overflow (`x = 1534236469`):** Reverses to `9646324351`. In Python, this fits in memory without throwing a hardware overflow, but the final range check detects `9646324351 > 2147483647` and correctly returns `0`.
- **`x = -2^31` (`-2147483648`):** In C/C++, `abs(-2147483648)` overflows a standard signed 32-bit integer. Python dynamically handles arbitrarily large integers, so `abs(x)` produces `2147483648` without error, reverses it to `8463847412`, and triggers the bounds check to return `0`.

---

## Possible Improvements

### Technical Soft Constraint Violation
While LeetCode accepts this solution, it technically relies on Python's arbitrary-precision integer support. During execution for inputs like `x = 1534236469`, `reversed_x` grows beyond $2^{31} - 1$ inside the loop before the post-check occurs.

In a strict 32-bit environment (such as C or C++ without 64-bit types), `reversed_x * 10` would trigger integer overflow inside the loop before reaching the return statement.

To strictly satisfy the problem's environment constraint without relying on 64-bit/unbounded math, check for potential overflow **before** multiplying:

```python
# Before multiplying by 10 and adding digit:
if reversed_x > (2**31 - 1) // 10 or (reversed_x == (2**31 - 1) // 10 and digit > 7):
    return 0
```

For Python specifically, the current accepted code runs efficiently and clearly, but understanding pre-computation overflow checking is essential for languages with fixed bit-width integer types.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
