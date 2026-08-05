# 385. Mini Parser - Solution Analysis

## Problem Understanding
The task requires parsing a serialized string `s` representing a nested list of integers (similar to JSON array structure) and constructing its equivalent `NestedInteger` data structure.

- Input consists of integers, square brackets `[` and `]`, negative signs `-`, and commas `,`.
- A `NestedInteger` object can either store a single integer value or a list of `NestedInteger` objects.
- Constraints guarantee valid input syntax, no spaces, and integer values fitting within `[-10^6, 10^6]`. String length $N \le 5 \times 10^4$.

## Approach
This solution uses an **Explicit Stack** pattern for parsing nested structures:
1. **Special case early-exit**: If the input does not start with `'['`, it represents a primitive integer rather than a list.
2. **Stack for nested contexts**: For list inputs, square brackets dictate depth. Encountering `'['` signals the start of a sub-list, requiring the current list context to be saved onto a stack. Encountering `']'` pops the parent list and adds the completed sub-list to it.
3. **Delimiter-driven tokenization**: Numbers are accumulated digit-by-digit. When a delimiter (`,` or `]`) is encountered, the code checks if a number was just finished by inspecting the preceding character (`s[i - 1]`).

## Algorithm
1. Check if `s[0] != '['`. If so, parse `s` directly as an integer using `int(s)`, wrap it in a `NestedInteger`, and return it.
2. Initialize an empty stack `stack`, `curr = None`, `num = 0`, and `sign = 1`.
3. Iterate through index `i` and character `ch` of `s`:
   - If `ch == '['`: If `curr` exists, push `curr` onto `stack`. Set `curr` to a new empty `NestedInteger` list.
   - If `ch == '-'`: Set `sign = -1`.
   - If `ch.isdigit()`: Update `num = num * 10 + int(ch)`.
   - If `ch` is `,` or `]`:
     - If `s[i - 1].isdigit()` is true, append `NestedInteger(sign * num)` to `curr`. Reset `num = 0` and `sign = 1`.
     - If `ch == ']'` and `stack` is non-empty: Pop `parent` from `stack`, append `curr` to `parent`, and update `curr = parent`.
4. Return `curr`.

## Line-by-Line Explanation
```python
if s[0] != '[':
    return NestedInteger(int(s))
```
Checks if the entire input is just a primitive integer (e.g., `"324"` or `"-324"`). If so, converts it directly without executing stack logic.

```python
stack = []
curr = None
num = 0
sign = 1
```
Initializes the stack to hold parent list contexts, `curr` to track the active list, `num` to accumulate multi-digit values, and `sign` for signed integer handling.

```python
for i, ch in enumerate(s):
```
Iterates through each character in the string with its index `i`.

```python
if ch == '[':
    if curr:
        stack.append(curr)
    curr = NestedInteger()
```
When an opening bracket is seen, if an active list `curr` already exists, it is saved onto `stack`. `curr` is then re-assigned to a newly created `NestedInteger` list node.

```python
elif ch == '-':
    sign = -1
```
Captures the negative sign for upcoming digits.

```python
elif ch.isdigit():
    num = num * 10 + int(ch)
```
Accumulates digits into `num` using standard base-10 shift arithmetic.

```python
elif ch in ',]':
    if s[i - 1].isdigit():
        curr.add(NestedInteger(sign * num))
        num = 0
        sign = 1
```
When encountering a delimiter (`,` or `]`), checks if the character immediately preceding it was a digit (`s[i - 1].isdigit()`). If true, constructs the integer node `NestedInteger(sign * num)`, adds it to `curr`, and resets `num` and `sign`.

```python
    if ch == ']' and stack:
        parent = stack.pop()
        parent.add(curr)
        curr = parent
```
If the closing bracket finishes an inner list (indicated by `stack` being non-empty), pops the parent list from `stack`, adds `curr` into `parent`, and restores `curr` to point back to `parent`.

```python
return curr
```
Returns the root `NestedInteger` object containing the fully deserialized structure.

## Dry Run
Tracing `s = "[123,[456]]"`:

| `i` | `ch` | `stack` | `curr` | `num` | `sign` | Action / Explanation |
|---|---|---|---|---|---|---|
| 0 | `[` | `[]` | `List([])` | 0 | 1 | Initialize root list `curr`. |
| 1 | `1` | `[]` | `List([])` | 1 | 1 | `num = 1` |
| 2 | `2` | `[]` | `List([])` | 12 | 1 | `num = 12` |
| 3 | `3` | `[]` | `List([])` | 123 | 1 | `num = 123` |
| 4 | `,` | `[]` | `List([123])` | 0 | 1 | `s[3]` is digit $\rightarrow$ add `123` to `curr`. Reset `num`. |
| 5 | `[` | `[List([123])]` | `List([])` | 0 | 1 | Save root list to `stack`. Start inner list `curr`. |
| 6 | `4` | `[List([123])]` | `List([])` | 4 | 1 | `num = 4` |
| 7 | `5` | `[List([123])]` | `List([])` | 45 | 1 | `num = 45` |
| 8 | `6` | `[List([123])]` | `List([])` | 456 | 1 | `num = 456` |
| 9 | `]` | `[]` | `List([123, List([456])])` | 0 | 1 | `s[8]` is digit $\rightarrow$ add `456` to inner list. `ch == ']'` $\rightarrow$ pop root, add inner list to root, `curr = root`. |
| 10 | `]` | `[]` | `List([123, List([456])])` | 0 | 1 | `s[9]` is `]` (not digit). `ch == ']'`, but `stack` is empty, so no pop occurs. |

Final result: `curr` holds `List([123, List([456])])`.

## Complexity
- **Time Complexity:** $O(N)$, where $N$ is the length of string `s`. Every character is examined a constant number of times during the single-pass loop.
- **Space Complexity:** $O(N)$ in the worst case. The explicit `stack` stores references to outer `NestedInteger` objects, whose max depth can reach $O(N)$ for deeply nested inputs like `[[[[...]]]]`.

## Edge Cases
- **Single Integer without brackets (`"324"`, `"-324"`):** Handled by the guard clause `if s[0] != '[':`.
- **Empty List (`"[]"` or `"[[]]"`):** When `]` is encountered immediately after `[`, `s[i - 1]` is `'['`, so `s[i - 1].isdigit()` evaluates to `False`. No integer node is created or added.
- **Negative Numbers (`"[-123]"`):** `sign` is set to `-1` when `'-'` is encountered, correctly negating `num` when added.
- **Deep Nesting:** Stack management ensures parent-child relations remain accurate across nested levels.

## Possible Improvements
- **Fragility of `s[i - 1].isdigit()`:** Looking backward in the string works because the problem guarantees valid syntax without whitespace. However, relying on string look-behind makes parser state implicit. A state variable like `has_num: bool` (set to `True` when encountering a digit) would make the token flushing logic explicit and resilient to potential formatting changes like whitespace.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
