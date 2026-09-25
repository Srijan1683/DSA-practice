"""3550. Smallest Index with Digit Sum Equal to INdex"""

"""Problem: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/"""


class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            if sum(map(int, str(num))) == i:
                return i
        return -1