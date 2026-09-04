class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_range(start, end):
            prev2, prev1 = 0, 0

            for i in range(start, end):
                prev2, prev1 = prev1, max(prev1, prev2 + nums[i])

            return prev1

        return max(
            rob_range(0, n - 1),  # exclude last
            rob_range(1, n)       # exclude first
        )