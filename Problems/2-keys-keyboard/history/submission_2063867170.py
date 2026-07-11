from functools import cache

class Solution:
    def minSteps(self, n: int):

        @cache
        def fn(curr, clip):

            if curr == n:
                return 0

            if curr > n:
                return float('inf')

            ans = float('inf')

            if curr != clip:
                ans = min(ans, 1 + fn(curr, curr))

            if clip:
                ans = min(ans, 1 + fn(curr + clip, clip))

            return ans

        return fn(1, 0)