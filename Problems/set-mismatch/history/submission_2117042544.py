class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check = set()
        n = len(nums)
        for num in nums:
            if num in check:
                dup = num
            else:
                check.add(num)
        mis  = n*(n+1)//2 - sum(check)
        return [dup,mis]
