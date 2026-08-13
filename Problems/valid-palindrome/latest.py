class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        # n = len(s)
        # for i in range(n//2):
        #     if s[i] != s[n-1-i]:
        #         return False
        # return True
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True



        