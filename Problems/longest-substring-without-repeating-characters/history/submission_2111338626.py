class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        store = {}
        for r , ch in enumerate(s):
            if store.get(ch, -1) >= l:
                l = store[ch] + 1
            store[ch] = r
            ans = max(ans, r-l+1)
        return ans
        