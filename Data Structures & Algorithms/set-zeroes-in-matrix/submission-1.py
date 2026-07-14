class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        visited_rows = set()
        visited_cols = set()

        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    visited_rows.add(i)
                    visited_cols.add(j)

        for i in visited_rows:
            for j in range(0,n):
                matrix[i][j] = 0
        
        for j in visited_cols:
            for i in range(0,m):
                matrix[i][j] = 0

                    