class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or not board[0]:
            return None

        def is_row_valid(i): # i: row index
            # board is passed from the outer function
            seen = set()
            for char in board[i]: # i should be valid
                if char == ".": # skip
                    continue
                # char is a digit '1' to '9'
                if char in seen:
                    return False
                seen.add(char)
            return True

        def is_col_valid(j): # j: column index
            seen = set()
            for i in range(len(board)):
                if board[i][j] == ".": # skip
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
            return True
        
        def is_subbox_valid(i, j): # provides the starting point
            seen = set()
            for di in range(0, 3):
                for dj in range(0, 3):
                    # it's assumed that the input is correct so the cells will not be out of bounds
                    current = board[i+di][j+dj]
                    if current == ".":
                        continue
                    if current in seen:
                        return False
                    seen.add(current)
            return True

        # check rows 
        for i in range(len(board)):
            if not is_row_valid(i):
                return False
    
        # check columns
        for j in range(len(board[0])):
            if not is_col_valid(j):
                return False

        # check subboxes
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                if not is_subbox_valid(i, j):
                    return False
                    
        return True