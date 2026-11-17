class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[i][j] in nums:
                    return False
                if board[i][j] != ".":
                    nums.add(board[i][j])
        
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[j][i] in nums:
                    return False
                if board[j][i] != ".":
                    nums.add(board[j][i])
        
        
        for i in range(9):
            if(i%3 == 0):
                s1, s2, s3 = set(), set(), set()
            for j in range(9):
                if j < 3:
                    if board[i][j] in s1:
                        return False
                    if board[i][j] != ".":
                        s1.add(board[i][j])
                elif j < 6:
                    if board[i][j] in s2:
                        return False
                    if board[i][j] != ".":
                        s2.add(board[i][j])
                else:
                    if board[i][j] in s3:
                        return False
                    if board[i][j] != ".":
                        s3.add(board[i][j])
        return True
        # time: O(n^2)
        # space: O(1) - constant bc wc. 9 * 4
                