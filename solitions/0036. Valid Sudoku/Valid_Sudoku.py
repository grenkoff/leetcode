# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        res = []
        for row in range(9):
            for col in range(9):
                element =board[row][col]
                if element != '.':
                    res += [(row,element),(element,col),(row//3,col//3,element)]
                    if len(res) != len(set(res)):
                        return False
        return True


a = Solution()

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(a.isValidSudoku(board))
