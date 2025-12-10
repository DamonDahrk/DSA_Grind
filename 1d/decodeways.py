class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s) #size of the code 
        if s[0] == '0': #cant start with 0, needs to be within 1-26
            return 0 
        if n == 0 :
            return 0
        dp = [0] * (n+1) #making the dp table for  decode paths
        dp[0] = 1 #for empty value only 1 way
        dp[1] = 1 #first digit is not 0 so also 1
        for i in range (2,n+1):
            one_digit = int(s[i-1:i]) #for s=12 we are taking single digit i.e 2
                                 #s[1:2] = 2 
            two_digit = int(s[i-2:i]) #s[0:2] = 12 which is tens place
            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1] #valid units place add the decode path as one
            if 10<= two_digit <= 26:
                dp[i] += dp[i-2] #valid two digits add as one, i-2 cuz what if
                                 #0 single place then make sure we add last to last
                                 #valid decode path if in range, else crash the decode
                                 #path and return 0
        return dp[n] #last value in the table must have the possible valid ways.

        