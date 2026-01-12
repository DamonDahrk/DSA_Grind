class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() #we are adding all the result in the set to prevent dups and keep track
        while n!= 1: #this loop will keep going (cyclical) until this conditon is met
            if n in seen:
                return False #we found a result that we met before so we are in inf loop hence false
            seen.add(n) #if not then add this number to the set for future loops

            n = sum(int(digit) ** 2 for digit in str(n))
            #first we convert the number to string to iterate the digits to tens^2 + units^2  
            #we loop the num and wrap the thing in sum for  1^2 + 0^2 + 0^2 = 1 result 

        return True #we got out of loop hence the result is non cyclical
        