class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, j):

            if i == j:
                return nums[i]

            left = nums[i] - dfs(i + 1, j)
            right = nums[j] - dfs(i, j - 1)

            return max(left, right)

        return dfs(0, len(nums) - 1) >= 0

        