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
                print(f'INVALID ROW')
                return False
            elif not valid([row[i] for row in board]):
                print('INVALID COL')
                return False
                
        for n in range(9):
            i = n//3*3
            j = n%3 * 3
            arr = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if not valid(arr):
                print('INVALID BOX')
                print(f'{n}\n{arr}')
                return False


        return True