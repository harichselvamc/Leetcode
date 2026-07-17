class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
            
        index=0

        for number in nums:
            if number!=0:
                nums[index]=number
                index=index+1

        while index<len(nums):
            nums[index]=0
            index=index+1

        return nums