"""3736. Minimum Moves to Equal Array Elements III"""

"""Problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/description/"""


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums) * len(nums) - sum(nums)