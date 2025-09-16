class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')',
                   '{':'}',
                   '[':']' }
    #storing the brackets in this dict
        stack = []
    #The stack is empty for now
        for character in s:
            if character in brackets.keys():
                stack.append(brackets[character])
#Here keys are the opening brackets so we will be appending closing bracket equivalent to the stack
#This maps the opening brackets only too

            elif character in brackets.values():
#if there is no stack that means the opening brackets never entered first
#if there is but its not close properly or in order then it shouldnt be equal to the latest
#bracket released
                if not stack or character != stack.pop():
                    return False
            else:
                return False  #illegal character other than brackets is passed
        return not stack
    #empty set should return false so opposite of that is true, plus after loops
    # valid parenth string should have empty stack