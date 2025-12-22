class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} #this dictionary will keep track of the last index of the character
        
        for i,c in enumerate(s):
            lastIndex[c] = i
        
        #this will always update the last index of a recurring char in the string
        result = [] #where we will be keeping the partition labels
        size,end = 0,0 #end of the spot of the partition 

        for i,c in enumerate(s):
            end = max(end,lastIndex[c]) #end limit set for an occurence character 
            size += 1

            if i==end :
                result.append(size) #append the size for labels
                size = 0
                

        return result

        