class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        n = len(ss)
        j = n-1
        for i in range(n//2):
            if ss[i] != ss[j-i]:
                return False
        return True



        