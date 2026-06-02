"""Max Consecutive Ones"""

"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        streak=0
        maxstreak=0
        for i in range(n):
            if nums[i]==1:
                streak+=1
                
            else:
                streak=0

            maxstreak=max(streak,maxstreak)
        return maxstreak