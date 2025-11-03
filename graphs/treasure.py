class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
     if not grid or not grid[0]: #make sure the matrix is valid
        return 
     ROWS, COLS = len(grid), len(grid[0])
     INF = 2147483647
     q = deque() #here we will be storing all the valid treasure locations so we can find the land pos relative distance
                 #to the nearest treasure sources
     
     for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                q.append([r,c]) #storing the treasure coordinates in the deque 
     directions = ([0,1],[1,0],[-1,0],[0,-1]) #all adjacent directions

     while q: #while we have all treasure locations for BFS 
        for i in range(len(q)): #every unique treasure location will have its own source for the following land areas
                                #to traverse through 
            r,c = q.popleft() #location of earlier treasure location 
            for dr,dc in directions:
                row,col = dr+r, dc+c   #the below will automatically ignore the water cells i.e -1 i.e lower than 0
                #INF are only land cells that need to be updated and yet to be traversed.
                if ((row<0 or row == ROWS ) or (col<0 or col == COLS) or grid[row][col]!= INF):
                    continue
                grid[row][col] = grid[r][c] + 1 #update the distance of the nearest treasure
                q.append([row,col]) #now can add this new distance in q and keep doing it till we run out of INF tiles
                


     