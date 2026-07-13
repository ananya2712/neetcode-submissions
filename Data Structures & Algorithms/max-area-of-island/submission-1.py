class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(row,col):
            if row < 0 or col < 0 or row ==m or col == n or (row,col) in visited or grid[row][col]==0:
                return 0
            
            visited.add((row,col))
            return 1 + dfs(row+1,col) + dfs(row -1, col) + dfs(row, col+1) + dfs(row,col-1)

        area = 0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 1:
                    area = max(area,dfs(i,j))
        return area
            



            