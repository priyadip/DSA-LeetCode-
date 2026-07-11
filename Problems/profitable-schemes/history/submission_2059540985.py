class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        from functools import cache
        mod = 10**9 + 7
        @cache
        def fn(i, p, minc):
            if i >= len(group):
                return 1 if minc == minProfit else 0
            ways = fn(i+1,p,minc)
            if p+group[i]<=n:
                new = min(minProfit, minc+profit[i])
                ways+= fn(i+1, p+group[i], new)
            return ways%mod
        return fn(0,0,0)
        