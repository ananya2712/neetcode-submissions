class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[1,0],[0,1],[0,-1],[-1,0]]

        components = 0

        def dfs(i,j):
            if i < 0 or j < 0 or j >= n or i >=m or grid[i][j] == '0':
                return 
            grid[i][j] = '0'
            for dr,dc in directions:
                dfs(i+dr, j+dc)
        
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    components +=1

        return components