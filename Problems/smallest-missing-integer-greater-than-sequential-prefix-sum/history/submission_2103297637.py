
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefixSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefixSum += nums[i]
            else:
                break

        s = set(nums)

        while prefixSum in s:
            prefixSum += 1

        return prefixSum