class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = {}

        for r, s in reservedSeats:
            reserved.setdefault(r, set()).add(s)

        ans = 2 * (n - len(reserved))

        for seats in reserved.values():
            left = not (seats & {2, 3, 4, 5})
            right = not (seats & {6, 7, 8, 9})
            middle = not (seats & {4, 5, 6, 7})

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans




        