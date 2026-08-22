class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cn = ans = 0
        for num in nums:
            if num == 1:
                cn += 1
            else:
                cn = 0
            ans = max(ans, cn)
        return ans


        