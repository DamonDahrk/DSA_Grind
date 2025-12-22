class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid) #for last r,c in the grid
        directions = [[1,0],[-1,0],[0,1],[0,-1]] 
        visit = set()  #count for the visited coords
        minHeap = [[grid[0][0],0,0]] #stores the values as [height/time,r,c]

        #WILL BE USING A MODIFIED DJIKSTRA'S algo where we count for the max prev node as well

        while minHeap:
            t,r,c = heapq.heappop(minHeap) #get the values popped first
            if (r,c) in visit:
                continue #avoid visiting previous coords
            visit.add((r, c))
            if r == N-1 and c == N-1 :
                return t #return the least amt of time to reach bottom right most grid
            
            for directionsROW, directionsCOL in directions:
                neighR = directionsROW + r
                neighC = directionsCOL + c 
                #now we have possible movement of our coords from grid pos
                if neighR < 0 or neighC < 0 or neighR >= N or neighC >= N or ((neighR,neighC) in visit):
                    continue #inbounds check and visit set checks
                
                heapq.heappush(minHeap,(max(t,grid[neighR][neighC]),neighR,neighC)) #INSERTS MAX VAL SO FAKE NEW MIN cannot overwrite
                                                                                    #as per problem requirement 