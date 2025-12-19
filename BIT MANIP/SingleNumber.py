class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        base = 0   #base case for XOR case for the On and O1 space
        for x in nums:
            base ^= x   #bitwise XOR operate will remove all non single toons return the single char in the array
        return base
        