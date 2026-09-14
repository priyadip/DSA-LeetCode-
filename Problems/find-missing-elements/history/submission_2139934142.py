class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        se = set(nums)
        missing=[]
        for i in range(min(nums),max(nums)):
            if i not in se:
                missing.append(i)
        return missing

        