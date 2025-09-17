#BINARY SEARCH

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #given search binary method given in o log n

        left,right = 0, len(nums) - 1 #first and last element

        while left<=right : #reaching left has to be smaller
            mid = ((left + right) // 2) #middle index
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                #the array is in ascending order so if the middle value is lower then increase the
                #counter for lowest to lower
                left += 1
            else:
                right -= 1
        return -1 #illegal search values


        