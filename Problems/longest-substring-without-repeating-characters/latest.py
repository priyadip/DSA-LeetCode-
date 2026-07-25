class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        store = {}
        for r, ch in enumerate(s):
            if ch in store and store[ch]>=l:
                l = store[ch]+1
            store[ch] = r
            res = max(res, r-l+1)
        return res




        