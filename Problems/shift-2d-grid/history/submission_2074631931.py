class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        if k == 0:
            return grid

        # Helper: swap two elements given their linear indices
        def swap(i, j):
            ri, ci = divmod(i, n)
            rj, cj = divmod(j, n)
            grid[ri][ci], grid[rj][cj] = grid[rj][cj], grid[ri][ci]

        # Reverse a range [start, end] (both inclusive)
        def reverse(start, end):
            while start < end:
                swap(start, end)
                start += 1
                end -= 1

        # Three-step reversal
        reverse(0, total - 1)        # reverse whole
        reverse(0, k - 1)            # reverse first k
        reverse(k, total - 1)        # reverse rest

        return grid