class Solution:
    def countSubstrings(self, s: str) -> int:
        # Transform string
        t = "^#" + "#".join(s) + "#$"
        n = len(t)

        p = [0] * n

        center = 0
        right = 0
        count = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            # Expand
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            # Update center and right
            if i + p[i] > right:
                center = i
                right = i + p[i]

            # Every radius contributes this many palindromic substrings
            count += (p[i] + 1) // 2

        return count