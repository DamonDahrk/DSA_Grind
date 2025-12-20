class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {} #required to prevent repeated computations
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)] #return result of existing stuff
            if i >= len(s) and j >= len(p):
                return True            
            if j >= len(p):
                return False # we are comparing s with pattern string p, if we run out of pattern characters then we didnt match
                                                                    #therefore it is false 
                                                                                
            match = i < len(s) and (s[i] == p[j] or p[j] == ".") #since we know that as long we still have to check for values for 
                                                                 #string s, "." can be any value and if they both equal then its ok
            
            if ((j+1) < len(p)) and p[j+1] == "*": #check for first of the preceding operator "*"

            #FOLLOWING HAVE TWO PATHS USE OR NOT USE:

                 cache[(i,j)] = (dfs(i,j+2) or #dont use the preceding value for not matching  
                                (match and dfs(i+1,j))) #use if match is true then move the i value of string s to the next index 

                                #match ensures s[i] matches p[j]                 
                 return cache[(i,j)]

            if match:
                cache[(i,j)] = dfs(i+1,j+1) #if they just match move to check the next index of the strings with the dfs
                return cache[(i,j)]

            cache[(i,j)] = False #even after all that if we didnt match then just return false 
            return cache[(i,j)]
        
        return dfs(0,0)