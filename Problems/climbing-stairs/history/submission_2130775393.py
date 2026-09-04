class Solution:
    def climbStairs(self, n: int) -> int:

        @lru_cache(None)
        def solve(i):
            if i <= 1:
                return 1

            return solve(i - 1) + solve(i - 2)

        return solve(n)