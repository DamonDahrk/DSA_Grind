class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -1 * 2**31  
        #boundaries established

        sign = -1 if x < 0 else 1  #to not check for the min 
        result = 0 #the reverse integer to be computed

        x = abs(x)  #again ignore the negative 

        while x: #as long as x is not zero 
            digit = x%10  #reverse begins by getting the last digit
            x = x // 10        #remove the last added digit from the number now 

            if (result > INT_MAX//10) or (result == INT_MAX and digit > INT_MAX%10 ):  #check for overflow by checks if digit is 
                return 0                                                                #greater than 7 case in units place 

            result = result * 10 + digit

        return result * sign # add the sign back here   


        