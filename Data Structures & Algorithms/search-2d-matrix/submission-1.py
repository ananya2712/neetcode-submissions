class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0 
        j = len(matrix[0]) - 1
        m = len(matrix)

        while i < m and j >= 0:
            if matrix[i][j] > target:
                j = j - 1
            elif matrix[i][j] < target:
                i = i + 1
            else:
                return True
        
        return False
