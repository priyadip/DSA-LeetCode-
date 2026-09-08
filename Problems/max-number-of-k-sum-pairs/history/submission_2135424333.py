class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        j = len(nums) - 1
        ans = 0

        while i < j:
            total = nums[i] + nums[j]

            if total == k:
                ans += 1
                i += 1
                j -= 1
            elif total < k:
                i += 1
            else:
                j -= 1

        return ans