class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if j!=i and nums[j]<nums[i]:
                    count=count+1
            new.append(count)
        return new