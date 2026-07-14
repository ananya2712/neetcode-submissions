class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        fresh = 0
        time = 0 
        q = collections.deque()

        # calculate fresh fruits and rotten fruits
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh = fresh + 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        # multi source BFS
        while q and fresh:
            length = len(q)
            for i in range(0,length):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh = fresh - 1
            time = time + 1
        
        if fresh == 0:
            return time
        return -1  