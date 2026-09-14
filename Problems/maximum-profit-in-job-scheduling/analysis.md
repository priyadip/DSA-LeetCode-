# 1235. Maximum Profit in Job Scheduling - Solution Analysis

## Problem Understanding
Given n jobs with start times, end times, and profits, select a subset of non-overlapping jobs that maximizes total profit. Jobs touching at endpoints (one ends at X, another starts at X) are compatible. Constraints: n ≤ 5·10⁴, times up to 10⁹, profits up to 10⁴. The large n rules out O(n²) DP; the large time range rules out coordinate compression over time values directly.

## Approach
**Weighted Interval Scheduling via DP + Binary Search**. The brute force would try all subsets (2ⁿ) or use O(n²) DP checking all previous jobs for each job. Sorting jobs by end time lets us define `dp[i]` as the maximum profit using the first i jobs in sorted order. For each job, we either skip it (`dp[i-1]`) or take it plus the best compatible prefix (`dp[j] + profit[i]`), where j is the last job ending ≤ current start. Binary search on the sorted end-times array finds j in O(log n), yielding O(n log n) overall. **Key insight**: sorting by end time makes the compatible prefix a contiguous prefix, so its optimum is a single DP value.

## Algorithm
1. Combine the three input arrays into a list of (start, end, profit) tuples and sort by end time ascending.
2. Extract the sorted end times into a separate array `ends` for binary search.
3. Initialise `dp` of length n+1 with zeros; `dp[i]` will hold the answer for the first i jobs (1-indexed).
4. For i from 1 to n:
   a. Let (start, end, value) be the (i-1)-th job in the sorted list.
   b. Use `bisect_right(ends, start, hi=i-1)` to find the count of jobs among the first i-1 that end ≤ start; this count is exactly the index j such that `dp[j]` is the best profit compatible with the current job.
   c. `take = dp[j] + value`, `skip = dp[i-1]`.
   d. `dp[i] = max(take, skip)`.
5. Return `dp[n]`.

## Line-by-Line Explanation
- `n = len(startTime)`: number of jobs.
- `jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])`: bundles each job and sorts by end time so compatible jobs form a prefix.
- `ends = [job[1] for job in jobs]`: array of end times in sorted order, used for binary search.
- `dp = [0] * (n + 1)`: DP table where `dp[i]` = max profit using first i sorted jobs.
- `for i in range(1, n + 1):`: iterate jobs in end-time order (1-indexed for DP convenience).
- `start, end, value = jobs[i - 1]`: unpack current job (0-indexed in `jobs`).
- `j = bisect_right(ends, start, hi=i - 1)`: finds insertion point for `start` in `ends[0:i-1]`; all jobs before that index end ≤ start, so `j` is the number of compatible jobs, and `dp[j]` is their optimal profit.
- `take = dp[j] + value`: profit if we take this job plus best compatible prefix.
- `skip = dp[i - 1]`: profit if we skip this job.
- `dp[i] = max(take, skip)`: optimal profit for first i jobs.
- `return dp[n]`: answer for all n jobs.

## Dry Run
Example 1: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]

Sorted jobs by end: (1,3,50), (2,4,10), (3,5,40), (3,6,70)  
ends = [3,4,5,6]

| i | start | end | value | j = bisect_right(ends, start, hi=i-1) | take = dp[j]+value | skip = dp[i-1] | dp[i] |
|---|-------|-----|-------|----------------------------------------|---------------------|----------------|-------|
| 1 | 1     | 3   | 50    | 0 (no prior jobs)                      | 0+50=50             | 0              | 50    |
| 2 | 2     | 4   | 10    | 0 (ends[0]=3 > 2)                      | 0+10=10             | 50             | 50    |
| 3 | 3     | 5   | 40    | 1 (ends[0]=3 ≤ 3)                      | 50+40=90            | 50             | 90    |
| 4 | 3     | 6   | 70    | 1 (ends[0]=3 ≤ 3, ends[1]=4 > 3)       | 50+70=120           | 90             | 120   |

Return dp[4] = 120. Matches expected output.

## Complexity
- Time: O(n log n). Sorting takes O(n log n). The loop runs n times; each iteration does a binary search on at most i-1 elements (O(log n)) and O(1) work.
- Space: O(n). The `jobs`, `ends`, and `dp` arrays each store n elements.

## Edge Cases
- **Single job (n=1)**: Loop runs once, j=0, take=profit[0], skip=0, returns profit[0]. Correct.
- **All jobs overlapping (e.g., same start, increasing end)**: Only one job can be chosen; DP correctly picks the max profit among them because each job's compatible prefix is empty (j=0), so `take = profit[i]`, `skip` carries forward the max seen so far.
- **Jobs touching at endpoints**: `bisect_right` with `start` includes jobs ending exactly at `start`, satisfying the "end at X, start at X" rule.
- **Maximum constraints (n=5·10⁴)**: O(n log n) fits easily within limits; recursion depth is not used, so no stack overflow risk.
- **Large time values (10⁹)**: Binary search operates on indices, not time values, so magnitude does not affect complexity.

## Possible Improvements
The solution is already optimal in asymptotic complexity for the given constraints. A minor clarity improvement: rename `value` to `profit` for consistency with the problem statement. The `hi=i-1` argument in `bisect_right` is correct and necessary to restrict search to already-processed jobs; omitting it would search the full `ends` array and produce wrong j for jobs with the same end time. No further algorithmic improvement is possible without changing the complexity class.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
