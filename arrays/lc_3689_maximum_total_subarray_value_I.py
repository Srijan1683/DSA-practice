"""3689: Maximum Total Subarray Value I"""

"""Problem: https://leetcode.com/problems/maximum-total-subarray-value-i/description/"""

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return k * (max(nums) - min(nums))