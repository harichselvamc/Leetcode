class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n*(n+1)/2
        # 3*(3+1)/2
        #3*4/2
        #12/2
        #6
        #3+0+1=4
        #6-4=2


        n=len(nums)

        formula=n*(n+1)/2

        totalingivenarray=sum(nums)

        output=formula-totalingivenarray

        return output



        