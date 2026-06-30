class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        q = collections.deque()
        time = 0

        # count fresh
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        # multi-source bfs
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr,dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh = fresh - 1
            time = time + 1

        if fresh == 0:
            return time
        return -1


        