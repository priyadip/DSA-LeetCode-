# 1510. Stone Game IV

**Difficulty:** Hard
**Topics:** Math, Dynamic Programming, Minimax, Game Theory, Nim Game, Sprague–Grundy Theorem, Zero-Sum Game

[View on LeetCode](https://leetcode.com/problems/stone-game-iv/)

## Description

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are `n` stones in a pile. On each player's turn, that player makes a *move* consisting of removing **any** non-zero **square number** of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer `n`, return `true` if and only if Alice wins the game otherwise return `false`, assuming both players play optimally.

**Example 1:**

```
Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
```

**Example 2:**

```
Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
```

**Example 3:**

```
Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
```

**Constraints:**

- `1 <= n <= 10^5`

## Hints

<details>
<summary>Hint 1</summary>

Use dynamic programming to keep track of winning and losing states. Given some number of stones, Alice can win if she can force Bob onto a losing state.

</details>

## Similar Questions

- [Stone Game V](https://leetcode.com/problems/stone-game-v/) - Hard
- [Stone Game VI](https://leetcode.com/problems/stone-game-vi/) - Medium
- [Stone Game VII](https://leetcode.com/problems/stone-game-vii/) - Medium
- [Stone Game VIII](https://leetcode.com/problems/stone-game-viii/) - Hard
- [Stone Game IX](https://leetcode.com/problems/stone-game-ix/) - Medium
- [Stone Removal Game](https://leetcode.com/problems/stone-removal-game/) - Easy

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
