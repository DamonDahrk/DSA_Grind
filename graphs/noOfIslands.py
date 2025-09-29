# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        number_of_islands = 0

        def CheckAdjacentLandArea(i,j):
            if i>=rows or i<0 or j<0 or j>=cols or grid[i][j] != '1': #indexes go till lastplace - 1
                return
            else:
                grid[i][j] = 0
                CheckAdjacentLandArea(i,j+1) #check for all corresponding adjacent lands for similar then we set them
                CheckAdjacentLandArea(i,j-1) #as zero as we are only counting seperate islands and not connected land
                CheckAdjacentLandArea(i+1,j)
                CheckAdjacentLandArea(i-1,j)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                  number_of_islands += 1
                  CheckAdjacentLandArea(i,j) #simple loop to check for valid isolated islands

        return number_of_islands       