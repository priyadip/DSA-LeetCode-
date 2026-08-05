# 219. Contains Duplicate II - Solution Analysis

## Problem Understanding
The goal is to determine whether an integer array `nums` contains any duplicate values located at most $k$ indices apart. Specifically, we need to find if there exist two distinct indices $i$ and $j$ such that `nums[i] == nums[j]` and $|i - j| \le k$.

### Constraints
- $1 \le \text{nums.length} \le 10^5$: An $O(n^2)$ nested-loop comparison will result in a Time Limit Exceeded (TLE). We need a solution running in $O(n)$ or $O(n \log n)$ time.
- $-10^9 \le \text{nums}[i] \le 10^9$: Values fit within standard signed 32-bit integers, but their range is large, so direct array indexing (bucket indexing) is not feasible.
- $0 \le k \le 10^5$: If $k = 0$, the condition $|i - j| \le 0$ can never be satisfied for distinct indices $i \neq j$, so the answer must always be `False`.

## Approach
This solution uses a **Hash Map** (dictionary) to track the most recent index where each number appeared.

A simple hash set can check for duplicates across the entire array, but here the distance between indices matters. By mapping each value `x` to its *last seen index* `last[x]`, we only ever need to check the gap between the current index `i` and `last[x]`. 

If `i - last[x] <= k`, we immediately return `True`. If `i - last[x] > k`, we overwrite `last[x] = i`. Overwriting is correct because any future occurrence of `x` at index $i' > i$ will be closer to $i$ than to `last[x]`, making $i$ the only relevant index going forward.

## Algorithm
1. Initialize an empty hash map `last`.
2. Iterate through `nums` with current index `i` and value `x`.
3. Check if `x` is in `last` and whether `i - last[x] <= k`.
4. If both conditions are true, return `True`.
5. Otherwise, set or update `last[x] = i`.
6. If the loop finishes without returning `True`, return `False`.

## Line-by-Line Explanation
```python3
last = {}
```
Initializes an empty dictionary `last` to map each distinct number in `nums` to its most recently encountered index.

```python3
for i, x in enumerate(nums):
```
Uses `enumerate` to iterate through `nums`, providing the index `i` and the element `x` at each step.

```python3
if x in last and i - last[x] <= k:
    return True
```
Checks if `x` has been seen previously. If it exists in `last`, Python's `and` operator evaluates short-circuit style, checking if the distance `i - last[x]` is within the threshold `k`. If so, a valid pair has been found and execution terminates immediately with `True`.

```python3
last[x] = i
```
Updates the entry for `x` in the dictionary to the current index `i`. If `x` was already present but further than $k$ steps away, this line updates its index to `i` so subsequent occurrences can be checked against this closer index.

```python3
return False
```
If the iteration completes without finding any pair satisfying the conditions, no such indices exist, so the function returns `False`.

## Dry Run
Input: `nums = [1, 2, 3, 1]`, `k = 3`

| `i` | `x` | `x in last` | `i - last[x] <= k` | Action | `last` State |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `0` | `1` | `False` | N/A | Insert `1: 0` | `{1: 0}` |
| `1` | `2` | `False` | N/A | Insert `2: 1` | `{1: 0, 2: 1}` |
| `2` | `3` | `False` | N/A | Insert `3: 2` | `{1: 0, 2: 1, 3: 2}` |
| `3` | `1` | `True` | `3 - 0 <= 3` (`True`) | Return `True` | Terminated |

Output: `True`

## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. The code traverses `nums` once. Dictionary lookup, insertion, and update operations run in $O(1)$ average time.
- **Space Complexity:** $O(n)$ in the worst case where all elements in `nums` are distinct, causing the `last` dictionary to store $n$ key-value pairs.

## Edge Cases
- **`k = 0`**: Because $i \neq j$, $i - \text{last}[x] \ge 1$. The condition `i - last[x] <= 0` will evaluate to `False` for all elements, returning `False` correctly.
- **Single Element (`nums = [1]`)**: The loop runs once, `x in last` is `False`, and the function returns `False` correctly.
- **Duplicates Outside Range $k$**: For `nums = [1, 0, 1, 1]` with `k = 1`, when `i = 2` (value `1`), `2 - 0 = 2 > 1`. `last[1]` gets updated from `0` to `2`. Then at `i = 3` (value `1`), `3 - 2 = 1 <= 1`, returning `True`. Updating the index on failure is essential for this to work.

## Possible Improvements
Instead of storing all unique elements in a hash map—which can take $O(n)$ space when $n \gg k$—you can use a **Sliding Window Set** that maintains at most $k$ elements:

```python3
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, x in enumerate(nums):
            if x in seen:
                return True
            seen.add(x)
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False
```

- **Space Complexity Improvement:** The sliding window set uses $O(\min(n, k))$ space, which reduces memory usage when $k \ll n$.
- For the existing solution, time complexity is already optimal at $O(n)$.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
