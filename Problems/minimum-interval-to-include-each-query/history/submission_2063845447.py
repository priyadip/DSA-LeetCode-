from heapq import heappush, heappop
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        qs = sorted((q, i) for i, q in enumerate(queries))

        an = [-1] * len(queries)
        heap = []
        i = 0

        for q, idx in qs:

            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heappush(heap, (r - l + 1, r))
                i += 1

            while heap and heap[0][1] < q:
                heappop(heap)

            if heap:
                an[idx] = heap[0][0]

        return an