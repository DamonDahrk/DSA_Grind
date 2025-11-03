class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set() #we are creating two sets one of each ocean specifically
        atlantic = set() 
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r,c, visit, prevHeight):
            if (((r,c) in visit) or r<0 or r == ROWS or c<0 or c==COLS or heights[r][c]< prevHeight):
                return #break the backtracking cycle in case of the cells going out of bounds
                       #or if the previous value is greater as it should be lower since we are going to ocean to land
                       #it should be in increasing order
            visit.add((r,c)) #add the cell to the set of either pacific or atlantic respectively for set we use add instead
                            #of append
            dfs(r+1,c,visit,  heights[r][c]) #this is to make sure its a valid cell for going to either ocean and flowing
                                             #as intended
            dfs(r-1,c,visit,  heights[r][c])
            dfs(r,c-1,visit,  heights[r][c])
            dfs(r,c+1,visit,  heights[r][c])
            #now we do backtracking for every possible cell from the selected cell 
        
        for c in range (COLS):
            dfs(0,c, pacific, heights[0][c])
            dfs(ROWS-1,c,atlantic,heights[ROWS-1][c])
        
        for r in range (ROWS):
            dfs(r,0, pacific, heights[r][0])
            dfs(r,COLS-1,atlantic,heights[r][COLS-1])
        
        results = [] 
        for r in range (ROWS):
            for c in range (COLS):
                if ((r,c) in pacific) and ((r,c) in atlantic): #if valid cells exist for both then add in result only then
                    results.append([r,c])
            
        return results


