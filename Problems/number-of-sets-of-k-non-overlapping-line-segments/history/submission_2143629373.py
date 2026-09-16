class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        MOD = 10**9 + 7

        r = 2 * k
        N = n + k - 1

        # dp[j] = C(current, j)
        dp = [0] * (r + 1)
        dp[0] = 1

        for i in range(1, N + 1):
            for j in range(min(i, r), 0, -1):
                dp[j] = (dp[j] + dp[j - 1]) % MOD

        return dp[r]