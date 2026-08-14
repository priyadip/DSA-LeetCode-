class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        rs = ''
        for i in range(n := len(s)):
            rs += s[(i+k) % n]
        return rs


        