class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        j = 0
        ans = 0
        for i in range(len(s)-1):
            if ord(s[i])+1 == ord(s[i+1]):
                j += 1
            else:
                j = 0
            if j > ans:
                ans = j
        return ans + 1           


        