"""How many Numbers are smaller than the current Number"""

"""Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array."""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=0
        res=[]
        for num in nums:
            for i in range(0,len(nums)):
                if num > nums[i]:
                    count+=1
            res.append(count)
            count=0
        return res
