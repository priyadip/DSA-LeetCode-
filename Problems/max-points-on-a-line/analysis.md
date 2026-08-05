# 149. Max Points on a Line - Solution Analysis

## Problem Understanding

The problem asks for the maximum number of points in a 2D plane that lie on a single straight line.

Key constraints:
- $1 \le N \le 300$, where $N$ is the number of points.
- Coordinates $x_i, y_i$ range from $-10^4$ to $10^4$.
- All points are guaranteed to be unique according to the constraints.

Because $N \le 300$, an $O(N^2)$ time complexity algorithm is well within the execution time limit.

## Approach

This solution uses an **Anchor Point + Hash Map (Slope Canonicalization)** pattern:

1. **Slope Equivalence**: Two points $(x_i, y_i)$ and $(x_j, y_j)$ form a line with slope $\frac{\Delta y}{\Delta x} = \frac{y_j - y_i}{x_j - x_i}$. Any third point that forms the same slope with $(x_i, y_i)$ lies on the exact same line.
2. **Avoiding Floating-Point Precision Issues**: Floating-point division (`dy / dx`) suffers from precision issues and cannot reliably distinguish nearly parallel lines. Instead, the slope is stored as a reduced fraction pair $(\frac{\Delta x}{\gcd(\Delta x, \Delta y)}, \frac{\Delta y}{\gcd(\Delta x, \Delta y)})$.
3. **Iterative Anchor**: By picking each point $i$ as an anchor and counting the slopes to all subsequent points $j > i$, we find the maximum number of collinear points sharing that anchor.

## Algorithm

1. If $N \le 2$, return $N$ immediately.
2. Iterate `i` from `0` to $N - 1$ as the fixed anchor point.
3. For each anchor `i`, initialize a hash map `slope_map`, an `overlap` counter, and `curr_max = 0`.
4. Iterate `j` from `i + 1` to $N - 1$:
   - Calculate $\Delta x = x_j - x_i$ and $\Delta y = y_j - y_i$.
   - If $\Delta x = 0$ and $\Delta y = 0$, increment `overlap` (handles duplicate points).
   - Compute `gcd_val = gcd(dx, dy)`.
   - Reduce the pair to `(dx // gcd_val, dy // gcd_val)` and increment its count in `slope_map`.
   - Update `curr_max` with the maximum count seen so far for anchor `i`.
5. Update global `max_points` with `curr_max + overlap + 1` (the $+1$ accounts for anchor point `i`).
6. Return `max_points`.

## Line-by-Line Explanation

```python
class Solution(object):
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
```
Handles base cases directly: 0, 1, or 2 points are always collinear.

```python
        max_points = 0
```
Tracks the global maximum number of collinear points found across all anchor iterations.

```python
        for i in range(len(points)):
            slope_map = defaultdict(int)
            overlap = 0
            curr_max = 0
```
Outer loop selects point `i` as the anchor. `slope_map` maps canonicalized slope tuples to counts. `overlap` tracks identical points, and `curr_max` stores the highest frequency of any single slope from anchor `i`.

```python
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
```
Inner loop considers all subsequent points `j`. Calculates displacement vector $(\Delta x, \Delta y)$.

```python
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
```
Handles duplicate coordinates if present.

```python
                gcd_val = self.gcd(dx, dy)
                slope = (dx // gcd_val, dy // gcd_val)
                slope_map[slope] += 1
                curr_max = max(curr_max, slope_map[slope])
```
Computes the greatest common divisor to reduce $(\Delta x, \Delta y)$ to its simplest integer ratio `slope`. Updates frequency in `slope_map` and tracks `curr_max`.

```python
            max_points = max(max_points, curr_max + overlap + 1)
```
After checking all $j > i$, computes total collinear points for anchor `i` (slope matches + duplicate points + anchor point itself) and updates `max_points`.

```python
        return max_points
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
```
Implements Euclidean GCD. In Python, because `%` preserves the sign of the divisor `b`, this custom GCD produces negative GCD values when $b < 0$. This implicitly normalizes directional vectors (e.g., $(-1, -1)$ and $(1, 1)$ both reduce to $(1, 1)$).

## Dry Run

