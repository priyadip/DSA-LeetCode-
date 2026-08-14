class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        return s[k%len(s):]+s[:k%len(s)]




        #return ''.join(s[(i+k)%n] for i in range(n))


        