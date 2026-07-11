class Solution:
    def minSteps(self, n: int) -> int:

        def fn(curr, clip):

            if curr == n:
                return 0

            if curr > n:
                return float('inf')

            ans = float('inf')

            # Copy All
            if curr != clip:          # avoid useless repeated copy
                ans = min(ans, 1 + fn(curr, curr))

            # Paste
            if clip:
                ans = min(ans, 1 + fn(curr + clip, clip))

            return ans

        return fn(1, 0)
        