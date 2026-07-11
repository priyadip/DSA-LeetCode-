from heapq import heappush, heappop

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        q = sorted((x, i) for i, x in enumerate(queries))

        ans = [-1] * len(queries)
        heap = []

        i = 0

        for query, idx in q:

            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i]
                heappush(heap, (r - l + 1, r))
                i += 1

            while heap and heap[0][1] < query:
                heappop(heap)

            if heap:
                ans[idx] = heap[0][0]

        return ans
        