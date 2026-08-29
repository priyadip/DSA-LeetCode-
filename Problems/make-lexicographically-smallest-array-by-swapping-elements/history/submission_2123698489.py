class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # Sort values while remembering their original indices.
        pairs = sorted((value, i) for i, value in enumerate(nums))

        ans = nums[:]
        start = 0

        while start < n:
            end = start

            # Find one connected component in value space.
            while (
                end + 1 < n
                and pairs[end + 1][0] - pairs[end][0] <= limit
            ):
                end += 1

            # Values in this component can be freely rearranged.
            values = [pairs[i][0] for i in range(start, end + 1)]
            indices = sorted(pairs[i][1] for i in range(start, end + 1))

            # Put the smallest values at the smallest indices.
            for idx, value in zip(indices, values):
                ans[idx] = value

            start = end + 1

        return ans
        