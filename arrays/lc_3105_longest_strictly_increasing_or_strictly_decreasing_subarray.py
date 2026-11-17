"""3105. Longest Strictly Increasing or Strictly Decreasing Subarray"""

"""Problem: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/"""


class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc = dec = best = 1
        for i in range (1, len(nums)):
            if nums[i] > nums[i-1]:
                dec = 1
                inc += 1
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            best = max(inc,dec,best)
        return best