# QUESTION:
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}
        #dicionary to store the numbers
      for i,num in enumerate(nums):
        #iterating through the numbers with the index and numbers to find complement
        complement = target - num
        if complement in seen: #if it exists
            return [seen[complement],i]
        seen[num] = i #because we are returning the indices so in case it doesnt exist
        #num is this one and it is present in index i so in future 
        #another number can come and then return it along with the compement value found
        