"""Set Mismatch"""

"""You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array."""

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