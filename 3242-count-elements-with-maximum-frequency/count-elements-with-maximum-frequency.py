class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}

        for number in nums:
            if number in freq:
                freq[number]=freq[number]+1
            else:
                freq[number]=1
        
        maximum=max(freq.values())

        # for value in freq.values():
        #     if value>maximum:
        #         maximum=value

        
        count =0 

        for digit in freq.values():
            if digit==maximum:
                count=count+1
        

        return count*maximum


        