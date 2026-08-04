class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [y for y in range(min(nums)+1, max(nums)) if y not in s]
        