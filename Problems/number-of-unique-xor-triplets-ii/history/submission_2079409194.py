class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX = 2048

        dp = [False] * MAX
        dp[0] = True

        for _ in range(3):
            ndp = [False] * MAX

            for x in range(MAX):
                if dp[x]:
                    for v in nums:
                        ndp[x ^ v] = True

            dp = ndp

        return sum(dp)
        