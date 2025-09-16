
# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
#for the number to generate brackets, we need to make sure that
#number of opening brackets = closing brackets and that its valid
# closingbrackets = opening brackets = n condition1
# openingbrackets> closingbrackets because there cant be more close brackets than opening before closing

        stack = [] #stack to compute our logic
        result = [] #the result list we need to return and print to store possible combinations

        def backTracking(openingBrackets,closingBrackets):
            #recursively solving this better approach for possibilites and cleaning stack
                if (openingBrackets == closingBrackets == n):
                    result.append(''.join(stack))
                    return
    #We combine the stack values to an empty string and then append that
    #Valid bracket combo to the result list we will print
                if (closingBrackets < openingBrackets):
                    stack.append(')')
                    backTracking(openingBrackets,closingBrackets+1)
                    stack.pop()
    #Opening brackets can never be more than number of generation level 
    #but you can add as many till it reaches the equal
                if(openingBrackets<n):
                    stack.append('(')
                    backTracking(openingBrackets+1,closingBrackets)
                    stack.pop()
    #keep going to recursive branches and adding values to explore possibilites and return result
    #clean up with pop
        #starting with zero
        backTracking(0,0)
        return result
        