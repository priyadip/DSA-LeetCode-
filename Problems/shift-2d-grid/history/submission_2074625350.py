class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0]*n for _ in range(m)]
        k %= m*n

        for i in range(m):
            for j in range(n):
                ni = (i+(j+k)//n)%m
                nj = (j+k)%n
                ans[ni][nj] = grid[i][j]
        return ans 



        