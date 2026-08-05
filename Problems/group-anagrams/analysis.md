# 49. Group Anagrams - Solution Analysis

## Problem Understanding

The problem requires grouping an array of strings `strs` into sublists where each sublist contains strings that are anagrams of one another. Anagrams are strings that contain the exact same characters with the exact same frequencies, differing only in the order of characters.

The key constraints are:
- $N = \text{len}(strs) \le 10^4$
- $K = \text{len}(strs[i]) \le 100$
- Characters are strictly lowercase English letters (`'a'` through `'z'`).

Because $K$ is small ($\le 100$), string transformations per word are cheap, but $N$ is up to $10^4$, requiring an efficient strategy for grouping identical character distributions.

## Approach

This solution uses a **Hash Map with Sorting-Based Canonical Keys**.

Two strings are anagrams if and only if sorting their characters results in identical strings. By sorting each word, we derive a unique canonical signature (`key`) for its anagram group. A hash map (`defaultdict`) maps this canonical string key to a list of original words that produce that key.

## Algorithm

1. Initialize a hash map `save` where missing keys automatically map to empty lists.
2. Iterate through each string `word` in `strs`:
   a. Sort the characters of `word` lexicographically.
   b. Rejoin the sorted characters into a single key string.
   c. Append `word` to the list in `save` under `key`.
3. Extract and return all value lists from `save`.

## Line-by-Line Explanation

```python
save = defaultdict(list)
```
Initializes a `defaultdict` from Python's `collections` module. Accessing a missing key automatically initializes it with an empty list (`[]`), avoiding manual key existence checks.

```python
for word in strs:
```
Iterates through each string in the input list sequentially.

```python
    key = ''.join(sorted(word))
```
`sorted(word)` breaks `word` into a list of characters and sorts them in $O(K \log K)$ time. `''.join(...)` concatenates the sorted characters back into a string key. Anagrams like `"eat"`, `"tea"`, and `"ate"` all produce the key `"aet"`.

```python
    save[key].append(word)
```
Looks up `key` in `save` and appends the un-sorted `word` to the corresponding group.

```python
return list(save.values())
```
Retrieves all grouped anagram lists from the dictionary and returns them as a 2D list.

## Dry Run

Input: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

| Iteration | `word` | `key` | `save` State |
|---|---|---|---|
| 1 | `"eat"` | `"aet"` | `{"aet": ["eat"]}` |
| 2 | `"tea"` | `"aet"` | `{"aet": ["eat", "tea"]}` |
| 3 | `"tan"` | `"ant"` | `{"aet": ["eat", "tea"], "ant": ["tan"]}` |
| 4 | `"ate"` | `"aet"` | `{"aet": ["eat", "tea", "ate"], "ant": ["tan"]}` |
| 5 | `"nat"` | `"ant"` | `{"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}` |
| 6 | `"bat"` | `"abt"` | `{"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": ["bat"]}` |

Output: `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

## Complexity

Let $N$ be the number of strings in `strs`, and $K$ be the maximum length of a string in `strs`.

- **Time Complexity:** $O(N \cdot K \log K)$. Iterating over $N$ strings takes $O(N)$ steps. For each string of length up to $K$, sorting takes $O(K \log K)$ time and joining takes $O(K)$ time. Dictionary insertions and lookups take $O(K)$ average time due to hashing string keys of length $K$.
- **Space Complexity:** $O(N \cdot K)$. The hash map stores all $N$ original strings across its values, which takes $O(N \cdot K)$ memory. The unique string keys also take up to $O(N \cdot K)$ space in the worst case (when all strings are distinct).

## Edge Cases

- **Empty Strings (`strs = [""]`):** `sorted("")` returns `[]`, `''.join([])` returns `""`. The key `""` is valid and mapped to `[""]`.
- **Single Character Strings (`strs = ["a"]`):** Handled cleanly without overhead.
- **Duplicate Words in Input (`strs = ["a", "a"]`):** Both words generate key `"a"` and are grouped together in the same list `["a", "a"]`.
- **No Anagram Matches:** Each word generates a distinct key, resulting in $N$ groups of size 1.

## Possible Improvements

The solution can be optimized in time complexity by replacing sorting with character frequency counting.

Since input strings contain only lowercase English letters, a fixed 26-element tuple representing character frequencies can serve as the map key:

```python
for word in strs:
    count = [0] * 26
    for ch in word:
        count[ord(ch) - ord('a')] += 1
    save[tuple(count)].append(word)
```

- **Frequency Counting Time Complexity:** $O(N \cdot K)$, because counting characters per word takes linear time $O(K)$ instead of $O(K \log K)$.
- **Trade-off in Python:** Note that you already wrote and commented out this frequency-tuple approach in your solution file. In Python, Python's built-in `sorted()` is implemented in C (Timsort), whereas a pure Python `ord()` loop over 26 elements carries interpreter overhead. For $K \le 100$, string sorting is often practically as fast or faster in LeetCode's Python runtime, even though frequency counting has lower theoretical asymptotic complexity.

---

_Generated by leetvault using gemini (gemini-flash-latest)_
