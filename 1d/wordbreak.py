class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        #we are converting the word dict to set 
        word_set = set(wordDict)
        n = len(s)#length of the string to be broken down
        dp = [False] * (n+1) 
        #we are creating a dp table for checking the string segments to see
        #if our original string can be broken apart or not
        dp[0] = True
        #Empty String is always true 

        max_len = max((len(w) for w in word_set) ,default=0)
        #generator expression in parameterized form, so now we will have a list of 
        #length of all subst words

        for i in range (1,n+1):
            start_j = max(0,i-max_len)
            #whatever the max length of the largest substring is it cannot be more than 
            #the size of the string so we avoid repeated checks till what we have checked already

#max len is 4

            for j in range (start_j,i): #check till the last ith index of the string 
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
        #last value is always the real result if the word can be broken up

        