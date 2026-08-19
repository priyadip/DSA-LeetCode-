# 1386. Cinema Seat Allocation - Solution Analysis

## Problem Understanding
We have `n` rows of 10 seats each. Some seats are reserved (given as `[row, seat]` pairs). A four-person group must occupy one of three specific contiguous blocks in a single row: seats 2‑5 (left), 4‑7 (middle), or 6‑9 (right). Blocks cannot overlap (each seat used at most once). We need the maximum number of groups that can be seated.  
Constraints: `n` up to 10⁹, but reserved seats list length ≤ 10⁴. This rules out iterating over all rows; only rows that actually have reservations need individual inspection. Rows without any reservations can always accommodate two groups (left and right blocks).

## Approach
**Pattern:** Greedy with bitmask and hash map.  
**Why it fits:** Rows are independent. For a row with no reservations we can always place two groups (left and right). For rows with reservations we only need to check which of the three blocks are completely free. Because left and right blocks do not overlap, they can be used simultaneously, giving a maximum of two groups per row. If both are not free, at most one of the three blocks can be used (any two blocks overlap).  
**Brute force** would iterate all `n` rows (impossible for `n=10⁹`). The chosen approach processes only rows that appear in `reservedSeats` (≤10⁴) and adds `2` for every other row in O(1).  
**Key insight:** A row can host at most two groups, and that happens exactly when both the left (2‑5) and right (6‑9) blocks are free; otherwise it can host at most one group if any of the three blocks is free.

## Algorithm
1. Build a dictionary `rows` mapping each row number to a bitmask of its reserved seats (bit `s` set if seat `s` is reserved).
2. Initialise answer `ans = 2 * (n - len(rows))` – two groups for every row without reservations.
3. Define bitmasks for the three blocks:  
   `left = (1<<2)|(1<<3)|(1<<4)|(1<<5)` (seats 2‑5)  
   `mid  = (1<<4)|(1<<5)|(1<<6)|(1<<7)` (seats 4‑7)  
   `right= (1<<6)|(1<<7)|(1<<8)|(1<<9)` (seats 6‑9)
4. For each row's mask:
   - If `mask & left == 0` **and** `mask & right == 0` → both side blocks free → add 2.
   - Else if `mask & left == 0` **or** `mask & mid == 0` **or** `mask & right == 0` → at least one block free → add 1.
   - Else add 0.
5. Return `ans`.

## Line-by-Line Explanation
- `rows = {}`: dictionary to accumulate reserved seats per row.
- `for r, s in reservedSeats:`: iterate over each reserved seat.
- `rows[r] = rows.get(r, 0) | (1 << s)`: set bit `s` in the mask for row `r` (bits 1‑10 correspond to seats 1‑10).
- `ans = 2 * (n - len(rows))`: each row not in `rows` has no reservations → can always seat two groups (left and right).
- `left = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)`: bitmask for seats 2,3,4,5.
- `mid = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)`: bitmask for seats 4,5,6,7.
- `right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)`: bitmask for seats 6,7,8,9.
- `for mask in rows.values():`: examine each row that has at least one reservation.
- `if not (mask & left) and not (mask & right):`: both left and right blocks completely free.
- `ans += 2`: we can place two groups in this row.
- `elif not (mask & left) or not (mask & mid) or not (mask & right):`: at least one of the three blocks is free (but not both left and right simultaneously, otherwise the first `if` would have triggered).
- `ans += 1`: we can place exactly one group.
- `return ans`: total maximum groups.

## Dry Run
Example 1: `n = 3`, `reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]`

| Step | Row | Reserved Seats | Mask (bits) | left free? | mid free? | right free? | Action |
|------|-----|----------------|-------------|------------|-----------|-------------|--------|
| init | –   | –              | –           | –          | –         | –           | `ans = 2*(3-3)=0` |
| 1    | 1   | 2,3,8          | bits 2,3,8  | False (2,3) | True      | False (8)   | `elif` true → `ans=1` |
| 2    | 2   | 6              | bit 6       | True       | False (6) | False (6)   | `elif` true → `ans=2` |
| 3    | 3   | 1,10           | bits 1,10   | True       | True      | True        | `if` true → `ans=4` |

Final `ans = 4`, matches expected output.

## Complexity
- **Time:** O(m) where m = `len(reservedSeats)` (≤ 10⁴). Building the dictionary and iterating over its values each take O(m). All other operations are O(1).
- **Space:** O(m) for the dictionary storing at most one entry per distinct row with reservations.

## Edge Cases
- **Rows without reservations:** Handled by the initial `2 * (n - len(rows))`. Since `reservedSeats.length ≥ 1`, there is at least one reserved seat, but `n` can be much larger.
- **All seats in a row reserved:** Mask has many bits; none of the three blocks are free → adds 0.
- **Reservations only in seats 1 and 10:** Both left and right blocks free → adds 2 (correct, seats 1 and 10 are not used by any block).
- **Reservation in seat 5 only:** Left and middle blocked, right free → `elif` adds 1.
- **Reservation in seats 4 and 7:** Left blocked (4), middle blocked (4,7), right blocked (7) → adds 0.
- **Multiple valid answers:** The greedy choice (prefer two groups when left and right free, otherwise one) is optimal because max per row is 2 and left/right are the only non‑overlapping pair.

## Possible Improvements
The solution is already optimal for the given constraints: O(m) time and space, which is the best possible since we must read all reserved seats. Variable names are clear (`left`, `mid`, `right`, `mask`). No redundant passes or structures. A minor stylistic tweak could pre‑compute `left|right` to check the two‑group condition with a single `&`, but the current code is perfectly readable and efficient.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
