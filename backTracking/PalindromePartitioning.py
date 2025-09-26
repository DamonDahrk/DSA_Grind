
# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

# You may return the solution in any order.

# Example 1:

# Input: s = "aab"

# Output: [["a","a","b"],["aa","b"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,partition = [],[]

        def dfs(i):
            if i >= len(s):
                res.append(partition[:]) #we have found all possible valid palindromes in one path in decision tree
                                         # and are now appending it from the dfs
                return 
            
            for j in range (i,len(s)):
                if self.isPalin(s,i,j): #if it is palindrome indeed then add the lower half and increase the string
                                        #limit to explore other paths, and check for more elements to add
                    partition.append(s[i:j+1]) #add that string 
                    dfs(j+1) #check for more elements to add from palin point 
                    partition.pop() #clean up while coming back from backtrack to explore other paths
        
        dfs(0)
        return res #should have all solutions found for the palindrome

    def isPalin(self, s,l,r):  #function to check if the string is palindrome or not
        while l < r:
            if s[l] != s[r]:
                return False
            l,r = l+1,r-1
        return True 
        
        