# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Lets map the board at first 
        ROWS, COLS = len(board) , len(board[0]) #columns and rows in the board
        wordsection = set()

        def dfs(r,c,i):
            if i == len(word):
                return True #we have reached the end of the word succesfully
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in wordsection:
                #if somehow the rows are less than 0 or it exceeds the board or the word is not found 
                #or the character/in that specific index is already present in the section then
                
                return False 

            wordsection.add((r,c))
            res = (dfs(r+1,c,i+1) or #check all possible positions from the index to see what returns true or if it is valid
            dfs(r-1,c,i+1) or 
            dfs(r,c+1,i+1) or 
            dfs(r,c-1,i+1)) 
            wordsection.remove((r,c))
            #clean up for backtracking and adding to res

            return res #return the correct path so we can check all possible positions from this point onwards and 
                        #ignore the other position
        
        for r in range (0,ROWS):
            for c in range (0,COLS):
                if dfs(r,c,0):
                    return True
        
        return False
            

        