# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterSet = set()
        #set cannot have duplicate values so its perfect to store string characters here
        leftwindow = 0 #the left window is empty for now
        LongestSubstringLength  =  0

        for rightwindow in range (len(s)):
            while s[rightwindow] in characterSet:
                characterSet.remove(s[leftwindow])
            #remove duplicate value and keep sliding the window
                leftwindow += 1
        #if dup exists then re
            characterSet.add(s[rightwindow])
            #add for non dup values
            LongestSubstringLength = max(LongestSubstringLength, rightwindow-leftwindow+1 )
        #keep updating length if bigger sequence is found , +1 is for int 0
        return LongestSubstringLength
        