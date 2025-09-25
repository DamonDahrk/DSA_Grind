class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #There is a decision tree to explore all subsets and then backtrack by poppoing

        res = [] #result set where values are inserted  

        subset = [] #every subset possible will be stored here globally 
        
        def dfs(i):
            if i >= len(nums): #the depth limit cannot be exceeded
                res.append(subset[:]) #copy of subset as it will be modified 
                return #the subset has exhausted the current path and is now appending variation to res

                #include path of including the elements and start the recursion
            subset.append(nums[i]) #nums for list 
            dfs(i+1)

                #after exhausted explore alternate path by not including the elements and start backtracking
            subset.pop() #get rid of the added element and go elsewhere 
            dfs(i+1)
        
        dfs(0)
        return res

        