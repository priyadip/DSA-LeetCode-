class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        ans = 0

        for x in nums:
            need = k - x

            if freq.get(need, 0) > 0:
                ans += 1
                freq[need] -= 1
            else:
                freq[x] = freq.get(x, 0) + 1

        return ans