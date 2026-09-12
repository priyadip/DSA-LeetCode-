class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # [left, right, weight, original_index]
        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by right endpoint
        arr.sort(key=lambda x: x[1])

        # All right endpoints
        ends = [x[1] for x in arr]

        # prev[i] = number of intervals whose right < arr[i].left
        prev = [0] * n

        for i in range(n):
            prev[i] = bisect_left(ends, arr[i][0])

        # dp[k][i] = (maximum score, sorted indices)
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):

                # Option 1: don't take current interval
                not_take = dp[k][i - 1]

                l, r, w, idx = arr[i - 1]

                # Option 2: take current interval
                p = prev[i - 1]

                old_score, old_indices = dp[k - 1][p]

                # Keep indices sorted for lexicographical comparison
                new_indices = tuple(sorted(old_indices + (idx,)))

                take = (
                    old_score + w,
                    new_indices
                )

                # Choose higher score
                if take[0] > not_take[0]:
                    dp[k][i] = take

                # Same score -> lexicographically smaller indices
                elif take[0] == not_take[0]:
                    dp[k][i] = min(take, not_take)

                else:
                    dp[k][i] = not_take

        return list(dp[4][n][1])

