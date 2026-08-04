# 385. Mini Parser

**Difficulty:** Medium
**Topics:** String, Stack, Depth-First Search

[View on LeetCode](https://leetcode.com/problems/mini-parser/)

## Description

Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return *the deserialized* `NestedInteger`.

Each element is either an integer or a list whose elements may also be integers or other lists.

**Example 1:**

```
Input: s = "324"
Output: 324
Explanation: You should return a NestedInteger object which contains a single integer 324.
```

**Example 2:**

```
Input: s = "[123,[456,[789]]]"
Output: [123,[456,[789]]]
Explanation: Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789
```

**Constraints:**

- `1 <= s.length <= 5 * 10^4`
- `s` consists of digits, square brackets `"[]"`, negative sign `'-'`, and commas `','`.
- `s` is the serialization of valid `NestedInteger`.
- All the values in the input are in the range `[-10^6, 10^6]`.

## Similar Questions

- [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) - Medium
- [Ternary Expression Parser](https://leetcode.com/problems/ternary-expression-parser/) - Medium
- [Remove Comments](https://leetcode.com/problems/remove-comments/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
