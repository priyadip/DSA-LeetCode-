# 1423. Maximum Points You Can Obtain from Cards

**Difficulty:** Medium
**Topics:** Array, Sliding Window, Prefix Sum

[View on LeetCode](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)

## Description

There are several cards **arranged in a row**, and each card has an associated number of points. The points are given in the integer array `cardPoints`.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly `k` cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array `cardPoints` and the integer `k`, return the *maximum score* you can obtain.

**Example 1:**

```
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
```

**Example 2:**

```
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
```

**Example 3:**

```
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
```

**Constraints:**

- `1 <= cardPoints.length <= 10^5`
- `1 <= cardPoints[i] <= 10^4`
- `1 <= k <= cardPoints.length`

## Hints

<details>
<summary>Hint 1</summary>

Let the sum of all points be total_pts. You need to remove a sub-array from cardPoints with length n - k.

</details>

<details>
<summary>Hint 2</summary>

Keep a window of size n - k over the array. The answer is max(answer, total_pts - sumOfCurrentWindow)

</details>

## Similar Questions

- [Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/) - Hard
- [Removing Minimum and Maximum From Array](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/) - Medium
- [Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) - Easy
- [Maximum Spending After Buying Items](https://leetcode.com/problems/maximum-spending-after-buying-items/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
