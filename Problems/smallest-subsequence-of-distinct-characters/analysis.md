# 1081. Smallest Subsequence of Distinct Characters - Solution Analysis

## Problem Understanding
The problem asks to find the lexicographically smallest subsequence of distinct characters in a given string `s`. This means we need to return a subsequence that contains all unique characters in `s`, exactly once, and this subsequence should be the smallest possible when compared lexicographically. The constraints are that `s` is a string of length between 1 and 1000 and consists only of lowercase English letters.

## Approach
The solution uses the monotonic stack algorithmic pattern. A monotonic stack is a stack that maintains a specific order of elements, in this case, a lexicographically increasing order. This pattern fits because it allows us to efficiently find the lexicographically smallest subsequence by iteratively pushing and popping characters from the stack, ensuring that the resulting stack (and thus the subsequence) is always in the correct order.

## Algorithm
1. Create a dictionary `last` to store the last occurrence of each character in the string `s`.
2. Initialize an empty stack and a set `seen` to keep track of characters that have been added to the stack.
3. Iterate through `s`, for each character `c`:
    * If `c` is already in `seen`, skip it.
    * While the stack is not empty and the top of the stack is greater than `c` and the last occurrence of the top of the stack is after the current index `i`, remove the top of the stack from `seen` and pop it from the stack.
    * Push `c` onto the stack and add it to `seen`.
4. Return the characters in the stack as a string, which is the lexicographically smallest subsequence.

## Line-by-Line Explanation
```python
last = {c: i for i,c in enumerate(s)}
```
This line creates a dictionary `last` where the keys are characters in `s` and the values are the indices of their last occurrences. This is done using a dictionary comprehension.

```python
stack = []
seen = set()
```
Here, an empty list `stack` and an empty set `seen` are initialized. The stack will store characters in the order they are added to the subsequence, and the set `seen` keeps track of characters that have been added to the stack.

```python
for i, c in enumerate(s):
    if c in seen:
        continue
```
This loop iterates over each character `c` in `s` along with its index `i`. If `c` is already in `seen`, it means `c` has already been added to the stack and thus to the subsequence, so the loop continues to the next iteration.

```python
while stack and stack[-1] > c and last[stack[-1]] > i:
    seen.remove(stack.pop())
```
This while loop checks two conditions: the stack is not empty (`stack`), the top of the stack (`stack[-1]`) is greater than the current character `c`, and the last occurrence of the top of the stack is after the current index `i`. If both conditions are true, it means adding `c` to the stack now would make the subsequence lexicographically smaller without causing any character to appear more than once or missing any character. So, it removes the top of the stack from `seen` and pops it from the stack.

```python
stack.append(c)
seen.add(c)
```
After the while loop, `c` is pushed onto the stack, and it is added to `seen` to mark it as part of the subsequence.

```python
return "".join(stack)
```
Finally, the function returns the characters in the stack as a string, which is the lexicographically smallest subsequence of distinct characters in `s`.

## Dry Run
Let's consider an example with the input string "bcabc". Here's how the state evolves over the iterations:
| Index `i` | Character `c` | Stack | Seen |
| --- | --- | --- | --- |
| 0 | b | [b] | {b} |
| 1 | c | [b, c] | {b, c} |
| 2 | a | [a, b, c] | {a, b, c} |
| 3 | b | [a, b, c] | {a, b, c} |
| 4 | c | [a, b, c] | {a, b, c} |
As we iterate, the stack remains [a, b, c] because any further operations do not change the stack due to the conditions in the while loop.

## Complexity
The time complexity is O(n), where n is the length of the string `s`, because we make a single pass through `s`. The space complexity is also O(n) because in the worst case, we might store every character in the stack and the set `seen`, and the dictionary `last` also stores n characters at most.

## Edge Cases
This solution handles strings with all distinct characters, with duplicate characters, and with various lengths up to 1000. However, it does not handle an empty string explicitly, but it will correctly return an empty string for such a case because the loop will not execute. It also assumes all characters are lowercase English letters, as per the problem constraints, and does not check for this condition.

## Possible Improvements
The solution is already quite efficient, with a linear time complexity. However, for very large strings, additional optimizations might be needed, such as more efficient data structures for storing the last occurrence of characters or the stack. Yet, within the given constraints (string length up to 1000), the current implementation is sufficient and optimal.

---

_Generated by leetvault using groq (llama-3.3-70b-versatile)_
