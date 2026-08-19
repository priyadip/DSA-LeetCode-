class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << s)

        ans = 2 * (n - len(rows))

        left  = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        mid   = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        for mask in rows.values():
            if not (mask & left) and not (mask & right):
                ans += 2
            elif not (mask & left) or not (mask & mid) or not (mask & right):
                ans += 1

        return ans