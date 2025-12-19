class Solution:
    def reverseBits(self, n: int) -> int:
        #you are shifting the result by left to make space then add the digit then shift the num to right to move on to the next digit

        result = 0 # start by zero
        for i in range(32): #32 bit integer
            result = result << 1 #shift left by 1 to make space
            result += (n & 1)  #0 will give 0 and 1 will give 1 so from end it will be processed but the bits will be reversed.
            n = n >> 1 #shift the number to right to move on to next digit
        
        return result #this integer will be the reverse bits number

        