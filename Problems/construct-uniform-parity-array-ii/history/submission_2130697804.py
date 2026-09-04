class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')

        for x in nums1:
            if x & 1:
                min_odd = min(min_odd, x)

        # All numbers are already even
        if min_odd == float('inf'):
            return True

        # Every even number must have a smaller odd number
        for x in nums1:
            if ~x & 1 and x <= min_odd:
                return False

        return True