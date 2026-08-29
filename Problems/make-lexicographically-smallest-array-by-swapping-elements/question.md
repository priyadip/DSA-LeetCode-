# 2948. Make Lexicographically Smallest Array by Swapping Elements

**Difficulty:** Medium
**Topics:** Array, Union-Find, Sorting

[View on LeetCode](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/)

## Description

You are given a **0-indexed** array of **positive** integers `nums` and a **positive** integer `limit`.

In one operation, you can choose any two indices `i` and `j` and swap `nums[i]` and `nums[j]` **if** `|nums[i] - nums[j]| <= limit`.

Return *the **lexicographically smallest array** that can be obtained by performing the operation any number of times*.

An array `a` is lexicographically smaller than an array `b` if in the first position where `a` and `b` differ, array `a` has an element that is less than the corresponding element in `b`. For example, the array `[2,10,3]` is lexicographically smaller than the array `[10,2,3]` because they differ at index `0` and `2 < 10`.

**Example 1:**

```
Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.
```

**Example 2:**

```
Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]
Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.
```

**Example 3:**

```
Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]
Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.
```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= limit <= 10^9`

## Hints

<details>
<summary>Hint 1</summary>

Construct a virtual graph where all elements in `nums` are nodes and the pairs satisfying the condition have an edge between them.

</details>

<details>
<summary>Hint 2</summary>

Instead of constructing all edges, we only care about the connected components.

</details>

<details>
<summary>Hint 3</summary>

Can we use DSU?

</details>

<details>
<summary>Hint 4</summary>

Sort `nums`. Now we just need to consider if the consecutive elements have an edge to check if they belong to the same connected component. Hence, all connected components become a list of position-consecutive elements after sorting.

</details>

<details>
<summary>Hint 5</summary>

For each index of `nums` from `0` to `nums.length - 1` we can change it to the current minimum value we have in its connected component and remove that value from the connected component.

</details>

## Similar Questions

- [Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/) - Medium
- [Minimize Hamming Distance After Swap Operations](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
