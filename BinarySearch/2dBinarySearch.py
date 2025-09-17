# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        TotalElements = rows*columns #flattened matrix
        LeftElement = 0
        RightElement = TotalElements-1

        while (LeftElement  <= RightElement):
            MiddleIndex = ((LeftElement+RightElement) // 2)
            i = MiddleIndex//columns #Get the row
            j = MiddleIndex % columns #Get which column 
            #converting flattened to 2d space again


            middle_element = matrix[i][j]

            if middle_element == target:
                return True
            #immediately return true on matching
            elif middle_element < target:
                LeftElement = MiddleIndex + 1 #target is bigger then update left to check second half
            else:
                RightElement = MiddleIndex - 1 #target is smaller then update right to check smaller values
        return False
        #if it didnt find the target
