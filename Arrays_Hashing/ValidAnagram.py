# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# You should aim for a solution with O(n + m) time and O(1) space, where n is the length of the string s and m is the length of the string t.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
          if len(s) != len(t):
                return False
          #If the length is not the same there is no way anagram is possible

          count = {}
          #empty dictionary for the count

          for value in s:
            count[value] = count.get(value, 0) + 1
        
        #counting the value of string key value pair with occurence
        
          for value in t:
            if value not in count or count[value] == 0:
                #This means that either the char is not in string or it is in unequal amounts
                return False
            count[value] = count[value] - 1
          return True
        