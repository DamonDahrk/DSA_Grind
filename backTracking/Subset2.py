# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

# The solution must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: nums = [1,2,1]

# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #every subset is valid here so dont even bother checking len(nums) == i limit 
        #we want to print every node save the duplicate 
        nums.sort()

        res,subset = [],[]
        def backtrack(start): #to remove the duplicate level later
            res.append(subset[:])  #empty subset counts

            for i in range (start,len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue  #duplicate found on the next level as the previous one so ignore the loop this time

                subset.append(nums[i]) #otherwise add the num to the subset  and get the other elements
                backtrack(i+1)
                subset.pop()    #pop to backtrack afterwards for other paths
            
        backtrack(0)
        return res


        
        