# 128. Longest Consecutive Sequence - Solution Analysis

## Problem Understanding
The problem asks for the length of the longest sequence of consecutive integers present anywhere within an unsorted array `nums`. The elements do not need to be contiguous in the original array. Duplicate values may appear, and the array can be empty. The primary constraint is that the algorithm must run in $O(n)$ time complexity, which rules out sorting the array (which takes $O(n \log n)$ time).

## Approach
The solution uses a **Hash Set** look-up pattern.

Converting `nums` into a hash set allows $O(1)$ average time lookups. To achieve overall linear time complexity, the algorithm must avoid redundant work—specifically, re-evaluating sub-sequences that are part of a longer sequence. 

It accomplishes this by starting a sequence search **only** at numbers that represent the beginning of a sequence. A number `num` is the start of a sequence if and only if `num - 1` is not present in the set. Once a start element is found, it uses a `while` loop to count consecutive integers going upward until the sequence breaks.

## Algorithm
1. Convert the input list `nums` into a hash set `s`.
2. Initialize `ans = 0` to record the maximum sequence length found.
3. Iterate over each unique element `num` in set `s`:
   a. Check if `num - 1` exists in `s`. If it does, skip `num` because it cannot be the start of a longest sequence.
   b. If `num - 1` is missing, `num` is a sequence start point. Initialize a tracking variable `curr = num`.
   c. Increment `curr` by 1 continuously while `curr` is present in `s`.
   d. Compute the sequence length as `curr - num` and update `ans` if `curr - num > ans`.
4. Return `ans`.

## Line-by-Line Explanation
```python3
s = set(nums)
```
Constructs a hash set `s` from `nums`. This removes duplicates and enables $O(1)$ average lookups for presence checks.

```python3
ans = 0
```
Initializes the maximum sequence length to `0`. If `nums` is empty, the loop will not execute, returning `0`.

```python3
for num in s:
```
Iterates through each unique element in the set `s`. Iterating over `s` rather than `nums` avoids redundant checks on duplicate elements.

```python3
    if num - 1 not in s:
```
Guards the expansion logic. If `num - 1` exists in `s`, `num` is partway through a sequence and will be traversed when its start element is processed. Skipping it here ensures each sequence is traversed only once.

```python3
        curr = num
```
Sets `curr` to the start value of the sequence.

```python3
        while curr in s:
            curr += 1
```
Extends the sequence upwards by incrementing `curr` until `curr` is no longer found in `s`.

```python3
        ans = max(ans, curr - num)
```
Calculates the sequence length using pointer subtraction (`curr - num`) and updates `ans` with the maximum length seen so far.

```python3
return ans
```
Returns the length of the longest consecutive sequence found.

## Dry Run
Input: `nums = [100, 4, 200, 1, 3, 2]`
`s = {1, 2, 3, 4, 100, 200}`
`ans = 0`

| `num` | `num - 1 in s` | `while` loop execution | `curr` after loop | `curr - num` | `ans` |
|---|---|---|---|---|---|
| `1` | `0 not in s` (True) | `curr` goes 1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 4 $\rightarrow$ 5 | `5` | `5 - 1 = 4` | `4` |
| `2` | `1 in s` (False) | Skipped | — | — | `4` |
| `3` | `2 in s` (False) | Skipped | — | — | `4` |
| `4` | `3 in s` (False) | Skipped | — | — | `4` |
| `100` | `99 not in s` (True) | `curr` goes 100 $\rightarrow$ 101 | `101` | `101 - 100 = 1` | `4` |
| `200` | `199 not in s` (True)| `curr` goes 200 $\rightarrow$ 201 | `201` | `201 - 200 = 1` | `4` |

Output: `4`

## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. Creating the set `s` takes $O(n)$ time. In the worst-case scenario (e.g., all numbers are consecutive), every number is visited once in the outer `for` loop, and the inner `while` loop runs $n$ times in total across the entire execution (only for the single sequence start element). Thus, each element is looked up a constant number of times, making it $O(n)$ average time.
- **Space Complexity:** $O(n)$ auxiliary space to store the set `s`, which contains up to $n$ unique elements.

## Edge Cases
- **Empty Array (`nums = []`):** Handled correctly. The loop does not execute, returning `ans = 0`.
- **Single Element (`nums = [5]`):** Handled correctly. `4 not in s` is true, the `while` loop runs once for `curr = 5` and stops at `curr = 6`. `ans` becomes `6 - 5 = 1`.
- **All Duplicate Elements (`nums = [2, 2, 2, 2]`):** Set deduplication reduces `s` to `{2}`. The search returns `1`.
- **Large Integer Ranges:** Element values range between $-10^9$ and $10^9$. Python automatically handles arbitrarily large integers, so integer overflow does not occur during `curr += 1`.

## Possible Improvements
This solution is already optimal in terms of both time ($O(n)$) and space ($O(n)$) complexity. 

The commented-out alternative implementation using explicit `length = 1` incrementing is functionally identical to using `curr` pointer math (`curr - num`). The active version is slightly more concise.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
