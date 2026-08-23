class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check = set()
        for num in nums:
            if num in check:
                dup = num
            else:
                check.add(num)
        for num in range(1, len(nums)+1):
            if num not in check:
                mis = num
                break
        return [dup,mis]
