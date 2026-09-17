# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum - Solution Analysis

## Problem Understanding
We are given an array `arr` of positive integers (1 ≤ arr[i] ≤ 1000) and a target sum. We must find two **non-overlapping** subarrays each summing exactly to `target` such that the sum of their lengths is minimized. If no such pair exists, return -1. The array length can be up to 10^5, so an O(n) or O(n log n) solution is required. All numbers are positive, which makes a sliding window viable for finding subarrays with a given sum.

## Approach
The solution combines **sliding window** (to enumerate all subarrays with sum = target in linear time) with **dynamic programming / prefix minimum** (to keep the best subarray length seen so far). Because all values are positive, a two-pointer window can maintain the current sum and shrink from the left when it exceeds the target. Whenever the window sum equals the target, we have a candidate subarray `[left, right]`. To pair it with an earlier non-overlapping subarray, we need the minimum length of any valid subarray ending **before** `left`. This prefix minimum is stored directly in the input array using a base encoding (`BASE = max(1001, n+2)`) that packs the original value and the best length into a single integer. The key insight: *the sliding window visits each valid subarray exactly once in increasing order of right endpoint, and the prefix minimum allows O(1) combination with the best earlier subarray.*

## Algorithm
1. **Initialize**  
   `n = len(arr)`, `INF = n + 1`, `BASE = max(1001, n + 2)`.  
   `left = 0`, `curr_sum = 0`, `ans = INF`.

2. **Iterate `right` from 0 to n-1**  
   a. **Decode** the original value at `arr[right]`:  
      `x = arr[right] // BASE` if `arr[right] >= BASE` else `arr[right]`.  
   b. **Expand window**: `curr_sum += x`.  
   c. **Shrink window** while `curr_sum > target`:  
      decode value at `left`, subtract from `curr_sum`, `left += 1`.  
   d. **Retrieve best length so far** (minimum length of a valid subarray ending at or before `right-1`):  
      `best = INF` if `right == 0` else `arr[right-1] % BASE`.  
   e. **If `curr_sum == target`**:  
      - `length = right - left + 1`.  
      - If `left > 0`, get `previous = arr[left-1] % BASE`; if `previous != INF`, update `ans = min(ans, previous + length)`.  
      - `best = min(best, length)`.  
   f. **Encode** current position: `arr[right] = x * BASE + best`.

3. **Return** `-1` if `ans == INF` else `ans`.

## Line-by-Line Explanation
- `n = len(arr)` – array length.
- `INF = n + 1` – sentinel larger than any possible subarray length.
- `BASE = max(1001, n + 2)` – base for packing; > max original value (1000) and > max possible length (n).
- `left = 0; curr_sum = 0; ans = INF` – sliding window pointers, current sum, answer.
- `for right in range(n):` – main loop, right endpoint of window.
- `if arr[right] >= BASE: x = arr[right] // BASE else: x = arr[right]` – retrieve original value (handles both raw and already-encoded entries).
- `curr_sum += x` – expand window to the right.
- `while curr_sum > target:` – shrink from left until sum ≤ target.
  - `if arr[left] >= BASE: value = arr[left] // BASE else: value = arr[left]` – decode left value.
  - `curr_sum -= value; left += 1` – remove leftmost element.
- `if right == 0: best = INF else: best = arr[right - 1] % BASE` – prefix minimum up to previous index (mod BASE extracts stored best length).
- `if curr_sum == target:` – found a valid subarray `[left, right]`.
  - `length = right - left + 1` – its length.
  - `if left > 0: previous = arr[left - 1] % BASE; if previous != INF: ans = min(ans, previous + length)` – combine with best subarray ending before `left`.
  - `best = min(best, length)` – update prefix minimum for this `right`.
- `arr[right] = x * BASE + best` – store original value and updated prefix minimum in one integer.
- `return -1 if ans == INF else ans` – final answer.

## Dry Run
Example 1: `arr = [3,2,2,4,3]`, `target = 3`.  
`n=5`, `INF=6`, `BASE=1001`.

| Step | right | left | curr_sum | x (decoded) | best (from right-1) | curr_sum==target? | length | previous (left-1) | ans | arr[right] after encode (x*BASE+best) |
|------|-------|------|----------|-------------|---------------------|-------------------|--------|-------------------|-----|---------------------------------------|
| 0    | 0     | 0    | 3        | 3           | INF                 | yes               | 1      | –                 | 6   | 3*1001 + 1 = 3004                     |
| 1    | 1     | 0    | 5        | 2           | 1 (3004%1001)       | no                | –      | –                 | 6   | 2*1001 + 1 = 2003                     |
| 2    | 2     | 1    | 4        | 2           | 1 (2003%1001)       | no                | –      | –                 | 6   | 2*1001 + 1 = 2003                     |
| 3    | 3     | 2    | 6        | 4           | 1 (2003%1001)       | no                | –      | –                 | 6   | 4*1001 + 1 = 4005                     |
| 4    | 4     | 4    | 3        | 3           | 1 (4005%1001)       | yes               | 1      | 1 (arr[3]%1001=1) | 2   | 3*1001 + 1 = 3004                     |

Final `ans = 2`, matches expected output.

## Complexity
- **Time**: O(n). Each element is added to `curr_sum` once and removed at most once; all other operations are O(1) per iteration.
- **Space**: O(1) auxiliary (the input array is modified in-place to store the DP values). If the input must remain unchanged, an extra array of size n would be needed, making it O(n) space.

## Edge Cases
- **No valid subarray** – `ans` stays `INF`, returns -1 (e.g., Example 3).
- **Only one valid subarray** – `previous` is always `INF` when a valid subarray is found, so `ans` never updates, returns -1.
- **Multiple overlapping candidates** – sliding window ensures each ending index is considered; prefix minimum guarantees non-overlap because we only combine with subarrays ending strictly before `left`.
- **Minimum length subarrays** – the prefix minimum always keeps the shortest valid subarray seen so far, which is optimal for minimizing the sum.
- **Large target** – window shrinks correctly because all numbers are positive; `curr_sum` can exceed target and we shrink until ≤ target.
- **Single element array** – loop runs once, `best = INF`, no pair possible, returns -1.

## Possible Improvements
- **Input modification**: The solution overwrites `arr`. If the caller expects `arr` unchanged, allocate a separate `best_len` array of size n (O(n) space) and store prefix minima there. This improves clarity and safety.
- **Variable naming**: `x`, `value`, `best`, `previous` are terse. More descriptive names (`val`, `left_val`, `best_len`, `prev_best`) would improve readability without changing logic.
- **BASE calculation**: `max(1001, n+2)` works because constraints guarantee `arr[i] ≤ 1000` and `best_len ≤ n`. A comment explaining the packing would help maintainability.
- The algorithm is already optimal in time (O(n)) and space (O(1) extra) for the given constraints. No asymptotic improvement is possible.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
