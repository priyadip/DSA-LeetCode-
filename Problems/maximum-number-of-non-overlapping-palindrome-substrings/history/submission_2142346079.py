class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        n = len(s)

        # --------------------------------------------------
        # Manacher: odd-length palindromes
        # d1[i] = radius of longest odd palindrome centered at i
        # --------------------------------------------------
        d1 = [0] * n

        l = 0
        r = -1

        for i in range(n):
            if i > r:
                k1 = 1
            else:
                k1 = min(d1[l + r - i], r - i + 1)

            while (
                i - k1 >= 0
                and i + k1 < n
                and s[i - k1] == s[i + k1]
            ):
                k1 += 1

            d1[i] = k1

            if i + k1 - 1 > r:
                l = i - k1 + 1
                r = i + k1 - 1

        # --------------------------------------------------
        # Manacher: even-length palindromes
        # d2[i] = radius of longest even palindrome
        # centered between i-1 and i
        # --------------------------------------------------
        d2 = [0] * n

        l = 0
        r = -1

        for i in range(n):
            if i > r:
                k2 = 0
            else:
                k2 = min(d2[l + r - i + 1], r - i + 1)

            while (
                i - k2 - 1 >= 0
                and i + k2 < n
                and s[i - k2 - 1] == s[i + k2]
            ):
                k2 += 1

            d2[i] = k2

            if i + k2 - 1 > r:
                l = i - k2
                r = i + k2 - 1

        # --------------------------------------------------
        # Check whether s[l:r+1] is palindrome.
        # We only call this for length k or k+1.
        # --------------------------------------------------
        def is_palindrome(left, right):
            length = right - left + 1

            if length & 1:  # odd
                center = (left + right) // 2
                return d1[center] >= (length + 1) // 2

            else:  # even
                center = (left + right + 1) // 2
                return d2[center] >= length // 2

        # --------------------------------------------------
        # DP
        #
        # dp[i] = maximum number of non-overlapping
        # palindromes in s[0:i]
        # --------------------------------------------------
        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            # Don't use a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # ------------------------------------------------
            # Case 1: palindrome of length k
            # ------------------------------------------------
            if i >= k:
                if is_palindrome(i - k, i - 1):
                    dp[i] = max(
                        dp[i],
                        dp[i - k] + 1
                    )

            # ------------------------------------------------
            # Case 2: palindrome of length k + 1
            # ------------------------------------------------
            if i >= k + 1:
                if is_palindrome(i - k - 1, i - 1):
                    dp[i] = max(
                        dp[i],
                        dp[i - k - 1] + 1
                    )

        return dp[n]