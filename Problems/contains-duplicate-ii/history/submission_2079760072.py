class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}

        for i, x in enumerate(nums):
            if x in last and i - last[x] <= k:
                return True

            last[x] = i

        return False