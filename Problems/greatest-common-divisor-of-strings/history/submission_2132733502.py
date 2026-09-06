class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        l = min(m,n)
        ans = ''

        for i in range(l):
            if str1[i] != str2[i]:
                return ''

        for length in range(1,l+1):
            if m%length != 0 or n%length != 0:
                continue
            pattern = str1[:length]

            if pattern * (m//length) == str1 and \
               pattern * (n//length) == str2:
               ans = pattern
        return ans if ans else ''
        
        

