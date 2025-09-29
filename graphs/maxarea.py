# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #same problem as before but with a twist
        max_area = 0

        rows, cols = len(grid), len(grid[0])

        def AdjacentIslandSizeCalculator(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]!= 1: #previous problem had "1" #watch out so int is valid here
                return 0
            else:
                grid[i][j] = 0 #mark the fact that you have visited the place already to avoid revisiting
                return (1 + AdjacentIslandSizeCalculator(i+1,j)
                         + AdjacentIslandSizeCalculator(i-1,j)
                         + AdjacentIslandSizeCalculator(i,j-1)
                         + AdjacentIslandSizeCalculator(i,j+1))
 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area,AdjacentIslandSizeCalculator(i,j))


        return max_area
        