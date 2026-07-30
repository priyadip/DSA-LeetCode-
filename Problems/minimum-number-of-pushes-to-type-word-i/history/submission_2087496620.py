class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        return (
            min(n, 8)
            + max(0, min(n - 8, 8)) * 2
            + max(0, min(n - 16, 8)) * 3
            + max(0, n - 24) * 4
        )