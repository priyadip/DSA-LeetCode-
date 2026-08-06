class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        suffixSum = 0
        ans = 0

        for x in reversed(satisfaction):
            suffixSum += x

            if suffixSum <= 0:
                break

            ans += suffixSum

        return ans
        