class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        pal = [False] * n
        dp = [0] * (n + 1)

        for r in range(n):
            dp[r + 1] = dp[r]

            for l in range(r + 1):

                # pal[l+1] is the palindrome status
                # of s[l+1:r] from the previous iteration.
                pal[l] = (s[l] == s[r] and (r - l <= 1 or pal[l + 1]))

                if pal[l] and r - l + 1 >= k:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)

        return dp[n]