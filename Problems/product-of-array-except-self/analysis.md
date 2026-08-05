# 238. Product of Array Except Self - Solution Analysis

## Problem Understanding
The task is to return an array `answer` where `answer[i]` is the product of every element in the input array `nums` except `nums[i]`.

The key constraints are:
1. **Time Complexity:** Must run in $O(n)$ time.
2. **Operation Constraint:** Division cannot be used (which rules out calculating the total product once and dividing by `nums[i]`).
3. **Space Constraint:** The follow-up requests $O(1)$ extra space usage, excluding the output array itself.
4. **Input Constraints:** `2 <= nums.length <= 10^5`, values range between `-30` and `30`, and all products fit within a standard 32-bit signed integer.

## Approach
This solution uses the **Prefix and Suffix Products** pattern (a variation of the Prefix Sum pattern). 

For any index `i`, the product of all elements except `nums[i]` is:
$$\text{answer}[i] = (\text{product of all elements to the left of } i) \times (\text{product of all elements to the right of } i)$$

Instead of allocating two extra arrays of size $n$ to precompute prefix and suffix products, this implementation:
1. Uses the output array `ans` to build up the prefix products in a forward pass.
2. Uses a single scalar variable `suffix` to accumulate products from right to left while updating `ans` in place.

This satisfies both the $O(n)$ time limit and the $O(1)$ auxiliary space follow-up.

## Algorithm
1. Create an output array `ans` of length $n$, pre-filled with `1`.
2. **Prefix Pass:** Loop forward from index `1` to $n-1$. Set `ans[i]` to `ans[i - 1] * nums[i - 1]`, storing the product of all elements to the left of index `i`.
3. Initialize a variable `suffix = 1`.
4. **Suffix Pass:** Loop backward from index $n-1$ down to `0`. Multiply `ans[i]` by `suffix`, then update `suffix` by multiplying it by `nums[i]`.
5. Return `ans`.

## Line-by-Line Explanation
```python
n = len(nums)
ans = [1] * n
```
Gets the length of the input array and initializes the output array `ans` with `1`s. `ans[0]` defaults to `1` because index `0` has no elements to its left.

```python
# prefix 
for i in range(1, n):
    ans[i] = ans[i - 1] * nums[i - 1]
```
Iterates from index `1` to `n - 1`. At each step `i`, `ans[i]` receives the product of all numbers before index `i`. For example, `ans[2]` becomes `nums[0] * nums[1]`.

```python
suffix = 1
```
Initializes the running multiplier for elements strictly to the right of the current index.

```python
# suffix 
for i in range(n - 1, -1, -1):
    ans[i] *= suffix
    suffix *= nums[i]
```
Iterates backward from `n - 1` to `0`. 
- `ans[i] *= suffix` multiplies the stored prefix product at `ans[i]` by the accumulated suffix product of all elements to the right of `i`.
- `suffix *= nums[i]` updates `suffix` to include `nums[i]` before moving to index `i - 1`.

```python
return ans
```
Returns the completed array containing the product of elements except self for each index.

## Dry Run

Given `nums = [1, 2, 3, 4]`:

### Phase 1: Prefix Pass
`ans` begins as `[1, 1, 1, 1]`.

| `i` | `ans[i - 1]` | `nums[i - 1]` | `ans[i]` calculated as | `ans` state |
|---|---|---|---|---|
| 1 | 1 | 1 | `1 * 1 = 1` | `[1, 1, 1, 1]` |
| 2 | 1 | 2 | `1 * 2 = 2` | `[1, 1, 2, 1]` |
| 3 | 2 | 3 | `2 * 3 = 6` | `[1, 1, 2, 6]` |

### Phase 2: Suffix Pass
`suffix` begins at `1`.

| `i` | `ans[i]` (before) | `suffix` (in) | `ans[i] *= suffix` | `nums[i]` | `suffix` (after) | `ans` state |
|---|---|---|---|---|---|---|
| 3 | 6 | 1 | `6 * 1 = 6` | 4 | `1 * 4 = 4` | `[1, 1, 2, 6]` |
| 2 | 2 | 4 | `2 * 4 = 8` | 3 | `4 * 3 = 12` | `[1, 1, 8, 6]` |
| 1 | 1 | 12 | `1 * 12 = 12` | 2 | `12 * 2 = 24` | `[1, 12, 8, 6]` |
| 0 | 1 | 24 | `1 * 24 = 24` | 1 | `24 * 1 = 24` | `[24, 12, 8, 6]` |

Final return value: `[24, 12, 8, 6]`

## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. The array is traversed twice sequentially (once forward, once backward).
- **Space Complexity:** $O(1)$ auxiliary space. The output array `ans` is required by the problem statement and does not count toward extra space complexity. Only a single scalar integer `suffix` is allocated.

## Edge Cases
- **Array containing one zero (e.g., `[-1, 1, 0, -3, 3]`):**
  The index containing `0` will evaluate to the product of all non-zero elements, while all other indices will evaluate to `0`. The algorithm handles this correctly without division-by-zero errors.
- **Array containing multiple zeros (e.g., `[0, 2, 0]`):**
  Every index will have at least one zero in its prefix or suffix, resulting in `[0, 0, 0]`. Handled correctly.
- **Minimum length $n = 2$ (e.g., `[5, 10]`):**
  The prefix loop runs once (`i = 1`), and the suffix loop runs twice (`i = 1`, then `i = 0`), producing `[10, 5]`.
- **Negative numbers:** Sign rules hold over multiplication; two negatives yield a positive suffix/prefix naturally.

## Possible Improvements
This solution is optimal in both time ($O(n)$) and space ($O(1)$ extra space). No further algorithmic improvements exist for this problem statement.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
