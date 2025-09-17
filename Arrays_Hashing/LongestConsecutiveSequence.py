# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4


#Sorting is OnLogn we want to avoid that

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
#This is what we will return in case of a sequence found
        SetOfNumbers = set(nums)
        for number in SetOfNumbers:
            if(number-1 not in SetOfNumbers):
                #this will elimate any future sequence that
#already might exist to not overlap when finding the lowest number
#of that sequence
                length = 0
                while(number+length) in SetOfNumbers:
                    length += 1
        #check all consecutive numbers
                longest = max(longest,length)
        return longest
#return the longest sequence found
