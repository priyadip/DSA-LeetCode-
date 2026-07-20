from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        mx = 0
        pgcd = []
        for x in nums:
            mx = max(mx,x)
            pgcd.append(gcd(x,mx))

           

        pgcd.sort()
        for i in range(n//2):
            gc = gcd(pgcd[i], pgcd[n-1-i])
            ans += gc
        return ans


        