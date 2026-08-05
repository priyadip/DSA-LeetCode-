# 600. Non-negative Integers without Consecutive Ones - Solution Analysis

## Problem Understanding

The problem asks us to count how many integers in the inclusive range $[0, n]$ have a binary representation containing no consecutive `1`s (i.e., no adjacent `11` substring).

Constraints:
- $1 \le n \le 10^9$.
- $10^9 < 2^{30}$, so any value of $n$ fits within a 30-bit unsigned integer (bit indices 0 to 29, or up to bit index 30 to handle $2^{30}-1$).

## Approach

This solution uses **Digit DP** combined with **Fibonacci precomputation**.

1. **Fibonacci Property:** The number of valid binary strings of length $i$ with no consecutive `1`s follows the Fibonacci sequence:
   - Length 0: 1 string (`""`) $\rightarrow f[0] = 1$
   - Length 1: 2 strings (`"0"`, `"1"`) $\rightarrow f[1] = 2$
   - Length 2: 3 strings (`"00"`, `"01"`, `"10"`) $\rightarrow f[2] = 3$
   - Length $i$: A valid string of length $i$ either starts with `0` (followed by any valid string of length $i-1$) or `10` (followed by any valid string of length $i-2$). Thus, $f[i] = f[i-1] + f[i-2]$.

2. **Prefix Matching (Digit DP):** To count valid numbers $\le n$, we process the bits of $n$ from the most significant bit (MSB) down to bit 0:
   - When bit $i$ of $n$ is `1`, we can choose to place a `0` at bit $i$. This strictly guarantees the resulting number is smaller than $n$, freeing the lower $i$ bits to take *any* valid binary string of length $i$ (yielding $f[i]$ combinations).
   - Next, to explore numbers that match $n$'s prefix up to bit $i$, we must set bit $i$ to `1`. If the previous bit (at $i+1$) was also `1`, we encounter `"11"`. Since $n$'s prefix itself is invalid, no valid numbers can exist in this branch or equal $n$, so we terminate early and return `ans`.

## Algorithm

1. Precompute `f`, where `f[i]` store the count of valid binary strings of length `i` up to length 31.
2. Initialize `ans = 0` and `prev_bit = 0`.
3. Iterate bit position `i` from 30 down to 0:
   - Extract the $i$-th bit of $n$: `(n >> i) & 1`.
   - If the bit is `1`:
     - Add `f[i]` to `ans` (counting numbers where bit $i$ is set to `0`).
     - If `prev_bit == 1`, $n$ contains consecutive ones. Stop and return `ans`.
     - Set `prev_bit = 1`.
   - If the bit is `0`:
     - Set `prev_bit = 0`.
4. If the loop completes without early termination, $n$ itself is valid. Return `ans + 1`.

## Line-by-Line Explanation

```python3
f = [1, 2]
for _ in range(30):
    f.append(f[-1] + f[-2])
```
Initializes the DP table `f` with $f[0] = 1, f[1] = 2$ and computes values up to $f[31]$ using the recurrence relation $f[i] = f[i-1] + f[i-2]$.

```python3
ans = 0
prev_bit = 0
```
`ans` accumulates the total count of valid numbers. `prev_bit` tracks the value of the bit directly to the left (bit $i+1$) during iteration.

```python3
for i in range(30, -1, -1):
```
Iterates from bit 30 down to bit 0. Bit 30 is chosen because $2^{30} > 10^9$, ensuring all valid bits of $n$ are checked.

```python3
    if (n >> i) & 1:
```
Checks if the $i$-th bit of $n$ is set to `1`.

```python3
        ans += f[i]            # place 0 here, free lower i bits
```
If bit $i$ of $n$ is `1`, placing `0` at bit $i$ yields numbers $< n$. The lower $i$ bits can form any valid binary combination of length $i$, adding $f[i]$ options.

```python3
        if prev_bit == 1:      # "11" → n itself invalid, stop
            return ans
```
If both bit $i+1$ (`prev_bit`) and bit $i$ are `1`, a `"11"` sequence is formed in $n$'s prefix. No valid integers can share or exceed this prefix, so the search terminates immediately.

```python3
        prev_bit = 1
```
Fixes bit $i$ as `1` for subsequent iterations and records `prev_bit = 1`.

```python3
    else:
        prev_bit = 0
```
If bit $i$ of $n$ is `0`, we must place `0` at bit $i$ to avoid exceeding $n$. Updates `prev_bit = 0`.

```python3
return ans + 1                 # +1 for n itself
```
If the loop finishes without hitting consecutive ones, $n$ itself has no consecutive ones and was not counted by the branching logic. We add `1` for $n$.

## Dry Run

Trace for $n = 5$ (binary `101`):

Precomputed `f`: `f[0]=1, f[1]=2, f[2]=3, f[3]=5, f[4]=8, ...`

For bits $i = 30$ down to $3$, $n$'s bit is `0`. `ans` stays `0`, `prev_bit` remains `0`.

| Bit $i$ | Bit value `(n >> i) & 1` | `prev_bit` before | Action / Branch | `ans` after | `prev_bit` after |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2** | `1` | `0` | Bit $2$ is `1`: add $f[2] = 3$ (choices with bit $2$ set to `0`) | $0 + 3 = 3$ | `1` |
| **1** | `0` | `1` | Bit $1$ is `0`: must keep bit $1$ as `0` | $3$ | `0` |
| **0** | `1` | `0` | Bit $0$ is `1`: add $f[0] = 1$ (choice with bit $0$ set to `0`) | $3 + 1 = 4$ | `1` |

Loop ends cleanly without encountering consecutive ones (`prev_bit == 1` was never true when current bit was `1`).

Final return: `ans + 1` = $4 + 1 = 5$.

Valid integers $\le 5$: $0 (`0`), 1 (`1`), 2 (`10`), 4 (`100`), 5 (`101`)$. Total = 5.

## Complexity

- **Time Complexity:** $\mathcal{O}(1)$ (or $\mathcal{O}(\log n)$). The precomputation takes 30 steps, and the bitwise loop executes exactly 31 iterations regardless of $n$. Since $n \le 10^9$, the bit length is capped by a constant (31).
- **Space Complexity:** $\mathcal{O}(1)$ (or $\mathcal{O}(\log n)$). The DP array `f` stores 32 integers, using a fixed amount of auxiliary memory.

## Edge Cases

- **$n = 1$ (Binary `1`):** Loops down to bit 0, adds $f[0] = 1$, loop finishes, returns $1 + 1 = 2$ ($0$ and $1$). Handled correctly.
- **Numbers with consecutive ones (e.g., $n = 3$, Binary `11`):** At $i=1$, bit is `1`, `ans += f[1]` ($2$). At $i=0$, bit is `1`, `prev_bit == 1` triggers early return of `ans` ($2 + f[0] = 3$, counting $0, 1, 2$). Correctly excludes $3$.
- **Power of two (e.g., $n = 4$, Binary `100`):** Single MSB set, lower bits all `0`. Correctly adds $f[2] = 3$ and then $+1$ at the end for $4$ itself. Total = 4 ($0, 1, 2, 4$).
- **Maximum constraint ($n = 10^9$):** Fits in 30 bits ($10^9 < 2^{30} = 1,073,741,824$). The hardcoded size of 31 entries in `f` is sufficient.

## Possible Improvements

The solution is optimal in both time and space complexity. A minor practical refinement:

- **Skip redundant high bits:** Instead of starting the loop from bit 30, start directly from $n$'s most significant bit position (`n.bit_length() - 1`). This avoids iterating through up to 30 leading zeros, though performance difference is negligible due to the fixed constant cap of 31 iterations.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
