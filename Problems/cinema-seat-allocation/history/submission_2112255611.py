class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rs = {tuple(x) for x in reservedSeats}

        rows = {x[0] for x in reservedSeats}

        c = 2 * (n - len(rows))

        for i in rows:
            alc = set()

            for j in range(2, 10):
                if (i, j) not in rs:
                    alc.add(j)

            if {2, 3, 4, 5, 6, 7, 8, 9} <= alc:
                c += 2
            elif ({4, 5, 6, 7} <= alc) or ({2, 3, 4, 5} <= alc) or ({6, 7, 8, 9} <= alc):
                c += 1

        return c




        