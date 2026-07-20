class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for i, x in enumerate(sorted(set(arr)), 1):
            rank[x] = i
        return [rank[x] for x in arr]


        