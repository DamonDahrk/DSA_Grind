class Solution:
    def countSubstrings(self, s: str) -> int:
       
    #same prob as last but with counting
        def palindromefunction(left: int, right: int) -> tuple[int,int]:
            count = 0 
            while left>=0 and right<len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        total = 0
        for i in range (0,len(s)):
            total += palindromefunction(i,i)
            total += palindromefunction(i,i+1)
        
        return total

    
    
        