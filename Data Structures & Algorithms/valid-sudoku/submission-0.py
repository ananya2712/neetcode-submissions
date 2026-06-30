class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validRow = True
        validCol = True
        validSquare = True

        # check rows valid 
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s and board[i][j]!='.':
                    validRow = False
                else:
                    s.add(board[i][j])

        # check if cols valid 
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s and board[j][i]!='.':
                    validCol = False
                else:
                    s.add(board[j][i])

        # check if squares valid
        for square in range(9):
            s = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in s:
                        validSquare = False
                    s.add(board[row][col])

        return validRow and validCol and validSquare