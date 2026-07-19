"""1979. Find Greatest Common Divisor of Array"""

"""Problem: https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/"""

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = min(nums), max(nums)
        while b:
            a, b = b, a % b
        return a