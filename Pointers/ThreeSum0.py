# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        Result = []
        #We are gonna be adding the result set here and returning it
        nums.sort()
        #sort to get our logic going

        for i,a in enumerate(nums):
            if i>0 and nums[i-1] == a:
                continue 
            #since it is sorted if the previous num is same as the new num skip the loop
            left,right = i+1,len(nums)-1
            #making the index at last and first respectively 
            #the threesum to run our test against
            while left<right:
                threesum = a + nums[left] + nums[right]
            #threesum inside while loop to get sums
                if threesum > 0:  #reduce max number at the end
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    Result.append([a,nums[left],nums[right]])
                #now for any possible future sums
                
                    left += 1 #to find another sum
                    #right not needed to update in this case 
                    while(nums[left] == nums[left-1] and left<right):
                        left += 1
                #keep shifting values for equal left value
        return Result

        