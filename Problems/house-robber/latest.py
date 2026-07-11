class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0  # max loot up to i-2 and i-1
        for money in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + money)
        return prev1