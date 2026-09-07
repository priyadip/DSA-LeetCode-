# 3499. Maximize Active Section with Trade I - Solution Analysis

## Problem Understanding
We are given a binary string `s` where `'1'` denotes an active section and `'0'` an inactive one. We may perform **at most one trade**: first, choose a contiguous block of `'1'`s that is surrounded by `'0'`s (in the string augmented with a `'1'` at both ends) and flip it to `'0'`s; second, choose a contiguous block of `'0'`s that is surrounded by `'1'`s in the resulting string and flip it to `'1'`s. The augmented `'1'`s do not count toward the final answer. We need the maximum possible number of `'1'`s in `s` after the optimal trade. The length of `s` is up to `10^5`, so an `O(n)` or `O(n log n)` solution is required.

## Approach
The solution uses **run-length encoding (RLE)** to compress the string into alternating runs of `'0'`s and `'1'`s. The key insight is that a valid trade must select an **interior `'1'`-run** (one that has a `'0'`-run on both sides in the augmented string) to flip to `'0'`s, which merges its two neighboring `'0'`-runs. The best `'0'`-run to flip to `'1'`s in the second step is either this newly merged `'0'`-run or the largest `'0'`-run elsewhere that is not adjacent to the chosen `'1'`-run. By precomputing the top three `'0'`-run lengths, each interior `'1'`-run can be evaluated in `O(1)` time, yielding an overall `O(n)` algorithm.

## Algorithm
1. **Run-length encoding**: Scan `s` and build a list `runs` of `[char, length]` for each maximal contiguous block.
2. **Collect zero runs and interior one runs**: Traverse `runs`:
   - Accumulate `total_ones` (sum of lengths of `'1'` runs).
   - Store lengths of all `'0'` runs in array `Z`.
   - For each `'1'` run that is not the first or last run (i.e., has a `'0'` run on both sides), record its length `A` and the index of the left `'0'` run in `Z` (which is `len(Z)-1` at that moment) into `interior`.
3. If `interior` is empty, no valid trade exists → return `total_ones`.
4. **Find top three zero runs**: Iterate over `Z` and maintain the three largest `(length, index)` pairs in `top3`.
5. **Evaluate each interior one run**: For each `(A, left_idx)` in `interior`:
   - `right_idx = left_idx + 1`.
   - `gain_merged = Z[left_idx] + Z[right_idx]` (net gain from flipping the merged zero block; the `A` ones lost are regained inside the merged block).
   - `best_other` = largest `Z[idx]` where `idx` not in `{left_idx, right_idx}` (using `top3`).
   - `gain_sep = best_other - A` (net gain from flipping a separate zero block; the `A` ones are lost and not regained).
   - Update `max_gain = max(max_gain, gain_merged, gain_sep)`.
6. Return `total_ones + max_gain`.

## Line-by-Line Explanation
- `runs = []` / loop over `ch in s`: Build run-length encoding by extending the last run if the character matches, otherwise appending a new run.
- `Z = []`, `interior = []`, `total_ones = 0`: Initialize containers for zero-run lengths, interior one-run descriptors, and total count of `'1'`s.
- Loop over `enumerate(runs)`:
  - If `ch == '1'`: add `ln` to `total_ones`. If the run is interior (`0 < i < len(runs)-1`), the left zero run is the last element added to `Z`; record `(ln, len(Z)-1)` in `interior`.
  - Else (`ch == '0'`): append `ln` to `Z`.
- `if not interior: return total_ones`: No interior one-run means no valid trade.
- `top3 = [(0, -1), (0, -1), (0, -1)]` / loop over `enumerate(Z)`: Maintain the three largest zero runs with their indices for quick exclusion of the two adjacent runs.
- `max_gain = 0` / loop over `interior`:
  - `right_idx = left_idx + 1` (zero runs alternate with one runs).
  - `gain_merged = Z[left_idx] + Z[right_idx]`: length of the merged zero block after flipping the one-run.
  - `best_other`: first entry in `top3` whose index is neither `left_idx` nor `right_idx`.
  - `gain_sep = best_other - A`: net gain from flipping a separate zero block.
  - `max_gain = max(max_gain, gain_merged, gain_sep)`.
- `return total_ones + max_gain`: Final answer.

## Dry Run
Example: `s = "0100"` (Example 2).

**Phase 1: Build runs**
| Step | ch | runs after |
|------|----|------------|
| 1 | '0' | [['0',1]] |
| 2 | '1' | [['0',1], ['1',1]] |
| 3 | '0' | [['0',1], ['1',1], ['0',1]] |
| 4 | '0' | [['0',1], ['1',1], ['0',2]] |

**Phase 2: Build Z, interior, total_ones**
| i | ch | ln | Z before | interior before | total_ones before | Action |
|---|----|----|----------|-----------------|-------------------|--------|
| 0 | '0' | 1 | [] | [] | 0 | Z=[1] |
| 1 | '1' | 1 | [1] | [] | 0 | total_ones=1; interior=[(1,0)] |
| 2 | '0' | 2 | [1] | [(1,0)] | 1 | Z=[1,2] |

Result: `Z=[1,2]`, `interior=[(1,0)]`, `total_ones=1`.

**Phase 3: Build top3 from Z**
| idx | length | top3 after |
|-----|--------|------------|
| 0 | 1 | [(1,0), (0,-1), (0,-1)] |
| 1 | 2 | [(2,1), (1,0), (0,-1)] |

**Phase 4: Evaluate interior**
| A | left_idx | right_idx | gain_merged | best_other | gain_sep | max_gain |
|---|----------|-----------|-------------|------------|----------|----------|
| 1 | 0 | 1 | 1+2=3 | 0 (only dummy left) | -1 | 3 |

Return `1 + 3 = 4`. ✅

## Complexity
- **Time**: `O(n)`. Each of the four loops (building runs, scanning runs, building top3, evaluating interior) processes at most `n` elements. All operations inside loops are `O(1)`.
- **Space**: `O(n)`. The `runs`, `Z`, and `interior` lists can each grow to `O(n)` in the worst case (alternating characters). `top3` is constant size.

## Edge Cases
- **No interior one-run** (e.g., `s = "01"`, `s = "111"`, `s = "000"`): `interior` empty → returns `total_ones` (correct, no valid trade).
- **All zeros**: `total_ones = 0`, `interior` empty → returns `0`.
- **Multiple interior one-runs** (e.g., `s = "01010"`): Each is evaluated; the best gain is chosen.
- **Large `n` (10^5)**: Linear time and space fit comfortably.
- **Trade not beneficial**: `max_gain` stays `0` (since `gain_merged ≥ 0` and `gain_sep` may be negative) → returns original `total_ones`, correctly modeling "at most one trade".

## Possible Improvements
The solution is already optimal in asymptotic complexity (`O(n)` time, `O(n)` space) for the given constraints. A minor space optimization would be to compute runs on the fly in a single pass without storing the full `runs` list, but the current approach is clear and the `O(n)` space is acceptable. The manual top-3 maintenance is efficient and avoids heap overhead. No correctness issues or significant redundancies are present.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
