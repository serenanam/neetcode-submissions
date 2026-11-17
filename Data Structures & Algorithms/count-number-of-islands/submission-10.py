class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cnt = 0
        def dfs(i, j):
            if i < 0 or i >= R or j < 0 or j >= C or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            for r, c in dirs:
                nr, nc = i+r, j+c
                dfs(nr, nc)

        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt