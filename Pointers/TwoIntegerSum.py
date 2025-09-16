# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. 
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
# There will always be exactly one valid solution.

# Your solution must use 
# O(1) additional space.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #initializing our left right pointers here
        left,right = 0, len(numbers) -1 
        
        while(left<right):
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left+1,right+1] #return index 1 versions
            elif current_sum<target:
                left += 1 #keep adding left to get the sum
            else:
                right -= 1 #reduce the max num at the end to make target bigger
                            #abusing the sort thing
            
            #guaranteed to return 1 solution

        
        