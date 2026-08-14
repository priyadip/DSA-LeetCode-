class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k %= n
        return s[k:]+s[:k]




        #return ''.join(s[(i+k)%n] for i in range(n))


        