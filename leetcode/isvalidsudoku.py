class Solution(object):
    
    def is_valid_cell(self,cell_list):
        cell = [cell for cell in cell_list if cell != "."]
        return len(cell) == len(set(cell))
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check if row is valid
        for row in board:
            row_valid = self.is_valid_cell(row)
            
        for col in zip(*board):
            col_valid = self.is_valid_cell(row)
            
        seen=[x for i, row in enumerate(board) 
                for j, c in enumerate(row) 
                    if c!='.' 
                        for x in ((c,i),(j,c),(i//3,j//3,c))]
             
        return seen
        
sol = Solution()
output = sol.isValidSudoku([
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
output
print(output)