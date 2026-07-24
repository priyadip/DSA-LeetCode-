class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)
        # if len(s) != len(t):
        #     return False

        # freq = {}

        # for c in s:
        #     freq[c] = freq.get(c, 0) + 1

        # for c in t:
        #     if c not in freq:
        #         return False
        #     freq[c] -= 1
        #     if freq[c] == 0:
        #         del freq[c]

        # return not freq
        