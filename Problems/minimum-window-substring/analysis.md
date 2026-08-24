# 76. Minimum Window Substring - Solution Analysis

## Problem Understanding
Given strings `s` (length m) and `t` (length n), find the shortest contiguous substring of `s` that contains every character of `t` with at least the same frequency (duplicates matter). Return empty string if impossible. Constraints: 1 ≤ m, n ≤ 10⁵, characters are A-Z and a-z. The O(m+n) follow-up expectation rules out O(m·n) or sorting-based approaches.

## Approach
**Sliding Window with Frequency Array** — The algorithm maintains a window `[left, right]` on `s` and a 52-element array `need` where `need[i] > 0` means the window still requires that many of character `i`, `need[i] ≤ 0` means the window has enough (or extra). A single counter `required` tracks total characters still needed. Expand `right` until `required == 0` (window covers `t`), then contract `left` while `required == 0` to minimise the window, recording the best. This is the classic variable-size sliding window for "minimum substring covering a multiset".

Brute force would check all O(m²) substrings and validate each in O(n), giving O(m²n). The sliding window visits each character at most twice (once entering, once leaving), achieving O(m+n).

**Key insight:** A single signed frequency array (`need`) simultaneously encodes both the target counts (initial positive values) and the current window surplus/deficit (updated as the window moves), eliminating the need for separate `have` and `need` maps and a distinct "matches" check.

## Algorithm
1. If `len(t) > len(s)`, return `""`.
2. Map each letter to an index 0–51: `'a'–'z'` → 0–25, `'A'–'Z'` → 26–51.
3. Initialise `need[52]` with counts of each character in `t`.
4. Set `required = len(t)`, `left = 0`, `best_len = ∞`, `best_start = 0`.
5. For each `right` from 0 to `len(s)-1`:
   a. Decrement `need[idx(s[right])]`.
   b. If that character was still needed (`need[idx] ≥ 0` before decrement), decrement `required`.
   c. While `required == 0` (window is valid):
      i. Update `best_len` and `best_start` if current window is smaller.
      ii. Increment `need[idx(s[left])]` (remove left char from window).
      iii. If that character becomes needed again (`need[idx] > 0`), increment `required`.
      iv. Increment `left`.
6. Return `""` if `best_len` unchanged, else `s[best_start:best_start+best_len]`.

## Line-by-Line Explanation
- `if len(t) > len(s): return ""` — Early exit: `t` cannot fit in `s`.
- `def index(ch): ...` — Maps `'a'–'z'` to 0–25, `'A'–'Z'` to 26–51 using ASCII arithmetic.
- `need = [0] * 52` — Fixed-size frequency array for 52 possible letters.
- `for ch in t: need[index(ch)] += 1` — Populate required counts from `t`.
- `left = 0` — Left boundary of sliding window.
- `required = len(t)` — Total characters still needed to satisfy `t` (counts duplicates).
- `best_start = 0; best_len = float("inf")` — Track best window found.
- `for right, ch in enumerate(s):` — Expand window rightward one character at a time.
- `idx = index(ch)` — Index of incoming character.
- `if need[idx] > 0: required -= 1` — This character was still needed; one less required now.
- `need[idx] -= 1` — Add character to window (decrement need; negative means surplus).
- `while required == 0:` — Window covers `t`; try to shrink from left.
- `window_len = right - left + 1` — Current window size.
- `if window_len < best_len: best_len = window_len; best_start = left` — Record new minimum.
- `left_idx = index(s[left])` — Index of character leaving window.
- `need[left_idx] += 1` — Remove its contribution from window.
- `if need[left_idx] > 0: required += 1` — If it becomes needed again, window no longer valid.
- `left += 1` — Shrink window.
- `if best_len == float("inf"): return ""` — No valid window found.
- `return s[best_start:best_start + best_len]` — Return the minimum window substring.

## Dry Run
Example: `s = "ADOBECODEBANC"`, `t = "ABC"`

Initial `need`: A:1, B:1, C:1 (indices 26, 27, 28), others 0. `required = 3`.

