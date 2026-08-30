class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_i = max_i = 0

        for i in range(n):
            if nums[i] < nums[min_i]:
                min_i = i
            if nums[i] > nums[max_i]:
                max_i = i

        a, b = sorted((min_i, max_i))

        return min(
            b + 1,          # both from left
            n - a,          # both from right
            a + 1 + n - b   # one from each side
        )