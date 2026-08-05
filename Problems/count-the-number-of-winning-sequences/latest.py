class Solution:
    def countWinningSequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        OFFSET = n

        # score change = BobScore - AliceScore
        score = {
            ('F', 0): 0,
            ('F', 1): 1,
            ('F', 2): -1,

            ('W', 0): -1,
            ('W', 1): 0,
            ('W', 2): 1,

            ('E', 0): 1,
            ('E', 1): -1,
            ('E', 2): 0,
        }

        # dp[last][diff]
        cur = [[0] * (2 * n + 1) for _ in range(3)]

        # First move (no previous move restriction)
        for move in range(3):
            d = score[(s[0], move)]
            cur[move][OFFSET + d] = 1

        for i in range(1, n):
            nxt = [[0] * (2 * n + 1) for _ in range(3)]

            for last in range(3):
                for diff in range(-i, i + 1):
                    ways = cur[last][OFFSET + diff]
                    if ways == 0:
                        continue

                    for move in range(3):
                        if move == last:
                            continue

                        ndiff = diff + score[(s[i], move)]
                        nxt[move][OFFSET + ndiff] = (
                            nxt[move][OFFSET + ndiff] + ways
                        ) % MOD

            cur = nxt

        ans = 0
        for last in range(3):
            for diff in range(1, n + 1):
                ans = (ans + cur[last][OFFSET + diff]) % MOD

        return ans
        