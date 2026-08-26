class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, c in enumerate(s) if c == '1']

        if len(ones) < k:
            return ""

        best = ""

        for i in range(len(ones) - k + 1):
            curr = s[ones[i]:ones[i + k - 1] + 1]

            if not best or len(curr) < len(best) or (
                len(curr) == len(best) and curr < best
            ):
                best = curr

        return best