class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1] #first reverse the list of array digits to make it easier

        one, i = 1,0 #i will iterate we are using while loop because of one as a control

        while one!=0: #as long as the control case is valid
            if i < len(digits): # as long as we stay in bounds
                if digits[i] == 9: #special edge case where we will carry over the 1 next
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0 #we dont have to carry over anymore
            else:
                digits.append(1) #we are adding a new value at the end to represent the specific 99 -> 100 sitch
                one = 0 #no need to go through the loop again
            i += 1
        
        return digits[::-1] #return the actual processed array 
        