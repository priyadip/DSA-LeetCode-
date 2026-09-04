class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x & 1:          # odd
                min_odd = min(min_odd, x)
            else:              # even
                min_even = min(min_even, x)

        # No odd numbers
        if min_odd == float('inf'):
            return True

        return min_even > min_odd