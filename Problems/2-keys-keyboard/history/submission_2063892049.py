class Solution:
    def minSteps(self, n: int):

        INF = float('inf')

        dp = [[INF] * (n + 1) for _ in range(n + 1)]

        # Base case
        for clip in range(n + 1):
            dp[n][clip] = 0

        for curr in range(n - 1, 0, -1):
            for clip in range(n, -1, -1):

                ans = INF

                # Copy All
                if curr != clip:
                    ans = min(ans, 1 + dp[curr][curr])

                # Paste
                if clip and curr + clip <= n:
                    ans = min(ans, 1 + dp[curr + clip][clip])

                dp[curr][clip] = ans

        return dp[1][0]