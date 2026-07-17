class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # [0,1,2,0,6]
        index=0

        for number in nums:
            if number!=0:
                nums[index]=number
                index=index+1
        while index<len(nums):
            nums[index]=0
            index=index+1

        