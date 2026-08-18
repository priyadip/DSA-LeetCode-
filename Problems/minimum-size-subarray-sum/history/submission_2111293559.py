class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = w  = 0
        ans = len(nums) + 1
        for r in range(len(nums)):
            w += nums[r]
            while w >= target:
                ans = min(ans, r-l+1)
                w -= nums[l]
                l += 1
                
        return 0 if ans == len(nums) +1 else ans

        