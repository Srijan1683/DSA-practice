"""How many Numbers are smaller than the current Number"""

"""https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/"""


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
