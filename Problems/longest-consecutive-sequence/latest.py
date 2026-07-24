class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # s = set(nums)

        # ans = 0

        # for num in s:

        #     if num - 1 not in s:

        #         length = 1

        #         while num + length in s:
        #             length += 1

        #         ans = max(ans, length)

        # return ans

        s = set(nums)
        ans = 0

        for num in s:
            if num - 1 not in s:
                curr = num

                while curr in s:
                    curr += 1

                ans = max(ans, curr - num)

        return ans
        