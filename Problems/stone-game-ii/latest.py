class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dfs(i: int, M: int) -> int:
            if i >= n:
                return 0

            if i + 2 * M >= n:
                return suffix[i]

            ans = 0

            for X in range(1, 2 * M + 1):
                ans = max(
                    ans,
                    suffix[i] - dfs(i + X, max(M, X))
                )

            return ans

        return dfs(0, 1)