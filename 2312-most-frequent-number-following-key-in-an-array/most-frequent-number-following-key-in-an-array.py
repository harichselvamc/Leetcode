class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        # nums = [1,100,200,1,100]
        temp={}
        
        for i in range(len(nums)-1):
            if nums[i]==key:
                nextnumber=nums[i+1]
                temp[nextnumber]=temp.get(nextnumber,0)+1
        
        #{100: 2}

        max_value=0

        for value in temp.values():
            if value>max_value:
                max_value=value
        

        # max_value=2


        for key,value in temp.items():
            if max_value==value:
                return key

