class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Transform string
        t = "^#" + "#".join(s) + "#$"
        n = len(t)

        # p[i] = radius of palindrome centered at i
        p = [0] * n

        center = 0
        right = 0

        max_len = 0
        max_center = 0

        for i in range(1, n - 1):

            # Mirror position of i around center
            mirror = 2 * center - i

            # If i is inside the current palindrome,
            # use previously calculated information
            if i < right:
                p[i] = min(right - i, p[mirror])

            # Try to expand palindrome around i
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            # If palindrome goes beyond right,
            # update center and right boundary
            if i + p[i] > right:
                center = i
                right = i + p[i]

            # Track longest palindrome
            if p[i] > max_len:
                max_len = p[i]
                max_center = i

        # Convert transformed-string indices back to original string
        start = (max_center - max_len) // 2

        return s[start:start + max_len]