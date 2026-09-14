# 835. Image Overlap - Solution Analysis

## Problem Understanding
We are given two n×n binary matrices `img1` and `img2`. We may translate one image by any integer offset (dr, dc) – sliding it up/down/left/right – and then overlay it on the other. Overlap is the number of positions where both images have a `1` after translation; bits shifted outside the matrix are discarded. The task is to return the maximum possible overlap. The matrix size is at most 30×30, so an O(n⁴) brute force is feasible, but a more efficient method exploits sparsity of `1`s.

## Approach
The solution uses **translation vector counting** (a form of coordinate hashing).  
Brute force would try all (2n−1)² translations and compute overlap in O(n²) each, giving O(n⁴). Instead, we observe that each pair of `1` bits – one from `img1` and one from `img2` – defines a unique translation vector `(dr, dc) = (r₂−r₁, c₂−c₁)` that aligns those two bits. The translation that aligns the most pairs yields the maximum overlap. We count frequencies of all such vectors; the highest frequency is the answer. This reduces work to O(k₁·k₂) where k₁, k₂ are the numbers of `1`s, which is optimal for sparse matrices and never worse than O(n⁴).

**Key insight:** The translation that maximizes overlap is exactly the translation vector that occurs most often among all pairs of `1` coordinates from the two images.

## Algorithm
1. Let `n = len(img1)`.
2. Collect coordinates of all `1`s in `img1` into list `ones1`.
3. Collect coordinates of all `1`s in `img2` into list `ones2`.
4. Initialize a dictionary `count` mapping translation vectors `(dr, dc)` to their frequency.
5. For each `(r1, c1)` in `ones1`:
   For each `(r2, c2)` in `ones2`:
       Compute `dr = r2 - r1`, `dc = c2 - c1`.
       Increment `count[(dr, dc)]`.
6. Return the maximum value in `count`, or `0` if `count` is empty.

## Line-by-Line Explanation
- `n = len(img1)`: matrix dimension.
- `ones1 = []` / `ones2 = []`: lists to store coordinates of `1`s.
- Double loop over `r, c`: scans every cell; if `img1[r][c] == 1` appends `(r, c)` to `ones1`; similarly for `img2`.
- `count = defaultdict(int)`: dictionary that defaults missing keys to `0`, used to tally translation vectors.
- Nested loops over `ones1` and `ones2`: enumerates every pair of `1`s across the two images.
- `dr = r2 - r1; dc = c2 - c1`: translation needed to move the `1` from `img1` onto the `1` from `img2`.
- `count[(dr, dc)] += 1`: records that this translation aligns one more pair.
- `return max(count.values(), default=0)`: the most frequent translation gives the maximum overlap; `default=0` handles the case where there are no `1`s in either image.

## Dry Run
Example 1:
```
img1 = [[1,1,0],
        [0,1,0],
        [0,1,0]]
img2 = [[0,0,0],
        [0,1,1],
        [0,0,1]]
```
`ones1 = [(0,0), (0,1), (1,1), (2,1)]`  
`ones2 = [(1,1), (1,2), (2,2)]`

| Step | r1 | c1 | r2 | c2 | dr | dc | count[(dr,dc)] after |
|------|----|----|----|----|----|----|----------------------|
| 1    | 0  | 0  | 1  | 1  | 1  | 1  | (1,1):1 |
| 2    | 0  | 0  | 1  | 2  | 1  | 2  | (1,2):1 |
| 3    | 0  | 0  | 2  | 2  | 2  | 2  | (2,2):1 |
| 4    | 0  | 1  | 1  | 1  | 1  | 0  | (1,0):1 |
| 5    | 0  | 1  | 1  | 2  | 1  | 1  | (1,1):2 |
| 6    | 0  | 1  | 2  | 2  | 2  | 1  | (2,1):1 |
| 7    | 1  | 1  | 1  | 1  | 0  | 0  | (0,0):1 |
| 8    | 1  | 1  | 1  | 2  | 0  | 1  | (0,1):1 |
| 9    | 1  | 1  | 2  | 2  | 1  | 1  | (1,1):3 |
| 10   | 2  | 1  | 1  | 1  | -1 | 0  | (-1,0):1 |
| 11   | 2  | 1  | 1  | 2  | -1 | 1  | (-1,1):1 |
| 12   | 2  | 1  | 2  | 2  | 0  | 1  | (0,1):2 |

Maximum count is `3` for translation `(1,1)`, which matches the example output.

## Complexity
- **Time:** O(k₁·k₂) where k₁ = number of `1`s in `img1`, k₂ = number of `1`s in `img2`. In the worst case (all `1`s) k₁ = k₂ = n², so O(n⁴). With n ≤ 30 this is at most 810,000 iterations, well within limits.
- **Space:** O(k₁ + k₂ + T) where T is the number of distinct translation vectors. T ≤ (2n−1)² = O(n²). The dictionary `count` holds at most O(n²) entries.

## Edge Cases
- **All zeros:** `ones1` and `ones2` are empty → `count` stays empty → `max(..., default=0)` returns `0`.
- **Single `1` in both at same position:** translation `(0,0)` gets count `1` → returns `1`.
- **Multiple translations with same maximum count:** `max` returns that count (any is fine).
- **Negative translations:** `dr, dc` can be negative; dictionary keys handle them correctly.
- **Maximum n = 30:** loops run within time; memory for dictionary is at most ~3600 entries.

## Possible Improvements
The solution is already optimal for the given constraints. For dense matrices it matches the brute-force O(n⁴) bound, but for sparse matrices it is significantly faster. No asymptotic improvement is possible without changing the problem (e.g., using FFT-based convolution would be overkill). The code is clean; minor stylistic changes (e.g., using list comprehensions to build `ones1`/`ones2`) would not affect performance.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
