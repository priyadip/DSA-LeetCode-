class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        m = len(word1)
        n = len(word2)
        for ch1, ch2 in zip(word1, word2):
            ans += ch1+ch2
        if m > n:
            ans += word1[n:]
        if n > m:
            ans += word2[m:]
        return ans


        