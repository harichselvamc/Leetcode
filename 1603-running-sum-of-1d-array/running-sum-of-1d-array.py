class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [1,2,3,4]
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        
        return nums