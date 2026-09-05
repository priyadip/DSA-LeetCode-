
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        prefix_max = list(accumulate(nums, max))
        suffix_min = list(accumulate(nums[::-1], min))[::-1]

        for i in range(len(nums)):
            if prefix_max[i] - suffix_min[i] <= k:
                return i

        return -1
        