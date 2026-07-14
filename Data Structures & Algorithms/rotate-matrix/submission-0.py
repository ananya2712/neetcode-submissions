class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
    
        for i in range(0,n):
            for j in range(0,n):
                rotated[j][n-1-i] = matrix[i][j]
        
        for i in range(0,n):
            for j in range(0,n):
                matrix[i][j] = rotated[i][j]