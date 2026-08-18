class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sl = mean(nums[:k])
        for i in range(k, len(nums)):
            sl = (sl*k - nums[i-k]+nums[i])/k
            if sl > ans:
                ans = sl
        return ans
    

        