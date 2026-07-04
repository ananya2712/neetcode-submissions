from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        q = collections.deque()
        visit = set()

        # count chests
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 :
                    q.append([i,j]) 
                    visit.add((i,j))
        
        def addCell(r,c):
            if r < 0 or c < 0 or r == m or c == n or (r,c) in visit or grid[r][c] == -1:
                return 
            visit.add((r,c))
            q.append([r,c])


        # Multi source BFS
        dist = 0
        while q:
            length = len(q)
            for i in range(0,length):
                r,c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist = dist + 1
