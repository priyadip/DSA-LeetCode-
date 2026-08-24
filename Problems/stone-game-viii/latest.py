class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Prefix sums in-place
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # dp[n - 2] = total sum
        ans = stones[-1]

        for i in range(n - 2, 0, -1):
            ans = max(ans, stones[i] - ans)

        return ans