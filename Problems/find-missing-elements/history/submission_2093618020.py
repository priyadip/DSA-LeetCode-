class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        L = []
        ma, mi = max(nums), min(nums)
        while ma != mi:
            if mi not in nums:
                L.append(mi)
            mi += 1
        return L 
        