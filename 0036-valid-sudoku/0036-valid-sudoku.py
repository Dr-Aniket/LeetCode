class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = [[int(col) if col != '.' else 0 for col in row] for row in board]

        def valid(arr):
            count = []
            for ele in arr:
                if not ele:
                    continue
                if ele in count:
                    return False
                else:
                    count.append(ele) 
                
                if ele<1 or ele>9:
                    return False
            
            return True

        for i in range(9):
            if not valid(board[i]):
                return False
            elif not valid([row[i] for row in board]):
                return False
                
            x = i//3 * 3
            y = i %3 * 3
            arr = board[x][y:y+3] + board[x+1][y:y+3] + board[x+2][y:y+3]

            if not valid(arr):
                return False
        
        return True