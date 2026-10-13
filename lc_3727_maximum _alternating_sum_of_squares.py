"""3727. Maximum Alternating Sum of Squares"""

"""Problem: https://leetcode.com/problems/maximum-alternating-sum-of-squares/description/"""


class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sq = sorted((x * x for x in nums), reverse=True)
        n = len(sq)
        pos = (n + 1) // 2
        return sum(sq[:pos]) - sum(sq[pos:])