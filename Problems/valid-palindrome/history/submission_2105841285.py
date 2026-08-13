class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return False
        return True



        