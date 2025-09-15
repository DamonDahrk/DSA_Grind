# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

#Please implement encode and decode

class Solution:

    def encode(self, strs: List[str]) -> str:
        #Assume you get a list of string strs to code
        #Lets generate the empty string first:
        result = ""
        #Now you get for every string in the list:
        for string in strs:
        #we add a number i.e length and then delimiter and then add the string
            result = result + str(len(string)) + "|" + string
        #as a result we can tell words apart and their length and delimiter to convert it back
        return result


    def decode(self, s: str) -> List[str]:

        #First we get the to be sent decoded Result list:
        ResultList = []
        i = 0 
        #to iterate 

        while i<len(s):
            #As long as we stay in bounds of the string
            j = i #setting the delimiter and finding the word eventually
            while s[j] != "|":
                j += 1
            LenOfIndividualString = int(str(s[i:j])) #len of individual strings
            ResultList.append(str(s[j+1:j+1+LenOfIndividualString]))
            #adding the word decoded
            i = j+1+LenOfIndividualString # now at the start of the next word
        
        return ResultList


