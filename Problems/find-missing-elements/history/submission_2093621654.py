class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        L = []
        ma, mi = max(nums), min(nums)
        while ma != mi:
            if mi not in s:
                L.append(mi)
            mi += 1
        return L 
        