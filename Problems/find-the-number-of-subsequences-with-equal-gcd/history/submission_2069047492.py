from math import gcd

MOD = 10**9 + 7

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        maxv = max(nums)

        # Precompute gcd table
        gcd_table = [[0] * (maxv + 1) for _ in range(maxv + 1)]
        for a in range(maxv + 1):
            for b in range(maxv + 1):
                gcd_table[a][b] = gcd(a, b)

        # dp[x][y] = number of ways with gcd(seq1)=x, gcd(seq2)=y
        dp = [[0] * (maxv + 1) for _ in range(maxv + 1)]
        dp[0][0] = 1

        for num in nums:
            newdp = [[0] * (maxv + 1) for _ in range(maxv + 1)]

            for x in range(maxv + 1):
                for y in range(maxv + 1):
                    cur = dp[x][y]
                    if cur == 0:
                        continue

                    # 1. Skip this element
                    newdp[x][y] = (newdp[x][y] + cur) % MOD

                    # 2. Put in first subsequence
                    new_x = gcd_table[x][num]
                    newdp[new_x][y] = (newdp[new_x][y] + cur) % MOD

                    # 3. Put in second subsequence
                    new_y = gcd_table[y][num]
                    newdp[x][new_y] = (newdp[x][new_y] + cur) % MOD

            dp = newdp

        ans = 0
        for g in range(1, maxv + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans