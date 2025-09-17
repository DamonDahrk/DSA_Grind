# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)    #length of the substring present below
        n2 = len(s2) #length of the bigger string to check the fixed sliding window against

        if n1 > n2:
            return False
        #if the substring is greater than actual string 
        
        #counters hash map
        s1count = [0] * 26
        s2count = [0] * 26

        for i in range (n1):
            s1count[ord(s1[i]) - ord('a')] += 1 #position in the ASCII value raise the counter
            s2count[ord(s2[i]) - ord('a')] += 1
        
        if s1count==s2count:
            return True #if the hash map initially matches then just return true right away

        for i in range(n1,n2): #starting from the next character after length of s1 to end of bigger string
            s2count[ord(s2[i]) - ord('a')] += 1
            s2count[ord(s2[i - n1]) - ord('a')] -= 1
            #remove count from the first element i.e i-n1 to move the fixed sliding window
            if s1count==s2count:
                return True #again check for every sliding window slide
        return False #if it didnt match at all
        