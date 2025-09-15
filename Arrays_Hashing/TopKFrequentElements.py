# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        FreqOfOccurence = {} #initiliazed as dictionary
        for number in nums:
            FreqOfOccurence[number] = FreqOfOccurence.get(number,0)+ 1 
            #key is the number and value is the occurence if no value there keep it zero
        
        FreqBucket = [[] for i in range (len(nums)+1)]
        #Creating the empty list bucket which will be len of list because it has to be within
        #max len and occurence cannot exceed that keeping this within O log n smartly
        for number,frequencies in FreqOfOccurence.items():
            #for the key value of the above
            FreqBucket[frequencies].append(number)
            #the key is the occurence and list added are the values who have that index occurence

        #Everything has been initialized now the solution:

        result = []
        for i in range (len(nums),0,-1):
            #we are starting from the last bucket (most common occurence)
            result.extend(FreqBucket[i])
            #extend is used when adding multiple items and not just a single
            
            if len(result) == k: #top k common result
                return result
        
        return result
