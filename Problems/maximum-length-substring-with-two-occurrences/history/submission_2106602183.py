class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        cn = [0]*26
        n, l, ans = len(s), 0, 0

        for r in range(n):
            x = ord(s[r]) -97
            cn[x] += 1

            while cn[x] > 2:
                cn[ ord(s[l]) - 97 ] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans




        