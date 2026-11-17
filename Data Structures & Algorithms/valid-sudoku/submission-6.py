class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        for i in range(9):
            rows = set()
            cols = set()
            for j in range(9):
                if board[i][j] in rows or board[j][i] in cols or board[i][j] in squares[(i//3, j//3)]:
                    return False
                
                if board[j][i] != ".":
                    cols.add(board[j][i])
                
                if board[i][j] == ".":
                    continue
                rows.add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])
        
        return True
        # time: O(n^2)
        # space: O(1) - constant bc wc. 9 * 4
                