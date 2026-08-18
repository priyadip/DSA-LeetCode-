class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sl = sum(nums[:k])
        for i in range(k, len(nums)):
            sl += - nums[i-k]+nums[i]
            if sl > ans:
                ans = sl
        return ans/k
    

        