# 853. Car Fleet - Solution Analysis

## Problem Understanding
We are given `n` cars with unique starting positions `position[i]` (miles from start) and speeds `speed[i]` (mph), all moving toward a common `target` mile. Cars cannot overtake; a faster car catching a slower car (or fleet) merges into it, forming a fleet that moves at the slower speed. A fleet is one or more cars driving together. If a car catches a fleet exactly at `target`, it counts as part of that fleet. Return the number of distinct fleets that arrive at `target`. Constraints: `n ≤ 10⁵`, so an `O(n log n)` solution is required; positions are unique and strictly less than `target`.

## Approach
**Pattern:** Monotonic Stack / Greedy with Sorting.  
**Why it fits:** The relative order of cars never changes (no passing). Processing cars from the one closest to `target` backward lets us know the arrival time of the fleet immediately ahead. A car forms a new fleet *only* if it arrives strictly later than the fleet ahead; otherwise it merges into that fleet. The stack maintains the arrival times of fleets that have not been absorbed by cars behind them.  
**Brute force:** Simulate each car's movement step by step or check all pairs for collisions – `O(n²)` or worse, infeasible for `n=10⁵`.  
**Key insight:** A car's fate is decided solely by comparing its unimpeded arrival time with the arrival time of the fleet directly in front of it.

## Algorithm
1. Pair each car's `(position, speed)` and sort descending by `position` (closest to `target` first).
2. Initialize an empty stack `stack` to store fleet arrival times.
3. For each car in sorted order:
   - Compute `time = (target - position) / speed` (float).
   - If `stack` is empty **or** `time > stack[-1]`: this car cannot catch the fleet ahead (or there is none), so it forms a new fleet → push `time` onto `stack`.
   - Else (`time ≤ stack[-1]`): this car catches up to the fleet ahead before or at `target` → it merges, do nothing.
4. Return `len(stack)` (number of fleets).

## Line-by-Line Explanation
- `cars = sorted(zip(position, speed), reverse=True)`: Creates a list of `(pos, spd)` tuples sorted by `pos` descending. `reverse=True` on tuples sorts by the first element (position) descending, which is exactly the order from nearest to farthest from `target`.
- `stack = []`: Stack that will hold the arrival times of the fleets formed so far (from the front of the line backward).
- `for pos, spd in cars:`: Iterates cars starting with the one closest to `target`.
- `time = (target - pos) / spd`: Computes the time this car would take to reach `target` if it drove unimpeded.
- `if not stack or time > stack[-1]:`: Checks whether there is no fleet ahead yet, or this car's arrival time is *strictly greater* than the fleet immediately ahead. In both cases the car cannot merge into that fleet.
- `stack.append(time)`: Records this car as a new fleet leader; its arrival time becomes the benchmark for cars behind it.
- `return len(stack)`: The stack size equals the number of distinct fleets that reach `target`.

## Dry Run
Example 1: `target = 12`, `position = [10,8,0,5,3]`, `speed = [2,4,1,1,3]`

Sorted cars (pos, spd): `(10,2)`, `(8,4)`, `(5,1)`, `(3,3)`, `(0,1)`  
Times: `1.0`, `1.0`, `7.0`, `3.0`, `12.0`

| Step | pos | spd | time | stack before | Condition `time > stack[-1]` | Action | stack after |
|------|-----|-----|------|--------------|------------------------------|--------|-------------|
| 1    | 10  | 2   | 1.0  | []           | true (empty)                 | push   | [1.0]       |
| 2    | 8   | 4   | 1.0  | [1.0]        | false (1.0 > 1.0 is false)   | merge  | [1.0]       |
| 3    | 5   | 1   | 7.0  | [1.0]        | true (7.0 > 1.0)             | push   | [1.0, 7.0]  |
| 4    | 3   | 3   | 3.0  | [1.0, 7.0]   | false (3.0 > 7.0 false)      | merge  | [1.0, 7.0]  |
| 5    | 0   | 1   | 12.0 | [1.0, 7.0]   | true (12.0 > 7.0)            | push   | [1.0, 7.0, 12.0] |

Result: `len(stack) = 3` ✓

## Complexity
- **Time:** `O(n log n)` – sorting `n` cars dominates; the single pass is `O(n)`.
- **Space:** `O(n)` – the `cars` list and the `stack` each hold up to `n` elements.

## Edge Cases
- **Single car (`n=1`):** Stack gets one time, returns 1. Correct.
- **All cars same speed:** Times strictly increase as position decreases (farther cars take longer). Each `time > stack[-1]` holds, so every car forms its own fleet. Correct (they never catch up).
- **Cars merging exactly at `target`:** `time == stack[-1]` triggers the `else` branch (merge). Matches problem statement: "If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet."
- **Maximum constraints (`n=10⁵`):** `O(n log n)` sorting and `O(n)` memory are well within limits.
- **Already sorted input:** Sorting still runs but cost is acceptable; no early-exit optimization needed.

## Possible Improvements
The solution is already optimal for the given constraints.  
- Time complexity `O(n log n)` is optimal because any comparison-based solution must sort by position (or use a linear-time sort like counting sort if `target ≤ 10⁶`, but `target` can be up to `10⁶` and `n` up to `10⁵`, so `O(n log n)` is standard and fast enough).  
- Space `O(n)` is optimal for the stack approach.  
- Variable names (`cars`, `stack`, `time`) are clear and idiomatic.  
- No redundant passes or structures.  
- One trivial stylistic note: `sorted(zip(position, speed), key=lambda x: x[0], reverse=True)` makes the sort key explicit, but the current tuple sort is correct and concise.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
