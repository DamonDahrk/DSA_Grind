# Input: s = "XYYX", k = 2

# Output: 4

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        #This is gonna be the dictionary to store the counts
        #EG: {'A': '2', 'B': '3' }
        ResultLongest = 0 #We will add the longest repeating string here

        left = 0 #left window will be here for right to move later

        for right in range (len(s)):
            count[s[right]] = 1 + count.get(s[right],0) 
        #for right character add counter on spotting  and if it doesnt exist then add 1 to 0
            while (right-left+1) - max(count.values()) > k:
                #max sequence minus longest repeating character value should give us the 
                #k replacements to be done: but if it is larger then 
                count[s[left]] -= 1
            #here we will subtract the counter of character which we are removing or sliding off
            #and reduce the count likewise to get out of the while loop
                left = left+1
            ResultLongest = max(ResultLongest,right-left+1 )
            #update longest non repeating segment 
        return ResultLongest
