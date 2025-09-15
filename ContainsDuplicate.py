# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        TheSet = set() 
        for num in nums:
            if(num in TheSet):
                return True
            TheSet.add(num)
        return False

# Here we can see that converting the list to set then iterating thru to find element only once as we are adding in the set
# For every element not in the array set, so when it will find one already in set it will run only once
# Hence the Time complexity is o 1 