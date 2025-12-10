class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums) #first we want to establish the fact we are taking the maximum number from the list
                            #i.e 1 x Max num
        
        minNum, maxNum = 1,1 #the lowest num possible

        for num in nums:
            if num == '0':
                minNum, maxNum = 1,1 #if there is zero we can ignore zero and reset the values to 1
            
            temp = maxNum*num
            maxNum = max(maxNum*num, minNum*num, num)
            minNum = min(temp,minNum*num,num) 
            #we are using max num and min num because there is a chance that negative x negative = positive so alternate paths with other numbers can be explored
            result = max(maxNum,result)  
        
        return result
        