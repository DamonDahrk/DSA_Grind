class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS,COLS = len(matrix),len(matrix[0]) #max len or row and col first

        dp = {} #gonna be storing the max path value here the key would be the index in the 2d matrix

        def dfs(r,c,previousValue):
            if r>=ROWS or c>= COLS or r<0 or c<0 or matrix[r][c] <= previousValue:
                return 0
            #making sure things are in bound and are not the same as the previous value.
            
            if (r,c) in dp:
                return dp[(r,c)] #this is where the soln goes from exponential to O(R × C)

            result = 1 #at a base level if there is no path counting the cell itself its 1 path only 
            result = max(result,1+dfs(r+1,c,matrix[r][c])) #traversing the matrix to see the possible increasing paths
            result = max(result,1+dfs(r-1,c,matrix[r][c]))
            result = max(result,1+dfs(r,c+1,matrix[r][c]))
            result = max(result,1+dfs(r,c-1,matrix[r][c]))

            dp[(r,c)] = result #store the result in incpath dp matrix 
            return result #return to start the backtracking
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)
        #start with negative value because its not possible then we will go through all possible starting points an inception
        
        return max(dp.values()) #get the max inc length here done.