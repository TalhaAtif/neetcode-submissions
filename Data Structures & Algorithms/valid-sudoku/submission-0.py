class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for i in range(9):
            rows = set()
            for j in range(9):
                if board[i][j] != ".":
                    if (board[i][j]) in rows:
                        return False
                    rows.add(board[i][j])
        for i in range(9):
            cols = set()
            for j in range(9):
                if board[j][i] != ".":
                    if (board[j][i]) in cols:
                        return False
                    cols.add(board[j][i])
        for i in range(9):
            box = set()
            for j in range(9):
                r = (i // 3) * 3 + (j // 3)
                c = (i % 3) * 3 + (j % 3)
                if board[r][c] != ".":
                    if board[r][c] in box:
                        return False
                    box.add(board[r][c])
                
        return True