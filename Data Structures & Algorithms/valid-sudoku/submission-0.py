class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # i = rows, j = columns
        i_dicts = [{} for item in board]
        j_dicts = [{} for item in board]
        square_dicts = [[{} for i in range(len(board)//3)] for j in range(len(board)//3)]
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] in i_dicts[i]:
                    if board[i][j] != '.':
                        return False
                    i_dicts[i][board[i][j]] += 1
                else:
                    i_dicts[i][board[i][j]] = 1
                if board[i][j] in j_dicts[j]:
                    if board[i][j] != '.':
                        return False
                    j_dicts[j][board[i][j]] += 1
                else:
                    j_dicts[j][board[i][j]] = 1
                
                if board[i][j] in square_dicts[i//3][j//3]:
                    if board[i][j] != '.':
                        return False
                    square_dicts[i//3][j//3][board[i][j]] += 1
                else:
                    square_dicts[i//3][j//3][board[i][j]] = 1
        return True