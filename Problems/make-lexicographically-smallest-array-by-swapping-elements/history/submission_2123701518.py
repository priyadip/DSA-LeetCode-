class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        pairs = sorted((v, i) for i, v in enumerate(nums))
        n = len(nums)

        start = 0

        while start < n:
            end = start

            # Find the current connected component.
            while (
                end + 1 < n
                and pairs[end + 1][0] - pairs[end][0] <= limit
            ):
                end += 1

            # Extract only indices, then sort them.
            indices = sorted(i for _, i in pairs[start:end + 1])

            # Values are already sorted because `pairs` is sorted.
            for k, idx in enumerate(indices):
                nums[idx] = pairs[start + k][0]

            start = end + 1

        return nums