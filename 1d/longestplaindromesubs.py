class Solution:
    def longestPalindrome(self, s: str) -> str:

        #We are going to be having left and right indexes to go left (-1) and right(+1) to compute the palindrome by matching
        #then eventually return the max substring 

        if not s and len(s) == 1:
            return s 

        start,end = 0,0 #will update the value to return the longest substring as s[start:end+1] i.e including the last value

        def palindromecheck(left: int,right: int) -> tuple[int,int]: #function to check the validity of the palindrome 
            #ideally from the centre
            while left>=0 and right<len(s) and s[left]==s[right]: #inbounds and eq for palindrome validity
                left = left - 1
                right = right + 1
            
            return left+1,right-1 #the loop will have exited the bounds at least once 
        
        for i in range (0,len(s)):
            #for odd length: 
            oddleft,oddright = palindromecheck(i,i) 

            #for even length:
            evenleft,evenright = palindromecheck(i,i+1)

            #check which one has the longest substring palindrome by comparing lengths and then return that answer 
            
            if oddright-oddleft > end-start:
                start,end = oddleft,oddright
            if evenright-evenleft > end-start:
                start,end = evenleft,evenright
        
        return s[start:end+1]





        