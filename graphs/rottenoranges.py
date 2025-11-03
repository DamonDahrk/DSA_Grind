class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0 #the minimum time that will be taken to turn every orange rotten
                       #the fresh oranges left (if more than 0 after BFS then it returns -1)
        
        q = deque() #the deque where we will add the rotten values (multiple sources)

        ROWS , COLS = len(grid), len(grid[0]) #MAX LENGTH OF THE FRUIT MATRIX 

        for r in range (ROWS):
            for c in range (COLS):
                if grid[r][c] == 2:
                    q.append([r,c]) #adding the rotten oranges in the deque 
                if grid[r][c] == 1:
                    fresh += 1 #adding the fresh oranges counter for the entire matrix 

        directions = ([0,1],[1,0],[-1,0],[0,-1]) #all possible directions to traverse in the matrix

        while q and fresh > 0: #the main loop will run till all rotten are gone from deque and no fresh oranges are left
            for i in range(len(q)): #this makes sure that every rotten source is traced in one time unit 
                r,c = q.popleft() #get rid of the earliest rotten iteration from the matrix and not the latest and store
                for dr,dc in directions: #checking 4 directions
                    rows, cols = r+dr, c+dc 
                    #making sure the values are valid i.e in bounds and not already rotten 
                    if ((rows < 0 or rows == len(grid)) or
                     (cols < 0 or cols == len(grid[0]))
                     or (grid[rows][cols] != 1)):
                        continue
                    grid[rows][cols] = 2
                    fresh -= 1 #updating the fact that fresh orange has turned rotten 
                    q.append([rows,cols]) 
            time += 1    
        return time if fresh == 0 else -1


