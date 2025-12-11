class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n #making the base row wrt columns
        #this is already bottom row

        for i in range(m-1): #thats why range is m-1
            newRow = [1] * n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1] + row[j] #the row j will have data directly below
            row = newRow #update the data of row for the future below data

        
        return row[0]
        #after all said and done row 0 should have possible way to target m-1,n-1 cuz
        #of backtrack from col end
        