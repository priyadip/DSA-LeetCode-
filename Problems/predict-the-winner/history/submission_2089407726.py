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



        # @cache
        # def dfs(i, j):

        #     if i == j:
        #         return nums[i]

        #     left = nums[i] - dfs(i + 1, j)
        #     right = nums[j] - dfs(i, j - 1)

        #     return max(left, right)

        # return dfs(0, len(nums) - 1) >= 0



        # n = len(nums)

        # dp = [[0] * n for _ in range(n)]

        # for i in range(n):
        #     dp[i][i] = nums[i]

        # for length in range(2, n + 1):
        #     for i in range(n - length + 1):
        #         j = i + length - 1

        #         dp[i][j] = max(
        #             nums[i] - dp[i + 1][j],
        #             nums[j] - dp[i][j - 1]
        #         )

        # return dp[0][n - 1] >= 0

        