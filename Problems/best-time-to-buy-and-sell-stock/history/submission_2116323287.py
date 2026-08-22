class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_s = prices[0]
        max_p = 0
        for p in prices:
            max_p = max(max_p, p - min_s)
            min_s = min(min_s, p)
        return max_p
        