class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        #You have to arrange to the two strings in sort of like 2d matrix, if you match you move diagonal 
        #if you dont then check for right and left
        # 0 a b c d
        # d 0 0 0 1 0
        # a 1 1 1 1 0
        # c 1 1 2 2 0
        #   0 0 0 0 0

        dp = [[0 for j in range(len(text2)+1)] for i in range (len(text1)+1)] #extra range cuz of the 0th rows

        for i in range (len(text1) - 1,-1,-1):  #bottomj down approach
            for j in range(len(text2) - 1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1  #diagonal plus 1
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])  #max of below or right
        
        return dp[0][0]



        