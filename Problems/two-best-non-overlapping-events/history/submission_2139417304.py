class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort by start time
        events.sort()

        n = len(events)

        # start_times[i] = start time of event i
        start_times = [event[0] for event in events]

        # suffix_max[i] = maximum value among events i ... n-1
        suffix_max = [0] * n

        suffix_max[n - 1] = events[n - 1][2]

        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])

        ans = 0

        for start, end, value in events:

            # First event whose start time > end
            j = bisect_right(start_times, end)

            # Take current event + best compatible event
            if j < n:
                ans = max(ans, value + suffix_max[j])

            # We can also attend only this event
            ans = max(ans, value)

        return ans
        