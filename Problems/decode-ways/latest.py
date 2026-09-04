class Solution:
    def numDecodings(self, s: str) -> int:
        prev2 = 1
        prev1 = 1

        for i in range(1, len(s) + 1):
            current = 0

            # One digit: s[i-1]
            if s[i - 1] != '0':
                current += prev1

            # Two digits: s[i-2:i]
            if i >= 2 and '10' <= s[i - 2:i] <= '26':
                current += prev2

            prev2, prev1 = prev1, current

        return prev1