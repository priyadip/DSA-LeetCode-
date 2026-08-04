# 1331. Rank Transform of an Array

**Difficulty:** Easy
**Topics:** Array, Hash Table, Sorting

[View on LeetCode](https://leetcode.com/problems/rank-transform-of-an-array/)

## Description

Given an array of integers `arr`, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

- Rank is an integer starting from 1.
- The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
- Rank should be as small as possible.

**Example 1:**

```
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
```

**Example 2:**

```
Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
```

**Example 3:**

```
Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
```

**Constraints:**

- `0 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

## Hints

<details>
<summary>Hint 1</summary>

Use a temporary array to copy the array and sort it.

</details>

<details>
<summary>Hint 2</summary>

The rank of each element is the number of unique elements smaller than it in the sorted array plus one.

</details>

## Similar Questions

- [Rank Transform of a Matrix](https://leetcode.com/problems/rank-transform-of-a-matrix/) - Hard
- [Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array/) - Easy

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
