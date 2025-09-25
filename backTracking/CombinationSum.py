# You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

# The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sumsubset = [], [] #starting the list for result where we will append stuff and subset sum here
        def backtrack(i,current_sum):
            if(current_sum==target): #the sum has been reached 
                res.append(sumsubset[:]) #send a copy of the valid subset in result 
                return
            if i==len(nums) or current_sum>target: #ignore the paths where the sum exceeds the target and 
                return                             #visited every single element to make sum

            backtrack(i+1,current_sum) #explore all the elements for the sums not include the elements

            sumsubset.append(nums[i]) #lets include this element to add to the combination sum
            backtrack(i,current_sum+nums[i]) #lets exhaust the paths with the numbers
                                             #stay where you are to avoid dups and make combinations with this
                                             #on staying you are adding the elem to the sum to meet target 
            
            sumsubset.pop() #remove upon finishing the element permu and explore other paths
            

            

        backtrack(0,0) #starting at the empty sum and first number 
        return res 
        