class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicate=False
        seen=set()

        for i in nums:
            if i in seen:
                duplicate=True
            else:
                seen.add(i)
        
        return duplicate