
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0]*n for _ in range(m)]
        k %= (m*n)
        if k == 0:
            return grid

        for i in range(m):
            for j in range(n):
                ni = i if j+k <n else (i+(j+k)//n)%m
                nj = (j+k)%n
                ans[ni][nj] = grid[i][j]
        return ans