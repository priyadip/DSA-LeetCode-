# 36. Valid Sudoku - Solution Analysis

## Problem Understanding

The problem asks whether a given $9 \times 9$ Sudoku board violates any of the game's basic positioning rules. A board is valid if and only if:
1. No row contains duplicate digits ('1'-'9').
2. No column contains duplicate digits ('1'-'9').
3. None of the nine $3 \times 3$ sub-grids (boxes) contains duplicate digits ('1'-'9').

Empty cells are represented by `'.'`. The board does not need to be solvable or complete—only the filled cells must satisfy these constraints.

---

## Approach

The solution uses a **Hash Set array pattern** (specifically, fixed-size lists of hash sets). 

Instead of checking rows, columns, and $3 \times 3$ boxes in three separate passes, this approach inspects each cell $(r, c)$ in a single pass over the grid. It maintains 9 sets for rows, 9 sets for columns, and 9 sets for sub-boxes.

The 2D box coordinate is flattened into a 1D index from `0` to `8` using integer division:
$$\text{box} = \left(\frac{r}{3}\right) \times 3 + \left(\frac{c}{3}\right)$$

This allows $O(1)$ duplicate checks for row, column, and box constraints simultaneously.

---

## Algorithm

1. Initialize three lists of 9 empty `set` objects: `rows`, `cols`, and `boxes`.
2. Iterate through every cell $(r, c)$ on the $9 \times 9$ board.
3. If `board[r][c]` is `'.' `, skip to the next iteration.
4. Otherwise, extract `num = board[r][c]` and compute the box index `box = (r // 3) * 3 + (c // 3)`.
5. Check if `num` already exists in `rows[r]`, `cols[c]`, or `boxes[box]`. If it exists in any of them, immediately return `False`.
6. Add `num` to `rows[r]`, `cols[c]`, and `boxes[box]`.
7. If the loop completes without finding duplicate conflicts, return `True`.

---

## Line-by-Line Explanation

```python3
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]
```
Creates three lists, each holding 9 independent hash sets. `rows[i]` stores digits seen in row `i`, `cols[j]` stores digits seen in column `j`, and `boxes[k]` stores digits seen in sub-box `k`.

```python3
for r in range(9):
    for c in range(9):
```
Nested loops iterate through all 81 cell coordinates from top-left $(0,0)$ to bottom-right $(8,8)$.

```python3
if board[r][c] == ".":
    continue
```
Ignores empty cells since they do not contribute to duplicate rules.

```python3
num = board[r][c]
box = (r // 3) * 3 + (c // 3)
```
Retrieves the character stored at `(r, c)` and calculates its $3 \times 3$ box index. Rows 0-2 belong to box rows 0, rows 3-5 to box rows 1, and rows 6-8 to box rows 2. Multiplying by 3 and adding `c // 3` yields a unique index from 0 to 8 for each $3 \times 3$ sub-grid.

```python3
if num in rows[r]:
    return False

if num in cols[c]:
    return False

if num in boxes[box]:
    return False
```
Queries each set in $O(1)$ expected time. If `num` has already been seen in the current row, column, or box, the board is invalid, so it returns `False` immediately.

```python3
rows[r].add(num)
cols[c].add(num)
boxes[box].add(num)
```
Records `num` in the set for row `r`, column `c`, and box `box`.

```python3
return True
```
If all 81 cells are evaluated without returning `False`, the board satisfies all Sudoku rules.

---

## Dry Run

Consider Example 2 where an invalid duplicate `'8'` exists in the top-left box at cells $(0,0)$ and $(2,2)$:

```
board[0][0] = "8"
board[0][1] = "3"
...
board[2][2] = "8"
```

| Step | $(r, c)$ | `board[r][c]` | Calculated `box` | State Check Result | Action Taken |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | $(0, 0)$ | `"8"` | $(0 // 3)*3 + (0 // 3) = 0$ | Not in `rows[0]`, `cols[0]`, `boxes[0]` | Add `"8"` to `rows[0]`, `cols[0]`, `boxes[0]` |
| 2 | $(0, 1)$ | `"3"` | $(0 // 3)*3 + (1 // 3) = 0$ | Not in `rows[0]`, `cols[1]`, `boxes[0]` | Add `"3"` to `rows[0]`, `cols[1]`, `boxes[0]` |
| ... | ... | ... | ... | ... | ... |
| 19 | $(2, 0)$ | `"."` | — | Skipped (`"."`) | None |
| 20 | $(2, 1)$ | `"9"` | $(2 // 3)*3 + (1 // 3) = 0$ | Not in `rows[2]`, `cols[1]`, `boxes[0]` | Add `"9"` to `rows[2]`, `cols[1]`, `boxes[0]` |
| 21 | $(2, 2)$ | `"8"` | $(2 // 3)*3 + (2 // 3) = 0$ | `"8" in boxes[0]` is **`True`** | **Return `False`** |

The program terminates immediately at step 21 when `"8"` is detected in `boxes[0]`.

---

## Complexity

- **Time Complexity:** $O(1)$. The board dimension is fixed at $9 \times 9 = 81$ cells. The nested loop executes exactly 81 times. Each set lookup and insertion takes $O(1)$ average time.
- **Space Complexity:** $O(1)$. There are 27 sets created, and each set can store at most 9 distinct single-character strings. The memory footprint is strictly constant and bounded.

*(Note: If generalized to an $N \times N$ board, time complexity would be $O(N^2)$ and space complexity would be $O(N^2)$).*

---

## Edge Cases

- **Fully empty board:** Handled correctly. All cells are `"."`, the loop finishes, and it returns `True`.
- **Board with no numbers repeated anywhere:** Handled correctly. Returns `True`.
- **Duplicates in same row but different box:** Handled correctly by `num in rows[r]`.
- **Duplicates in same column but different box:** Handled correctly by `num in cols[c]`.
- **Duplicates in same $3 \times 3$ box but different row/col:** Handled correctly by `num in boxes[box]`.

---

## Possible Improvements

The implementation is already optimal in asymptotic time and space complexity. However, micro-optimizations exist:

1. **Bitmasking instead of Hash Sets:**
   Because values are restricted to digits 1–9, an integer bitmask can replace each set. Set membership checks become bitwise AND operations (`(rows[r] >> num) & 1`), reducing memory overhead and set hashing overhead entirely.
2. **Consolidating `if` statements:**
   The three separate `if` checks can be combined into a single conditional statement:
   ```python3
   if num in rows[r] or num in cols[c] or num in boxes[box]:
       return False
   ```

---

_Generated by leetvault using gemini (gemini-flash-latest)_
