# You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

# Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #no more duplicates to be used here unless and until it is used in the list itself
        res, subsetsum = [],[]
        candidates.sort()
        #sort it to find possible duplicates 

        def backtrack(start,current_sum): #start here which will show the levels and the branch we are on
            if current_sum == target:
                res.append(subsetsum[:])
                return
            if current_sum>target:
                return
            for i in range (start,len(candidates)):
                if  i>start and candidates[i] == candidates[i-1]:
                    continue  #duplicates within array found and on a new level so we are ignoring it because 
                              #it was explored on a prior level
                subsetsum.append(candidates[i])    #add the element in the path
                backtrack(i+1,current_sum+candidates[i]) #here i+1 instead of i since we can use one element at most
                                                        #only one time 
                subsetsum.pop() #pop it to revisit other paths
                
        backtrack(0,0)
        return res
        