# 792. Number of Matching Subsequences - Solution Analysis

## Problem Understanding
Given a string `s` and a list of words, count how many words are subsequences of `s`. A subsequence preserves relative order but not necessarily contiguity. Constraints: `|s| ≤ 5·10⁴`, `|words| ≤ 5000`, `|word| ≤ 50`, lowercase letters only. The large `|s|` and `|words|` rule out checking each word independently with a fresh scan of `s` (O(|s|·|words|) ≈ 2.5·10⁸). We need a single pass over `s` that advances all candidate words in parallel.

## Approach
**Pattern:** Multi-pointer / Bucket Queue (often called "waiting list" or "character buckets").

**Why it fits:** Each word progresses through `s` one character at a time. Instead of scanning `s` for each word, we group words by the *next character they need*. As we iterate `s` once, we take the bucket for the current character, advance every word in it, and re-bucket them by their new next character. This processes all words simultaneously in a single left-to-right pass over `s`.

**Brute-force contrast:** Checking each word separately with two pointers costs O(|s|·|words|). The bucket approach costs O(|s| + Σ|word|) because each character of each word is examined exactly once when its bucket is processed.

**Key insight:** A word only cares about the next occurrence of its current needed character; we can defer all words waiting for `'c'` until we actually see a `'c'` in `s`, then advance them all at once.

## Algorithm
1. Create 26 buckets (or a defaultdict of lists), one per lowercase letter. Each bucket holds tuples `(word, index)` where `index` is the position of the next character the word needs to match.
2. Initialise: for each `word` in `words`, place `(word, 0)` into the bucket for `word[0]`.
3. Iterate through each character `ch` in `s`:
   a. Retrieve the list `current = buckets[ch]` and clear `buckets[ch]` (so words re-added this round aren't processed again for the same `ch`).
   b. For each `(word, i)` in `current`:
      - Increment `i`.
      - If `i == len(word)`: the whole word matched → increment answer.
      - Else: append `(word, i)` to `buckets[word[i]]` (the bucket for the next needed character).
4. Return the accumulated answer.

## Line-by-Line Explanation
- `buckets = defaultdict(list)`: maps each character to a list of `(word, next_index)` pairs waiting for that character.
- `for word in words: buckets[word[0]].append((word, 0))`: seed the buckets with every word waiting for its first character.
- `ans = 0`: counter for fully matched words.
- `for ch in s:`: single left-to-right pass over `s`.
- `current = buckets[ch]; buckets[ch] = []`: take all words waiting for `ch` and empty the bucket so words re-inserted this iteration (impossible here because `i` only increases) don't get double-processed.
- `for word, i in current:`: process each waiting word.
- `i += 1`: we just matched `word[i-1]` with `ch`, so advance to the next needed character.
- `if i == len(word): ans += 1`: word fully consumed → count it.
- `else: buckets[word[i]].append((word, i))`: word still has characters left; park it in the bucket for its new next character.

## Dry Run
Example 1: `s = "abcde"`, `words = ["a","bb","acd","ace"]`

Initial buckets:
- 'a': [("a",0), ("acd",0), ("ace",0)]
- 'b': [("bb",0)]

| Step | ch | current bucket (word, i) | i→i+1 | New bucket / Action |
|------|----|--------------------------|-------|---------------------|
| 1 | 'a' | ("a",0), ("acd",0), ("ace",0) | 1,1,1 | "a": i==len→ans=1; "acd"→bucket['c']; "ace"→bucket['c'] |
| 2 | 'b' | ("bb",0) | 1 | "bb"→bucket['b'] (needs another 'b') |
| 3 | 'c' | ("acd",1), ("ace",1) | 2,2 | "acd"→bucket['d']; "ace"→bucket['e'] |
| 4 | 'd' | ("acd",2) | 3 | i==len→ans=2 |
| 5 | 'e' | ("ace",2) | 3 | i==len→ans=3 |

Final `ans = 3`. ("bb" never finds a second 'b').

## Complexity
- **Time:** O(|s| + Σ|word|). The outer loop runs `|s|` times. Each word character causes exactly one append/pop from a bucket, so total inner iterations = Σ|word|. All operations inside are O(1).
- **Space:** O(|words|) for the buckets (at most one entry per word at any time) plus O(Σ|word|) for storing the word strings themselves (input storage). Auxiliary space is O(|words|).

## Edge Cases
- **Words longer than `s`**: Handled naturally; they never reach `i == len(word)` because `s` ends first.
- **Duplicate words**: Each occurrence is tracked independently in buckets, so duplicates are counted separately (correct per problem statement).
- **Words with characters not in `s`**: Their bucket is never processed; they remain stuck and never increment `ans`.
- **Single-character words**: Matched immediately when their character appears in `s` (i becomes 1 == len).
- **Empty `words` list**: Constraints guarantee `words.length ≥ 1`, but code would return 0 correctly.
- **All 26 letters**: `defaultdict` handles missing keys gracefully; no pre-initialisation needed.

## Possible Improvements
- **Already optimal** for the given constraints. O(|s| + Σ|word|) is linear in the total input size; no asymptotic improvement is possible.
- **Micro-optimisation**: Use a fixed-size list of 26 lists instead of `defaultdict(list)` to avoid hashing overhead (`buckets = [[] for _ in range(26)]`, index with `ord(ch) - 97`). This is faster in practice but same complexity.
- **Memory**: The current code stores the full `word` string in every tuple. Could store only the word index and a separate `positions` array, but Python's string interning and small word length (≤50) make this unnecessary.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
