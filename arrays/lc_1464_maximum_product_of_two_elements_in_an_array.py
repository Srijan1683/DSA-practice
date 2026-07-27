"""1464. Maximum Product of Two Elements in an Array"""

"""Problem: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return ((nums[-1]-1) * (nums[-2]-1))