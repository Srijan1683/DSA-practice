"""Set Mismatch"""

"""Problem: https://leetcode.com/problems/set-mismatch/"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dupe = -1
        miss = -1
        for num in nums:
            if nums[abs(num)-1] < 0:
                dupe = abs(num)
            else:
                nums[abs(num)-1] *= -1
        
        for i in range(len(nums)):
            if nums[i]>0:
                miss = i+1
            
        return [dupe,miss]