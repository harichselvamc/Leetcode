class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index=0
        for i in range(len(nums)):
            if val!=nums[i]:
                nums[index]=nums[i]
                index=index+1
        
        return index