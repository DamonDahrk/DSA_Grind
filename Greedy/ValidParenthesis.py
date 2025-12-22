class Solution:
    def checkValidString(self, s: str) -> bool:
        #for the greedy approach that will yield o(n) complexity.
        # we will have two varialbles to account for ( or ) 
        leftMin,leftMax = 0,0
        for c in s:
            if c == '(':
                leftMin , leftMax = leftMin  + 1 , leftMax + 1 #no choice because we are adding a open parenthesis case 
            elif c == ')':
                leftMin , leftMax = leftMin  - 1 , leftMax - 1 #similarly a parenthesis situation is closed
            else:
                leftMin , leftMax = leftMin  - 1 , leftMax + 1 
            if leftMax < 0: #Max range can never be negative that means there is no way parenth loop will ever close 
                return False
            
            if leftMin < 0:
                leftMin = 0 #we are not accounting for empty value for "*" so we have to update incase left value goes negative
        
        return leftMin == 0 #if atleast the lowest range 0 then the parenthesis loop is closed so return
        