class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)

        jobs = sorted(
            zip(startTime, endTime, profit),
            key=lambda x: x[1]
        )

        ends = [job[1] for job in jobs]

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            start, end, value = jobs[i - 1]

            # Find last job ending <= current start
            j = bisect_right(ends, start, hi=i - 1)

            take = dp[j] + value
            skip = dp[i - 1]

            dp[i] = max(take, skip)

        return dp[n]