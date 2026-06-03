"""Concatenation of Array"""

"""https://leetcode.com/problems/concatenation-of-array/"""

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = nums*2
        return ans