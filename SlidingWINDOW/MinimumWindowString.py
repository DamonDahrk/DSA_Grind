
# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":  return ""
        #edge case for empty target
        THash,Window = {}, {}     
        resLen = float('infinity')
        #we need minimu value so starting with the largest possible and
        #go down from there
        res = [-1,-1] #random two pointers (index for returning later)
        left = 0 #initial left is 0

        for character in t:
            THash[character] = THash.get(character, 0) + 1
        #for character add 1 
        have = 0
        need = len(THash)

        for right in range (len(s)):
            character = s[right]
            Window[character] = Window.get(character, 0) + 1
            #adding to our Window counter
            if character in THash and Window[character] == THash[character]:
                #if two have the same values 
                have += 1 
            while have == need: #as long as this stays valid
                if (right - left + 1) < resLen: #this will run atleast once
                    resLen = right - left + 1 #update the resuts
                    res = [left, right]
                Window[s[left]] -= 1 #remove from left
                #have has to update too
                if s[left] in THash and Window[s[left]] < THash[s[left]]:
                    have -= 1
                #we care only if the left character is in our T in the firstPlace
                left += 1 #left will be moved anyways to update      
     
        left, right = res #update left and right for last minimum positions

        if resLen == float('infinity'): #if the result was ever updated or not
            return ""
        else:
            return s[left:right+1]  #return the string for updated




        