# 139. Word Break

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Dynamic Programming, Trie, Memoization, Brute-Force Search

[View on LeetCode](https://leetcode.com/problems/word-break/)

## Description

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

**Example 1:**

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:**

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

**Example 3:**

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

**Constraints:**

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

## Similar Questions

- [Word Break II](https://leetcode.com/problems/word-break-ii/) - Hard
- [Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string/) - Medium

---

_Problem statement retrieved from LeetCode. All problem content is the property of LeetCode._
