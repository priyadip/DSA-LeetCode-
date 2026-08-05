# 3499. Maximize Active Section with Trade I - Solution Analysis

## Problem Understanding
The problem involves a binary string `s` where '1' represents an active section and '0' represents an inactive section. The goal is to maximize the number of active sections in `s` after making at most one trade. A trade involves converting a contiguous block of '1's surrounded by '0's to all '0's and then converting a contiguous block of '0's surrounded by '1's to all '1's. The string `s` is treated as if it is augmented with a '1' at both ends.

## Approach
The solution uses a combination of string splitting and enumeration to solve the problem. It splits the input string into runs of identical characters (either '0' or '1') and then calculates the maximum gain that can be achieved by making a trade. This approach fits the problem well because it allows for efficient enumeration of all possible trades and calculation of the maximum gain.

## Algorithm
Here are the concise steps of the solution's method:
1. Split the input string into runs of identical characters.
2. Calculate the total number of '1's in the string.
3. Identify all '1' runs that are surrounded by '0' runs and store their lengths and indices.
4. Identify the top three longest '0' runs and store their lengths and indices.
5. Iterate over all '1' runs and calculate the maximum gain that can be achieved by making a trade for each '1' run.
6. Return the total number of '1's plus the maximum gain.

## Line-by-Line Explanation
```python
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
```
This defines a class `Solution` with a method `maxActiveSectionsAfterTrade` that takes a string `s` as input.
```python
runs = []
for ch in s:
    if runs and runs[-1][0] == ch:
        runs[-1][1] += 1
    else:
        runs.append([ch, 1])
```
This code splits the input string into runs of identical characters. It iterates over each character `ch` in the string and checks if the last run in the `runs` list has the same character. If it does, it increments the length of the last run. Otherwise, it appends a new run to the `runs` list.
```python
Z = []                # lengths of all '0' runs
interior = []         # (length_A, left_zero_index)
total_ones = 0
```
This initializes three variables: `Z` to store the lengths of all '0' runs, `interior` to store the lengths and indices of '1' runs that are surrounded by '0' runs, and `total_ones` to store the total number of '1's in the string.
```python
for i, (ch, ln) in enumerate(runs):
    if ch == '1':
        total_ones += ln
       
        if 0 < i < len(runs) - 1:
            left_idx = len(Z) - 1   # previous '0' is the last element in Z
            interior.append((ln, left_idx))
    else:
        Z.append(ln)
```
This code iterates over the `runs` list and updates the `total_ones`, `Z`, and `interior` variables accordingly.
```python
top3 = [(0, -1), (0, -1), (0, -1)]
for idx, length in enumerate(Z):
    if length > top3[0][0]:
        top3 = [(length, idx), top3[0], top3[1]]
    elif length > top3[1][0]:
        top3 = [top3[0], (length, idx), top3[1]]
    elif length > top3[2][0]:
        top3[2] = (length, idx)
```
This code finds the top three longest '0' runs and stores their lengths and indices in the `top3` list.
```python
max_gain = 0
for A, left_idx in interior:
    right_idx = left_idx + 1
    #  flip the merged zero block
    gain_merged = Z[left_idx] + Z[right_idx]

    #  flip the best zero block elsewhere
    best_other = 0
    for ln, idx in top3:
        if idx != left_idx and idx != right_idx:
            best_other = ln
            break
    gain_sep = best_other - A

    max_gain = max(max_gain, gain_merged, gain_sep)
```
This code iterates over the `interior` list and calculates the maximum gain that can be achieved by making a trade for each '1' run.
```python
return total_ones + max_gain
```
This returns the total number of '1's plus the maximum gain.

## Dry Run
Let's consider an example input `s = "0100"`. The `runs` list would be `[['0', 1], ['1', 1], ['0', 2]]`. The `Z` list would be `[1, 2]`, and the `interior` list would be `[(1, 0)]`. The `top3` list would be `[(2, 1), (1, 0), (0, -1)]`. The maximum gain would be calculated as `max(0, 3, -1) = 3`. The final output would be `1 + 3 = 4`.

| Iteration | `runs` | `Z` | `interior` | `top3` | `max_gain` |
| --- | --- | --- | --- | --- | --- |
| 1 | `[['0', 1], ['1', 1], ['0', 2]]` | `[1, 2]` | `[(1, 0)]` | `[(2, 1), (1, 0), (0, -1)]` | 3 |
| 2 | `[['0', 1], ['1', 1], ['0', 2]]` | `[1, 2]` | `[(1, 0)]` | `[(2, 1), (1, 0), (0, -1)]` | 3 |

## Complexity
The time complexity is O(n), where n is the length of the input string. This is because the solution iterates over the input string once to split it into runs, and then iterates over the runs list to calculate the maximum gain. The space complexity is also O(n), where n is the length of the input string. This is because the solution stores the runs list, the Z list, and the interior list, which can have a maximum length of n.

## Edge Cases
The solution handles the following edge cases:
* Empty input string: The solution would return 0, which is correct because there are no active sections.
* Single element: The solution would return 1 if the single element is '1', and 0 if the single element is '0', which is correct.
* Duplicates: The solution handles duplicates correctly by merging adjacent runs of identical characters.
* Overflow: The solution does not overflow because it uses integers to store the lengths of the runs, which are at most n, where n is the length of the input string.
* Maximum size: The solution handles the maximum size correctly because it uses integers to store the lengths of the runs, which are at most n, where n is the length of the input string.

## Possible Improvements
The solution is already optimal for the given constraints, with a time complexity of O(n) and a space complexity of O(n). However, some minor improvements could be made, such as reducing the number of iterations over the runs list or using a more efficient data structure to store the runs. Nevertheless, these improvements would likely have a negligible impact on the overall performance of the solution.

---

_Generated by leetvault using groq (llama-3.3-70b-versatile)_
