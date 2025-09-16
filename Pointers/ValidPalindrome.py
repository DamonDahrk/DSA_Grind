class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right = 0,len(s) - 1
        #initializing left and right counters at each ends respectively
        #Problem says to skip all non-alphanumeric characters,
        #its okay if it exists just skip them

        while(left<right): #to maintain the checks
            #skip non alphanum
            while(left<right and not self.isAlphanumeric(s[left])):
                left += 1
            while(left<right and not self.isAlphanumeric(s[right])):
                right -= 1
            #call fumc using self
            
            if(s[left].lower() != s[right].lower()):
                return False
            right -= 1
            left += 1
        return True



    def isAlphanumeric(self,character):
        return ((ord('A') <= ord(character) <= ord('Z')) or
                (ord('a') <= ord(character) <= ord('z')) or
                (ord('0') <= ord(character) <= ord('9')))
        #using ASCII value to check incase we are not allowed to use isalnum()