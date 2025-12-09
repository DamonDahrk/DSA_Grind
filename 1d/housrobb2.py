class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
    #utitilizing helper functions and making sure the circular and the logic of greater houses only applies ignoring the last house
    #and the first house and therefore we take the max of those two only to prevent last first value overlapping
        return max(
            self.helper(nums[1:]),
            self.helper(nums[:-1])
        )

    def helper(self, houses):
            rob1,rob2 = 0,0
            for n in houses:
                temp = max(rob1+n,rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        