| Step | right | ch  | idx | need before | required before | Action |
|------|-------|-----|-----|-------------|-----------------|--------|
| 1    | 0     | A   | 26  | A:1         | 3               | need[A]=0, required=2 |
| 2    | 1     | D   | 3   | D:0         | 2               | need[D]=-1 |
| 3    | 2     | O   | 14  | O:0         | 2               | need[O]=-1 |
| 4    | 3     | B   | 27  | B:1         | 2               | need[B]=0, required=1 |
| 5    | 4     | E   | 4   | E:0         | 1               | need[E]=-1 |
| 6    | 5     | C   | 28  | C:1         | 1               | need[C]=0, required=0 → enter shrink |
|      |       |     |     |             |                 | window [0,5] len=6, best=(0,6) |
|      |       |     |     | left=0 (A)  |                 | need[A]=1, required=1, left=1 → exit shrink |
| 7    | 6     | O   | 14  | O:-1        | 1               | need[O]=-2 |
| 8    | 7     | D   | 3   | D:-1        | 1               | need[D]=-2 |
| 9    | 8     | E   | 4   | E:-1        | 1               | need[E]=-2 |
| 10   | 9     | B   | 27  | B:0         | 1               | need[B]=-1 |
| 11   | 10    | A   | 26  | A:1         | 1               | need[A]=0, required=0 → enter shrink |
|      |       |     |     |             |                 | window [1,10] len=10, not better |
|      |       |     |     | left=1 (D)  |                 | need[D]=-1, left=2 |
|      |       |     |     | left=2 (O)  |                 | need[O]=-1, left=3 |
|      |       |     |     | left=3 (B)  |                 | need[B]=0, left=4 |
|      |       |     |     | left=4 (E)  |                 | need[E]=-1, left=5 |
|      |       |     |     | left=5 (C)  |                 | need[C]=1, required=1, left=6 → exit shrink |
| 12   | 11    | N   | 13  | N:0         | 1               | need[N]=-1 |
| 13   | 12    | C   | 28  | C:1         | 1               | need[C]=0, required=0 → enter shrink |
|      |       |     |     |             |                 | window [6,12] len=7, not better |
|      |       |     |     | left=6 (O)  |                 | need[O]=0, left=7 |
|      |       |     |     | left=7 (D)  |                 | need[D]=0, left=8 |
|      |       |     |     | left=8 (E)  |                 | need[E]=0, left=9 |
|      |       |     |     | left=9 (B)  |                 | need[B]=1, required=1, left=10 → exit shrink |

Final best: start=0, len=6 → `"ADOBEC"`? Wait, the example output is `"BANC"`. Let me re-check.

Actually, the example output is `"BANC"` which is at indices 9-12. My trace shows window [9,12] would be B A N C? Let me check indices: s = "ADOBECODEBANC"
Indices: 0:A, 1:D, 2:O, 3:B, 4:E, 5:C, 6:O, 7:D, 8:E, 9:B, 10:A, 11:N, 12:C

At step 13, right=12 (C). Window [6,12] is "ODEBANC" len 7. Shrinking:
left=6 (O) → need[O]=0
left=7 (D) → need[D]=0
left=8 (E) → need[E]=0
left=9 (B) → need[B]=1, required=1, left=10. So window [9,12] was valid before removing B? Wait, when left=9, window is [9,12] = "BANC". At that point need[B] was 0 (since we had two B's in window: index 3 and 9? No, index 3 was removed earlier when left moved from 3 to 4. Let me trace more carefully.

Actually, after step 11 shrink, left=6. Window [6,10] = "ODEBA". need: A:0, B:0, C:1 (since C at index 5 was removed), others negative. required=1.

Step 12: right=11 (N). need[N]=-1. required=1.
Step 13: right=12 (C). need[C] was 1, becomes 0, required=0. Window [6,12] = "ODEBANC". Shrink:
left=6 (O): need[O] -2→-1
left=7 (D): need[D] -2→-1
left=8 (E): need[E] -2→-1
left=9 (B): need[B] -1→0 (still valid)
left=10 (A): need[A] 0→1, required=1, left=11. So window [9,12] = "BANC" was valid and length 4. But best_len was 6 from first window. When left=9, window_len = 12-9+1 = 4 < 6, so best should update to (9,4). My trace missed that update inside the while loop. The code does update at each iteration of while loop. So best becomes (9,4). Correct.

## Complexity
- **Time:** O(m + n) — Building `need` takes O(n). The `for` loop runs m times; each character enters the window once (right pointer) and leaves at most once (left pointer). All operations inside are O(1).
- **Space:** O(1) — The `need` array is fixed size 52, independent of input size. Only a few integer variables are used.

## Edge Cases
- **`len(t) > len(s)`**: Handled by early return.
- **`t` has characters not in `s`**: `required` never reaches 0, returns `""`.
- **Duplicates in `t`** (e.g., `t="aa"`): `required` starts at 2; both `a`s must be covered before shrinking.
- **Case sensitivity**: Mapping distinguishes uppercase/lowercase correctly.
- **Entire `s` is the answer** (e.g., `s="a", t="a"`): Window expands to cover, shrinks to same, recorded correctly.
- **Multiple valid windows**: The unique-answer guarantee means we don't need tie-breaking logic; first minimum found is the only one.

## Possible Improvements
The solution is already optimal in time O(m+n) and space O(1) for the given constraints. The fixed 52-element array is faster than a dictionary for this alphabet. Variable names are clear (`need`, `required`, `left`, `right`). One minor readability improvement: the `index` function could be inlined or replaced with a precomputed `ord` lookup table for 128 ASCII chars to avoid the branch, but the branch is well-predicted and the gain is negligible. No material improvement needed.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
