class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]          # dp[i] = dp[i][i]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(
                    nums[i] - dp[j],      # old dp[j] = dp[i+1][j]
                    nums[j] - dp[j - 1]   # dp[j-1] = dp[i][j-1]
                )

        return dp[-1] >= 0

        