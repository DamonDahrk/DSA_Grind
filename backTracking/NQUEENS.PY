# The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

# A queen in a chessboard can attack horizontally, vertically, and diagonally.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

# You may return the answer in any order.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = [] #the result we will send at the end
        posDiag = set() #this will store (r+c) basically the r+c has to store double on origin or increment on every 
        negDiag = set() #diagonal, similarly negdiag will have (r-c), zero on origin or -ve on one end and +ve on other
        col = set() #we will try make sure once a queen is placed in a cell, that column cannot have another queen

        board = [['.'] * n  for i in range(n)] #creating the chess board

        def backtracking(r):
            if n == r:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag: #invalid position due to above mentioned reasons
                    continue 
                
                #VALID THEN ADD VALUES FOR FUTURE CHECKING
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtracking(r+1)

                #NOW CLEANUP FOR OTHER PATHS POSSIBILTIES
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        backtracking(0)
        return result

        