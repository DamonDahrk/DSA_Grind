# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #where we will compute 

        for character in tokens:
            if character == '+':
                stack.append(stack.pop() + stack.pop())
            elif character == '*':
                stack.append(stack.pop() * stack.pop())
            elif character == '-':
                a,b = stack.pop(),stack.pop()
                stack.append(b-a) 
                #to substract properly
            elif character == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a)) #round down the decimal to int 
            else:
                stack.append(int(character)) #add the numbers to stack
        
        return stack[0] #only one value should exist in the stack that should return the true result 

        