class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        #max lengths 

        def capture(r,c):
            if ((r < 0 or r == ROWS) or (c < 0 or c == COLS) or board[r][c]!= 'O'):
             return
            board[r][c] = 'T' #Assigning a a temp value for the non connected O cells i.e present in the border
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c-1)
            capture(r,c+1) #backtracking to check any adjacent such values
        
        #check for border values to convert to T 

        for r in range(ROWS):
            for c in range(COLS):
                if (((board[r][c]) == 'O') and (r in [0,ROWS-1] or c in [0,COLS-1])):
                    capture(r,c)
        
        #now just convert non border O to X 

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        #now convert the T to Os again:

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
