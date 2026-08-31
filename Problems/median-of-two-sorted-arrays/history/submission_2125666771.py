class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            # Number of elements taken from nums1
            partition1 = (left + right) // 2

            # Number of elements taken from nums2
            partition2 = (m + n + 1) // 2 - partition1

            # Elements immediately around the partitions
            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right1 = float('inf') if partition1 == m else nums1[partition1]

            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == n else nums2[partition2]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                return (max(left1, left2) + min(right1, right2)) / 2

            # nums1 partition is too far right
            elif left1 > right2:
                right = partition1 - 1

            # nums1 partition is too far left
            else:
                left = partition1 + 1