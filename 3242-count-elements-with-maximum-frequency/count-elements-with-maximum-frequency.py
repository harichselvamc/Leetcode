class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicst={}

        for num in nums:
            if num in dicst:
                dicst[num]=dicst[num]+1
            else:
                dicst[num]=1
    
        # maximum=max(dicst.values())
        maximum=0

        for value in dicst.values():
            if value>maximum:
                maximum=value

        value=0

        for number in dicst.values():
            if number==maximum:
                value=value+number


        return value        