class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        temp={}
        for i in range(len(nums)-1):
            if key==nums[i]:
                nextnumber=nums[i+1]
                temp[nextnumber]=temp.get(nextnumber,0)+1

        max_value=0

        for value in temp.values():
            if value>max_value:
                max_value=value



        for key,value in temp.items():

            if value==max_value:

                return key
                







