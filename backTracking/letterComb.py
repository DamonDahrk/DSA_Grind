# You are given a string digits made up of digits from 2 through 9 inclusive.

# Each digit (not including 1) is mapped to a set of characters as shown below:

# A digit could represent any one of the characters it maps to.

# Return all possible letter combinations that digits could represent. You may return the answer in any order.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        #combinations of characters in the phone that are possible
        chardict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtracking(i,thestring) :
            if len(digits) == len(thestring):
                combinations.append(thestring)
                return
            #if the length of the string entered by the user equals the possible character combos letterwise

            for c in chardict[digits[i]]:
            #iterate thru individual a b c in the numbers
                    backtracking(i+1,thestring+c)
            
        
        if digits: #incase the user inputs an empty number characters then we return an empty string
            backtracking (0,"")
            

        return combinations   
