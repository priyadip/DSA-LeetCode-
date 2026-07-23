
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        ans = []

        for f in range(len(bucket) - 1, 0, -1):
            for num in bucket[f]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        