class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0
            # All non-empty subsets
            for mask in range(1, 1 << n):
                L = 1
                bits = 0
                for i in range(n):

                    if mask & (1 << i):
                        L = lcm(L, coins[i])
                        bits += 1
                # Number of multiples of L <= x
                ways = x // L
                # Inclusion-exclusion
                if bits % 2 == 1:
                    total += ways
                else:
                    total -= ways
            return total

        # Binary search
        left = 1
        right = min(coins) * k

        while left < right:
            mid = left + (right - left) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
        