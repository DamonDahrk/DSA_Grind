class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0 
        while n:
            counter += n%2 #will be 1 for 1 and 0 for zero, so are counting for 1
            n = n >> 1 #shift to the right and get rid of the left most element 
        return counter #we can send the 1 addition back

        