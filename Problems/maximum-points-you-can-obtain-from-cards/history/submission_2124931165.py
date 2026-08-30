class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)

        window_size = n - k

        # Sum of the first window
        window_sum = sum(cardPoints[:window_size])
        min_window = window_sum

        # Sliding window
        for i in range(window_size, n):
            window_sum += cardPoints[i]
            window_sum -= cardPoints[i - window_size]

            min_window = min(min_window, window_sum)

        return sum(cardPoints) - min_window