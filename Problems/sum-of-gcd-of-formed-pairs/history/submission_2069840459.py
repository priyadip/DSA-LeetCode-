from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        mx = 0
        for i in range(n):
            mx = max(mx,nums[i])
            nums[i] = gcd(nums[i], mx)
        nums.sort()
        for i in range(n//2):
            gc = gcd(nums[i], nums[n-1-i])
            ans += gc
        return ans


        