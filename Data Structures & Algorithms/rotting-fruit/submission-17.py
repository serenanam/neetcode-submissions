class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        fresh = 0
        q = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()                
                
                for i, j in dirs:
                    nr, nc = i+r, j+c
                    if nr >= 0 and nr < R and nc >= 0 and nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))  
                        fresh -= 1
            time += 1
        print(fresh)
        if fresh == 0:
            return time
        return -1

    
