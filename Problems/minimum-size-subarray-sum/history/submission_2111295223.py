class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = w  = 0
        ans = float('inf')
        for r in range(len(nums)):
            w += nums[r]
            while w >= target:
                ans = min(ans, r-l+1)
                w -= nums[l]
                l += 1
                
        return 0 if ans == float('inf') else ans

        