Trace for `points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]` ($N=6$):

### Anchor $i = 0$ at `[1,1]`:

| $j$ | Point | $\Delta x, \Delta y$ | $\text{gcd}(\Delta x, \Delta y)$ | Canonical Slope | `slope_map` state | `curr_max` |
|---|---|---|---|---|---|---|
| 1 | `[3,2]` | $(2, 1)$ | $1$ | $(2, 1)$ | `{(2,1): 1}` | 1 |
| 2 | `[5,3]` | $(4, 2)$ | $2$ | $(2, 1)$ | `{(2,1): 2}` | 2 |
| 3 | `[4,1]` | $(3, 0)$ | $3$ | $(1, 0)$ | `{(2,1): 2, (1,0): 1}` | 2 |
| 4 | `[2,3]` | $(1, 2)$ | $1$ | $(1, 2)$ | `{(2,1): 2, (1,0): 1, (1,2): 1}` | 2 |
| 5 | `[1,4]` | $(0, 3)$ | $3$ | $(0, 1)$ | `{(2,1): 2, ...}` | 2 |

`max_points` = $\max(0, 2 + 0 + 1) = 3$.

---

### Anchor $i = 1$ at `[3,2]`:

| $j$ | Point | $\Delta x, \Delta y$ | $\text{gcd}(\Delta x, \Delta y)$ | Canonical Slope | `slope_map` state | `curr_max` |
|---|---|---|---|---|---|---|
| 2 | `[5,3]` | $(2, 1)$ | $1$ | $(2, 1)$ | `{(2,1): 1}` | 1 |
| 3 | `[4,1]` | $(1, -1)$ | $-1$ | $(-1, 1)$ | `{(2,1): 1, (-1,1): 1}` | 1 |
| 4 | `[2,3]` | $(-1, 1)$ | $1$ | $(-1, 1)$ | `{(2,1): 1, (-1,1): 2}` | 2 |
| 5 | `[1,4]` | $(-2, 2)$ | $2$ | $(-1, 1)$ | `{(2,1): 1, (-1,1): 3}` | 3 |

`max_points` = $\max(3, 3 + 0 + 1) = 4$.

Iterations $i = 2, 3, 4, 5$ run similarly and yield counts $\le 4$. Final answer returned is **4**.

## Complexity

- **Time Complexity**: $\mathcal{O}(N^2 \log M)$, where $N$ is the number of points and $M = \max(|x|, |y|)$ is the coordinate boundary magnitude ($10^4$). For each pair of points, Euclidean GCD takes $\mathcal{O}(\log M)$ steps. With $N \le 300$, $N^2 \approx 90,000$ iterations, running in a few milliseconds.
- **Space Complexity**: $\mathcal{O}(N)$. The `slope_map` stores at most $N - 1$ distinct slope entries for any single anchor point.

## Edge Cases

- **$N \le 2$**: Handled by the early check at line 3.
- **Vertical Lines ($\Delta x = 0$)**: Handled correctly; $\gcd(0, \Delta y) = \Delta y$, yielding slope tuple `(0, 1)`.
- **Horizontal Lines ($\Delta y = 0$)**: Handled correctly; $\gcd(\Delta x, 0) = \Delta x$, yielding slope tuple `(1, 0)`.
- **Negative Displacements**: Python's floor division `//` combined with the sign of `%` in custom `gcd` handles negative slopes, ensuring anti-parallel vectors map to identical slope tuples.

## Possible Improvements

1. **Use Standard Library `math.gcd`**: Custom Python `gcd` implementation is executed in interpreted bytecode. Standard library `math.gcd` is written in C and significantly faster.
2. **Explicit Canonicalization**: Relying on Python's modulo behavior on negative numbers for sign normalization in `self.gcd` is obscure and non-portable. Explicitly normalizing sign (e.g., ensuring $\Delta y > 0$, or $\Delta y == 0$ and $\Delta x > 0$) is clearer and less fragile.
3. **Early Loop Exit**: If $N - i \le \text{max\_points}$, no subsequent anchor point $i$ can produce a larger collinear set than `max_points`. Terminating the outer loop early when this condition holds avoids redundant work.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
