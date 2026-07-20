from math import gcd
from typing import List

MOD = 10**9 + 7

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        # Precompute GCD table for speed (0<=a,b<=200)
        MAX = 200
        gcd_table = [[0]*(MAX+1) for _ in range(MAX+1)]
        for i in range(MAX+1):
            for j in range(MAX+1):
                gcd_table[i][j] = gcd(i, j)

        n = len(nums)
        if n == 0:
            return 0

        max_num = max(nums)
        # dp[x][y] = number of ways (so far) with GCD(seq1)=x, GCD(seq2)=y
        dp = [[0]*(max_num+1) for _ in range(max_num+1)]
        dp[0][0] = 1

        for num in nums:
            new_dp = [row[:] for row in dp]  # copy current dp
            for g1 in range(max_num+1):
                for g2 in range(max_num+1):
                    cur = dp[g1][g2]
                    if cur == 0:
                        continue
                    # 1. Skip 'num' (already accounted in new_dp via copy).
                    # 2. Put num in subsequence1:
                    ng1 = num if g1 == 0 else gcd_table[g1][num]
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + cur) % MOD
                    # 3. Put num in subsequence2:
                    ng2 = num if g2 == 0 else gcd_table[g2][num]
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + cur) % MOD
            dp = new_dp

        # Sum over gcd=g for g>=1
        ans = 0
        for g in range(1, max_num+1):
            ans = (ans + dp[g][g]) % MOD
        return ans


