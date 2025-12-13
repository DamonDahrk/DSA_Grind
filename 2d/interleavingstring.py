class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {} #here we will use memoization solutions again because its easier
                #i and j will have the index for str 1 and str 2 respectively 
                # i + j should have the str 3 position depending on sitch 

        def backtracktree(i,j):
            if i >= len(s1) and j>= len(s2):
                return True 
            #immediately send True for completion of substrings for later inner nests, caching helps reduce work

            if (i,j) in dp:
                return dp[(i,j)] 
            #prevent too much repetition

            if i < len(s1) and s1[i] == s3[i+j] and backtracktree(i+1,j): #as long as its under s1 length and the character matches go ahead on that 
                return True
            if i < len(s2) and s2[j] == s3[i+j] and backtracktree(i,j+1):
                return True
            
            dp[(i,j)] = False #this position doesnt have any matching string 
            return False
        
        return backtracktree(0,0)
