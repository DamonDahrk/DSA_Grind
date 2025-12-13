class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = {} #ith index for s for the string to compared the subseq for, jth index for the subseq string

        def dfs(i,j):
            #base cases:
            if j == len(t):
                return 1 #completed the subseq strong wholly so return 1 way discovered 
            if i == len(s):
                return 0 #we have completed the main string but not the subseq so no way of continuing 
            

            if (i,j) in dp:
                return dp[(i,j)] #stop repetition 
            
            if s[i] == t[j]: #if the string matches, then move ahead index for both but also what if the next string matches the subseq
                dp[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:             #if it doesnt match go on anyways to check again 
                dp[(i,j)] = dfs(i+1,j) 
            
            return dp[(i,j)]
        
        return dfs(0,0)
        