# 12. Integer to Roman - Solution Analysis

## Problem Understanding
The problem asks to convert a given integer `num` into its corresponding Roman numeral string. 

Roman numerals follow a place-value breakdown from highest to lowest. Standard symbols represent specific fixed values ($I=1, V=5, X=10, L=50, C=100, D=500, M=1000$). Normally, symbols are repeated or combined additively. However, when a digit in a decimal place begins with $4$ or $9$, a subtractive form is used ($IV=4, IX=9, XL=40, XC=90, CD=400, CM=900$) to prevent repeating a symbol four times.

The problem bounds `num` strictly to $1 \le \text{num} \le 3999$.

## Approach
This solution uses a **Greedy Algorithm** backed by a static lookup table. 

Because Roman numeral representation is deterministic and always selects the largest possible value component at each step, listing all $13$ possible atomic building blocks (the $7$ standard symbols plus the $6$ subtractive pairs) in descending order allows us to greedily subtract the largest fitting value until `num` becomes $0$.

## Algorithm
1. Define a list of tuples containing integer values and their Roman numeral string equivalents sorted in strictly descending order from $1000$ down to $1$.
2. Initialize an empty string `result`.
3. Iterate through each `(value, roman)` pair in the list:
   - While `num` is greater than or equal to `value`, append `roman` to `result` and subtract `value` from `num`.
4. Return `result`.

## Line-by-Line Explanation

```python
        roman_tuples = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
```
Defines all $13$ fundamental Roman numeral units in descending order. Including the subtractive forms directly in this list eliminates the need for conditional logic checking for $4$ or $9$.

```python
        result = ''
```
Initializes the output string buffer.

```python
        for value, roman in roman_tuples:
```
Iterates through the pre-defined mapping from largest value ($1000$) to smallest ($1$).

```python
            while num >= value:
                result += roman
                num -= value
```
Greedily consumes `value` from `num` as many times as possible. For each successful subtraction, it appends the matching `roman` string to `result`.

```python
        return result
```
Returns the fully constructed Roman numeral representation once `num` reaches $0$.

## Dry Run

Tracing `num = 1994`:

| `value` | `roman` | `num` (before) | Condition `num >= value` | `result` (after) | `num` (after) |
|---|---|---|---|---|---|
| 1000 | `'M'` | 1994 | True | `"M"` | 994 |
| 1000 | `'M'` | 994 | False | `"M"` | 994 |
| 900 | `'CM'` | 994 | True | `"MCM"` | 94 |
| 900 | `'CM'` | 94 | False | `"MCM"` | 94 |
| 500..100 | ... | 94 | False | `"MCM"` | 94 |
| 90 | `'XC'` | 94 | True | `"MCMXC"` | 4 |
| 90 | `'XC'` | 4 | False | `"MCMXC"` | 4 |
| 50..5 | ... | 4 | False | `"MCMXC"` | 4 |
| 4 | `'IV'` | 4 | True | `"MCMXCIV"` | 0 |
| 4 | `'IV'` | 0 | False | `"MCMXCIV"` | 0 |
| 1 | `'I'` | 0 | False | `"MCMXCIV"` | 0 |

Final Output: `"MCMXCIV"`

## Complexity

- **Time Complexity:** $\mathcal{O}(1)$. Where $n$ is `num`. Because $n \le 3999$, the outer loop always runs exactly $13$ times. The inner `while` loop executes at most $15$ times total across all iterations (the longest generated string is $15$ characters for $3888$: `"MMMDCCCLXXXVIII"`). Thus, the runtime is strictly bounded by a constant.
- **Space Complexity:** $\mathcal{O}(1)$. The size of `roman_tuples` is fixed at $13$ elements, and the maximum length of the output string `result` is $15$ characters.

## Edge Cases

- **Minimum Bound (`num = 1`):** Handled correctly. The loop skips down to `(1, 'I')`, appends `'I'`, and terminates.
- **Maximum Bound (`num = 3999`):** Handled correctly. Produces `"MMMDCCCXCIX"`.
- **Subtractive Forms:** Values like $4, 9, 40, 90, 400, 900$ are handled naturally by the presence of these explicit entries in `roman_tuples`.
- **Relaxed Constraint - Zero or Negative Inputs (`num <= 0`):** The `while` condition `num >= value` is never satisfied for positive values, returning an empty string `""`. Standard Roman numerals do not represent zero or negative numbers.
- **Relaxed Constraint - Values $\ge 4000$:** The implementation would append $4$ or more `'M'` symbols (e.g., $4000 \to \text{"MMMM"}$), which violates standard Roman numeral notation where a vinculum (overline) is required for numbers $\ge 4000$.

## Possible Improvements

The implementation is efficient and optimal given the constraints. However, two minor technical modifications exist:

1. **Avoid Repeated String Concatenation:** String concatenation (`result += roman`) creates a new string object on each iteration in Python. Using a list accumulator (`result_list.append(roman)`) followed by `''.join(result_list)` is generally preferred for Pythonic string construction, though for a maximum length of $15$ characters, the performance difference is negligible.
2. **Direct Arithmetic / Direct Place-Value Lookup:** Instead of a `while` loop, you can calculate character frequency via integer division (`count = num // value`) or directly index into positional arrays for thousands, hundreds, tens, and ones:

```python
THOUSANDS = ["", "M", "MM", "MMM"]
HUNDREDS  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
TENS      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
ONES      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

return THOUSANDS[num // 1000] + HUNDREDS[(num % 1000) // 100] + TENS[(num % 100) // 10] + ONES[num % 10]
```

This direct positional lookup eliminates loops entirely, running in pure $O(1)$ operations with zero loop overhead. However, the existing greedy approach remains completely optimal in asymptotic terms.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
