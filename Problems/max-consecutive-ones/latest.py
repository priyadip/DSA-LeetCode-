class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cn = ans = 0
        for num in nums:
            if num == 1:
                cn += 1
                ans = max(ans, cn)
            else:
                cn = 0
            
        return ans


        