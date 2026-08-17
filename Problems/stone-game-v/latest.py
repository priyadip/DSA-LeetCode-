

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @cache
        def dfs(l, r):

            if l >= r:
                return 0

            ans = 0

            left = 0
            right = prefix[r + 1] - prefix[l]

            for k in range(l, r):

                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:

                    # Maximum possible = 2 * left
                    if ans >= 2 * left:
                        continue

                    ans = max(
                        ans,
                        left + dfs(l, k)
                    )

                elif left > right:

                    # Maximum possible = 2 * right
                    if ans >= 2 * right:
                        break

                    ans = max(
                        ans,
                        right + dfs(k + 1, r)
                    )

                else:

                    ans = max(
                        ans,
                        left + dfs(l, k),
                        right + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, n - 1)