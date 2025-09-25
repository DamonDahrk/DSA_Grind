# Input: nums = [1,2,3]

# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res,permutations = [],[] 

        def perm():
            if len(permutations) == len(nums):
                res.append(permutations[:])  #add only when the perm has same units as the nums representing
                                            #permutations that are unique 
                return
            
            for x in nums:
                if x not in permutations:
                    permutations.append(x) #add if the element is not there
                    perm()              #recursion starts 
                    permutations.pop()  #once all elements exhausted pop for a different combo or path
        
        perm()
        return res
        