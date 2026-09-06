class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        m = len(word1)
        n = len(word2)
        for ch1, ch2 in zip(word1, word2):
            ans.append(ch1)
            ans.append(ch2)
        if m > n:
            ans.extend(word1[n:])
        if n > m:
            ans.extend(word2[m:])
        return ''.join(ans)


        