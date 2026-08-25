# 20. Valid Parentheses

**Difficulty:** Easy
**Topics:** String, Stack, Bracket Sequences

[View on LeetCode](https://leetcode.com/problems/valid-parentheses/)

## Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

**Input:** s = "()"

**Output:** true

**Example 2:**

**Input:** s = "()[]{}"

**Output:** true

**Example 3:**

**Input:** s = "(]"

**Output:** false

**Example 4:**

**Input:** s = "([])"

**Output:** true

**Example 5:**

**Input:** s = "([)]"

**Output:** false

**Constraints:**

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## Hints

<details>
<summary>Hint 1</summary>

Use a stack of characters.

</details>

<details>
<summary>Hint 2</summary>

When you encounter an opening bracket, push it to the top of the stack.

</details>

<details>
<summary>Hint 3</summary>

When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.

</details>

## Similar Questions

- [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) - Medium
- [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) - Hard
- [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) - Hard
- [Check If Word Is Valid After Substitutions](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/) - Medium
- [Check if a Parentheses String Can Be Valid](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/) - Medium
- [Move Pieces to Obtain a String](https://leetcode.com/problems/move-pieces-to-obtain-a-string/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
