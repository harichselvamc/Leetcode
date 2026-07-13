class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=0
        max2=0

        for number in nums:

            if number > max1:
                max2=max1
                max1=number
            elif number>max2:
                max2=number
        
        return (max1-1)*(max2-1)
            
