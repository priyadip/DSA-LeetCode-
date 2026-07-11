class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if sum(nums) < abs(target):
            return 0
        if (target + sum(nums))%2:
            return 0
        tar = (target + sum(nums))//2
        dp = [0]*(tar+1)
        dp[0] = 1
        
        for x in nums:
            for j in range(tar, x-1, -1):
                dp[j] += dp[j-x]
        return dp[tar]
        