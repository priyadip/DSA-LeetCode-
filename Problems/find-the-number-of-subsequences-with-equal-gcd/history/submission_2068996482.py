from math import gcd
class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9+7
        n = len(nums)
        if n == 0: 
            return 0
        D = max(nums) + 1  # bounds for gcd values
        
        # Precompute GCD table [0..D)
        gcd_table = [[0]*D for _ in range(D)]
        for i in range(D):
            for j in range(D):
                # iterative Euclid is faster than math.gcd in loop
                a, b = i, j
                while b:
                    a, b = b, a % b
                gcd_table[i][j] = a
        
        # DP arrays (flattened 2D: idx = x*D + y)
        size = D*D
        cur = [0]*size
        cur[0] = 1  # dp[0][0] = 1
        
        for v in nums:
            nxt = [0]*size
            for x in range(D):
                base = x * D
                for y in range(D):
                    cnt = cur[base + y]
                    if cnt:
                        # 1) Skip v
                        nxt[base + y] = (nxt[base + y] + cnt) % MOD
                        # 2) Add v to seq1
                        nx = gcd_table[x][v]
                        nxt[nx * D + y] = (nxt[nx * D + y] + cnt) % MOD
                        # 3) Add v to seq2
                        ny = gcd_table[y][v]
                        nxt[base + ny] = (nxt[base + ny] + cnt) % MOD
            cur = nxt
        
        # Sum dp[g][g] for g>=1
        ans = 0
        for g in range(1, D):
            ans = (ans + cur[g*D + g]) % MOD
        return ans
