# 155. Min Stack

**Difficulty:** Medium
**Topics:** Stack, Design

[View on LeetCode](https://leetcode.com/problems/min-stack/)

## Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int value)` pushes the element `value` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints:**

- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

## Hints

<details>
<summary>Hint 1</summary>

Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)

</details>

## Similar Questions

- [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) - Hard
- [Max Stack](https://leetcode.com/problems/max-stack/) - Hard

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
