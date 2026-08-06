
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        keep = 0
        swap = 1

        for i in range(1, len(nums1)):
            keep_new = float("inf")
            swap_new = float("inf")

            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                keep_new = keep
                swap_new = swap + 1

            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                keep_new = min(keep_new, swap)
                swap_new = min(swap_new, keep + 1)

            keep, swap = keep_new, swap_new

        return min(keep, swap)